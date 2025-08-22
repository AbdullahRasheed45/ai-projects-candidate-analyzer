import os
import re
import yaml
import streamlit as st
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.nebius import Nebius
from agno.tools.github import GithubTools
from agno.tools.exa import ExaTools
from agno.tools.thinking import ThinkingTools
from agno.tools.reasoning import ReasoningTools

# Load environment variables from .env if present
load_dotenv()

# Load prompts from YAML file
def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

prompts = load_yaml("hiring_prompts.yaml")
description_multi = prompts.get("description_for_multi_candidates", "")
instructions_multi = prompts.get("instructions_for_multi_candidates", "")
description_single = prompts.get("description_for_single_candidate", "")
instructions_single = prompts.get("instructions_for_single_candidate", "")

# Configure Streamlit page
st.set_page_config(page_title="Candilyzer", layout="wide")

# Initialize session state with environment variables
for key in ["NEBIUS_API_KEY", "MODEL_ID", "GITHUB_API_KEY", "EXA_API_KEY"]:
    if key not in st.session_state:
        st.session_state[key] = os.getenv(key, "")

# Sidebar for API keys and settings
st.sidebar.title("API Keys & Settings")
st.session_state["NEBIUS_API_KEY"] = st.sidebar.text_input("Nebius API Key", value=st.session_state["NEBIUS_API_KEY"], type="password")
st.session_state["MODEL_ID"] = st.sidebar.text_input("Model ID", value=st.session_state["MODEL_ID"])
st.session_state["GITHUB_API_KEY"] = st.sidebar.text_input("GitHub API Key", value=st.session_state["GITHUB_API_KEY"], type="password")
st.session_state["EXA_API_KEY"] = st.sidebar.text_input("Exa API Key", value=st.session_state["EXA_API_KEY"], type="password")

page = st.sidebar.radio("Select Page", ("Multi-Candidate Analyzer", "Single Candidate Analyzer"))

# Header
st.markdown("<h1 style='text-align:center'>Candilyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Elite GitHub and LinkedIn Candidate Analyzer</p>", unsafe_allow_html=True)

# Multi-candidate mode
if page == "Multi-Candidate Analyzer":
    st.header("Multi-Candidate Analyzer")
    with st.form("multi_form"):
        github_usernames = st.text_area("GitHub Usernames (one per line)", placeholder="username1\nusername2\n...")
        job_role = st.text_input("Target Job Role", placeholder="Backend Engineer")
        submit = st.form_submit_button("Analyze Candidates")
    if submit:
        if not github_usernames or not job_role:
            st.error("Please enter usernames and job role.")
        elif not all([st.session_state["NEBIUS_API_KEY"], st.session_state["MODEL_ID"], st.session_state["GITHUB_API_KEY"], st.session_state["EXA_API_KEY"]]):
            st.error("Please provide all API keys and model ID.")
        else:
            usernames = [u.strip() for u in github_usernames.split("\n") if u.strip()]
            query = f"Evaluate GitHub candidates for role '{job_role}': {', '.join(usernames)}"
            agent = Agent(
                description=description_multi,
                instructions=instructions_multi,
                model=Nebius(
                    id=st.session_state["MODEL_ID"],
                    api_key=st.session_state["NEBIUS_API_KEY"],
                ),
                name="CandilyzerMulti",
                tools=[
                    ThinkingTools(think=True, instructions="Strict GitHub candidate evaluation"),
                    GithubTools(access_token=st.session_state["GITHUB_API_KEY"]),
                    ExaTools(api_key=st.session_state["EXA_API_KEY"], include_domains=["github.com"], type="keyword"),
                    ReasoningTools(add_instructions=True)
                ],
                markdown=True,
                show_tool_calls=True
            )
            st.markdown("### Evaluation in Progress...")
            with st.spinner("Running analysis..."):
                stream = agent.run(query, stream=True)
                output = ""
                placeholder = st.empty()
                for chunk in stream:
                    if hasattr(chunk, "content") and isinstance(chunk.content, str):
                        output += chunk.content
                        placeholder.markdown(output, unsafe_allow_html=True)
# Single candidate mode
else:
    st.header("Single Candidate Analyzer")
    with st.form("single_form"):
        github_username = st.text_input("GitHub Username", placeholder="username")
        linkedin_url = st.text_input("LinkedIn Profile (optional)", placeholder="https://linkedin.com/in/...")
        job_role = st.text_input("Job Role", placeholder="ML Engineer")
        submit_single = st.form_submit_button("Analyze Candidate")
    if submit_single:
        if not github_username or not job_role:
            st.error("Please enter GitHub username and job role.")
        elif not all([st.session_state["NEBIUS_API_KEY"], st.session_state["MODEL_ID"], st.session_state["GITHUB_API_KEY"], st.session_state["EXA_API_KEY"]]):
            st.error("Please provide all API keys and model ID.")
        else:
            query = f"Analyze candidate for {job_role}. GitHub: {github_username}"
            if linkedin_url:
                query += f", LinkedIn: {linkedin_url}"
            agent = Agent(
                description=description_single,
                instructions=instructions_single,
                model=Nebius(
                    id=st.session_state["MODEL_ID"],
                    api_key=st.session_state["NEBIUS_API_KEY"]
                ),
                name="CandilyzerSingle",
                tools=[
                    ThinkingTools(add_instructions=True),
                    GithubTools(access_token=st.session_state["GITHUB_API_KEY"]),
                    ExaTools(api_key=st.session_state["EXA_API_KEY"], include_domains=["linkedin.com", "github.com"], type="keyword"),
                    ReasoningTools(add_instructions=True)
                ],
                markdown=True,
                show_tool_calls=True,
                add_datetime_to_instructions=True
            )
            st.markdown("### Evaluation in Progress...")
            with st.spinner("Analyzing candidate..."):
                stream = agent.run(query, stream=True)
                output = ""
                placeholder = st.empty()
                for chunk in stream:
                    if hasattr(chunk, "content") and isinstance(chunk.content, str):
                        output += chunk.content
                        placeholder.markdown(output, unsafe_allow_html=True)
            match = re.search(r"\b([1-9]?\d|100)/100\b", output)
            if match:
                score = int(match.group(1))
                st.success(f"Candidate Score: {score}/100")
