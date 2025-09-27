# 👨‍💻 Candidate Analyzer: AI-Powered Technical Recruitment

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Agno](https://img.shields.io/badge/Agno-Framework-purple?style=for-the-badge)](https://agno.dev/)
[![GitHub](https://img.shields.io/badge/GitHub_API-181717?style=for-the-badge&logo=github&logoColor=white)](https://docs.github.com/en/rest)

## Overview

**Candidate Analyzer** revolutionizes technical recruitment by leveraging AI to analyze developer profiles across GitHub and LinkedIn. Built with Agno framework and powered by Nebius AI, this tool provides comprehensive candidate assessment through intelligent analysis of code repositories, contribution patterns, and professional presence.

Whether you're screening multiple candidates for a role or conducting deep-dive analysis of individual profiles, this system delivers consistent, data-driven insights to support your hiring decisions.

### Key Features

- **Multi-Candidate Analysis**: Discover and rank candidates based on role requirements
- **Deep Profile Assessment**: Comprehensive technical evaluation of individual developers  
- **Intelligent Data Aggregation**: Combines GitHub repositories, contribution history, and web presence
- **Configurable Scoring Rubric**: Customizable evaluation criteria via YAML configuration
- **Streamlit Web Interface**: User-friendly dashboard for analysis and report generation
- **Professional Reports**: Detailed Markdown reports with competency scores and evidence
- **Agentic Workflow**: Orchestrated data gathering and analysis using AI agents

### Perfect For

- **Technical Recruiters**: Streamline candidate screening and evaluation processes
- **Hiring Managers**: Make data-driven decisions with comprehensive candidate insights
- **Development Teams**: Assess potential team members based on actual code contributions
- **HR Departments**: Standardize technical evaluation criteria across roles
- **Talent Acquisition**: Scale technical screening for high-volume recruitment

## Architecture

The system employs a sophisticated multi-agent approach to candidate analysis:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Role/Profile  │ ──▶│   AI Agent       │ ──▶│   Data Sources  │
│   Requirements  │    │   (Nebius AI)    │    │                 │
│                 │    │                  │    │ • GitHub API    │
│ • Job Role      │    │ • Search Planning│    │ • Repository    │
│ • Skills Needed │    │ • Data Analysis  │    │ • Contributions │
│ • Experience    │    │ • Score Calculation│  │ • Web Search    │
└─────────────────┘    │ • Report Generation│  └─────────────────┘
                       └──────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Assessment        │
                    │   Engine            │
                    │                     │
                    │ • Competency Scoring│
                    │ • Evidence Gathering│
                    │ • Risk Assessment   │
                    │ • Ranking Algorithm │
                    │ • Report Generation │
                    └─────────────────────┘
```

## Project Structure

```
.
├── app.py                 # Agent orchestration and tool configuration
├── main.py               # Streamlit application entry point
├── hiring_prompts.yaml   # Scoring rubric and evaluation criteria
├── .env.example          # Environment variable template
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore patterns
├── LICENSE              # MIT license
└── README.md            # This documentation
```

## Quick Start

### Prerequisites

- Python 3.10 or higher
- API keys for Nebius AI, GitHub, and Exa search
- Understanding of technical recruitment needs

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdullahRasheed45/ai-projects-candidate-analyzer.git
   cd ai-projects-candidate-analyzer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Set up API keys:**
   ```bash
   # Required API keys in .env
   NEBIUS_API_KEY=your_nebius_api_key
   GITHUB_API_KEY=your_github_api_key
   EXA_API_KEY=your_exa_api_key
   
   # Optional model configuration
   MODEL_ID=meta-llama/Llama-3.3-70B-Instruct
   ```

5. **Launch the application:**
   ```bash
   streamlit run main.py
   ```

## Usage Modes

### Multi-Candidate Analysis

Perfect for initial screening and candidate discovery:

**Input:**
- **Role**: "Senior Full-Stack Developer"
- **Candidate Count**: 10
- **Required Skills**: React, Node.js, Python, AWS

**Process:**
1. AI agent searches GitHub for developers with relevant skills
2. Analyzes public repositories and contribution patterns  
3. Evaluates code quality, project complexity, and activity levels
4. Ranks candidates based on role fit and technical competency

**Output:**
```markdown
# Candidate Analysis Report: Senior Full-Stack Developer

## Top Candidates (Ranked)

### 1. john_developer (Score: 8.7/10)
- **Strengths**: Extensive React/Node.js portfolio, active contributor
- **Key Repositories**: enterprise-dashboard, microservices-api
- **Activity Level**: 500+ commits in last 6 months
- **Risk Factors**: Limited cloud deployment experience

### 2. sarah_coder (Score: 8.4/10)  
- **Strengths**: Strong Python/AWS background, technical leadership
- **Key Repositories**: ml-pipeline, serverless-architecture
- **Activity Level**: Consistent daily contributions
- **Risk Factors**: Less frontend experience than ideal
```

### Single-Candidate Deep Dive

Comprehensive assessment for final evaluation:

**Input:**
- **GitHub Username**: "torvalds" 
- **LinkedIn URL**: (optional for additional context)
- **Target Role**: "Senior Software Engineer"

**Analysis Includes:**
- Repository quality and diversity assessment
- Code contribution patterns and consistency
- Technical skill demonstration through projects
- Open source involvement and community impact
- Professional growth trajectory

**Sample Output:**
```markdown
# Technical Assessment: Linus Torvalds

## Overall Score: 9.2/10

### Technical Competencies
- **System Programming**: 10/10 - Exceptional (Linux kernel)
- **Architecture Design**: 9/10 - Strong distributed systems knowledge  
- **Code Quality**: 9/10 - Clean, well-documented contributions
- **Leadership**: 10/10 - Proven technical leadership at scale

### Portfolio Analysis
- **Primary Languages**: C (95%), Shell (3%), Other (2%)
- **Project Complexity**: Extremely high - operating system level
- **Contribution Volume**: 25,000+ commits over 30+ years
- **Community Impact**: Massive - millions of developers affected

### Risk Assessment
- **Low Risk**: Proven track record, exceptional technical depth
- **Considerations**: Specific domain expertise may not translate to all roles
```

## Customizable Scoring Framework

### Scoring Rubric Configuration

Edit `hiring_prompts.yaml` to customize evaluation criteria:

```yaml
# Technical Competencies (Weighted Scoring)
competencies:
  algorithms_data_structures:
    weight: 0.20
    description: "Problem-solving and algorithmic thinking"
    evidence_sources: ["leetcode_style_repos", "algorithmic_projects", "competitive_programming"]
    
  backend_development:
    weight: 0.25  
    description: "Server-side development and API design"
    evidence_sources: ["api_projects", "database_usage", "server_frameworks"]
    
  frontend_development:
    weight: 0.20
    description: "User interface and client-side development" 
    evidence_sources: ["ui_frameworks", "responsive_design", "javascript_proficiency"]
    
  devops_cloud:
    weight: 0.15
    description: "Deployment, infrastructure, and cloud technologies"
    evidence_sources: ["docker_usage", "ci_cd_pipelines", "cloud_deployments"]
    
  communication_collaboration:
    weight: 0.10
    description: "Documentation, code reviews, and team collaboration"
    evidence_sources: ["readme_quality", "pr_descriptions", "issue_discussions"]

# Red Flags and Risk Assessment
risk_factors:
  - "Inactive for 6+ months"
  - "No original projects (only forks)"
  - "Poor code documentation"
  - "Single language/framework focus"
  - "No collaborative contributions"

# Report Generation Settings  
report_format:
  include_code_samples: true
  highlight_standout_projects: true
  provide_improvement_suggestions: true
  include_salary_band_estimate: false
```

### Role-Specific Configurations

```yaml
# Frontend Developer Focus
frontend_role:
  competencies:
    frontend_development: 0.40
    ux_design_sense: 0.20  
    performance_optimization: 0.15
    testing_practices: 0.15
    backend_integration: 0.10

# DevOps Engineer Focus  
devops_role:
  competencies:
    infrastructure_automation: 0.30
    containerization_orchestration: 0.25
    monitoring_observability: 0.20
    security_practices: 0.15
    scripting_automation: 0.10
```

## Advanced Features

### Intelligent Data Aggregation

The system combines multiple data sources for comprehensive analysis:

**GitHub Analysis:**
- Repository metadata (stars, forks, languages)
- Commit history and contribution patterns
- Code quality indicators
- Project complexity assessment
- Collaboration evidence

**Web Intelligence (via Exa):**
- Technical blog posts and articles
- Conference talks and presentations  
- Open source project involvement
- Professional recognition and awards
- Technical community participation

**LinkedIn Integration (Optional):**
- Professional experience timeline
- Skill endorsements and recommendations
- Educational background
- Industry connections and network quality

### Bias Mitigation Features

```python
# Built-in fairness considerations
bias_mitigation = {
    "anonymize_personal_info": True,      # Focus on technical merit
    "diverse_evaluation_criteria": True,   # Multiple competency dimensions  
    "activity_context_awareness": True,    # Consider life circumstances
    "contribution_quality_over_quantity": True,  # Value depth over volume
}
```

### Performance Analytics

Track system effectiveness and candidate quality:

```python
analytics_metrics = {
    "false_positive_rate": "< 15%",       # Candidates who don't perform well
    "time_to_shortlist": "< 2 hours",     # Analysis speed
    "interviewer_alignment": "> 85%",     # Agreement with human reviewers
    "diversity_representation": "Tracked", # Demographic analysis
}
```

## API Integration Details

### GitHub API Usage

```python
# Efficient API usage patterns
github_analysis = {
    "repositories": "public repos, contributions, stars received",
    "activity": "commits, issues, pull requests, code reviews", 
    "languages": "primary languages, project diversity",
    "collaboration": "team projects, open source contributions",
    "rate_limits": "5000 requests/hour with authentication"
}
```

### Exa Search Integration

```python
# Intelligent web search for candidate context
exa_search = {
    "technical_content": "blog posts, tutorials, documentation",
    "speaking_engagements": "conference talks, webinars, podcasts",
    "recognition": "awards, mentions, community impact",
    "thought_leadership": "technical opinions, industry insights"
}
```

## Ethical Considerations

### Privacy and Data Protection
- Uses only publicly available information
- No scraping of private repositories or personal data
- Respects platform terms of service and rate limits
- Option to exclude candidates who opt-out of analysis

### Fair Assessment Practices  
- Standardized scoring criteria across all candidates
- Bias detection and mitigation built into evaluation process
- Focus on demonstrated technical competency over personal characteristics
- Transparent reporting of evaluation methodology

### Responsible AI Usage
- Human oversight required for final hiring decisions
- Regular audit of scoring algorithms for bias
- Clear communication that this is decision support, not automated hiring
- Continuous improvement based on hiring outcome feedback

## Deployment Options

### Local Development
```bash
# Standard local setup
streamlit run main.py
# Access at http://localhost:8501
```

### Hugging Face Spaces
```bash
# Deploy to Hugging Face for team access
# Add secrets: NEBIUS_API_KEY, GITHUB_API_KEY, EXA_API_KEY, MODEL_ID
# Zero configuration changes needed
```

### Enterprise Deployment
```bash
# Docker containerization
docker build -t candidate-analyzer .
docker run -p 8501:8501 --env-file .env candidate-analyzer

# Kubernetes deployment with secrets management
kubectl apply -f k8s-deployment.yaml
```

## Troubleshooting

### API Issues
**"401/403 from GitHub API"**
- Verify GitHub personal access token has correct permissions
- Check rate limit status and usage quotas
- Ensure token hasn't expired

**"Empty search results"**
- Broaden search criteria or increase candidate count
- Verify GitHub usernames exist and are public
- Check for network connectivity issues

### Analysis Problems
**"Weak or inconsistent scores"**
- Review and adjust scoring rubric in `hiring_prompts.yaml`
- Consider role-specific customization
- Verify sufficient data available for analysis

**"Model timeout or errors"**
- Try different MODEL_ID (smaller/faster model)
- Reduce analysis scope to fit token limits
- Check Nebius API status and quotas

### Performance Issues
**"Slow analysis speed"**
- Optimize API request batching
- Consider caching for repeated analyses
- Use faster model variants for initial screening

## Contributing

We welcome contributions to enhance candidate analysis capabilities!

### Development Guidelines

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/analysis-enhancement`
3. Follow ethical AI development practices
4. Test with diverse candidate profiles
5. Submit pull request with evaluation examples

### Contribution Areas

- **Additional Data Sources**: Integration with more platforms (GitLab, Bitbucket)
- **Advanced Analytics**: Machine learning models for better prediction
- **Bias Detection**: Enhanced fairness and bias mitigation features
- **Report Templates**: Industry-specific evaluation frameworks
- **Performance Optimization**: Faster analysis and better caching

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **[Agno Framework](https://agno.dev/)** for AI agent orchestration capabilities
- **[Nebius AI](https://nebius.ai/)** for powerful language model integration
- **[Streamlit](https://streamlit.io/)** for rapid web application development
- **GitHub API** for comprehensive developer data access
- **Exa Search** for intelligent web content discovery

## 📞 Connect & Support

<div align="center">

### 🚀 Ready to Transform Technical Recruitment?

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://techvibes360.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullahrasheed-/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdullahrasheed45@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbdullahRasheed45)

**Let's make technical hiring data-driven and fair!**

</div>

---

*Built with ❤️ by Muhammad Abdullah Rasheed. Ready to revolutionize your technical recruitment process?*
