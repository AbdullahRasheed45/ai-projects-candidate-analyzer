# Candidate Analyzer

AI-powered Candidate Analyzer built with [Agno](https://www.agno.com/), Nebius AI and Streamlit.

## Features
- **Multi-candidate analyzer** – Provide a job role and the number of candidates; the agent searches GitHub for matching users, inspects their public contributions, and compiles a ranked list of the most suitable profiles.
- **Single candidate analyzer** – Enter a GitHub username (and optionally a LinkedIn URL) to generate a detailed technical review and a competency score report for that individual.
- **Strict scoring and professional reports** – The agent uses a rubric defined in `hiring_prompts.yaml` to objectively score each candidate across core competencies and outputs a polished markdown report.
- **Agentic workflow** – Combines GitHub search, Exa web search and Nebius LLM reasoning inside an [Agno](https://www.agno.com/) agent with thinking and reasoning tools.
- **Streamlit UI** – Interactive interface for selecting analysis mode, entering candidate details, viewing analysis results and sharing them with your hiring team.

## Prerequisites
- Python ≥ 3.10
- Nebius AI account and API key
- GitHub API key for searching candidate repositories
- Exa API key for web search
- Optional: a model ID to select a specific Nebius model (e.g. `meta-llama/Llama-3.3-70B-Instruct`).

## Installation
Clone this repository and install the dependencies:
```bash
git clone https://github.com/AbdullahRasheed45/ai-projects-candidate-analyzer.git
cd ai-projects-candidate-analyzer
pip install -r requirements.txt
```

Create a `.env` file by copying `.env.example` and fill in your API keys:
```env
NEBIUS_API_KEY=your_nebius_api_key
GITHUB_API_KEY=your_github_api_key
EXA_API_KEY=your_exa_api_key
MODEL_ID=meta-llama/Llama-3.3-70B-Instruct
```

## Usage
Launch the Streamlit app:
```bash
streamlit run main.py
```

- **Multi-candidate mode**: Enter a job role (e.g. `"machine learning engineer"`) and the number of candidates to fetch. The agent will search for developers on GitHub, evaluate them against the rubric and produce a ranked report.
- **Single candidate mode**: Enter a candidate's GitHub username and (optionally) their LinkedIn profile. The agent will scrape their repositories and public information, generate a detailed report and provide a competency score.

The prompts used for evaluation live in `hiring_prompts.yaml` and can be customised to suit your organisation's hiring rubric.

## Deployment
You can deploy this app to a Hugging Face Space or any platform that supports Streamlit. In Hugging Face, add your secret keys in the Space settings (as `NEBIUS_API_KEY`, `GITHUB_API_KEY`, `EXA_API_KEY` and `MODEL_ID`) and the app will run without modification.

## License
This project is licensed under the MIT License.
