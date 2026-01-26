# 🤖 Customer Support AI System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28.8-purple.svg)](https://github.com/joaomdmoura/crewAI)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Agentic Customer Support Intelligence Platform** — A sophisticated multi-agent AI system with intent detection, persistent memory, risk evaluation, and quality scoring. Inspired by modern AI support products (Freshworks Freddy AI, HubSpot Breeze AI, Salesforce Einstein).

Built with **CrewAI**, **OpenAI models**, and **Python**.

---

## 🌟 Overview

This project implements a **hierarchical multi-agent architecture** specifically designed for high-stakes customer service environments. By leveraging specialized agents, the system ensures that every customer message is analyzed for intent, grounded in history, safely drafted, and evaluated for quality before reaching the user.

### 🧠 The Agentic Brain

The system orchestrates **5 specialized AI Agents** working in a hierarchical workflow:

1. **🔍 Intent Agent**: Classifies the request (billing, technical, etc.), extracts key entities, and assigns a confidence score.
2. **🧠 Memory Agent**: Manages long-term customer preferences and session-based context to ensure personalized responses.
3. **💡 Resolution Agent**: The "Writer" that drafts helpful, factual responses using web search and scraping tools.
4. **🛡️ Risk & Policy Agent**: The "Guardrail" that scans drafts for hallucinations, policy violations, and safety risks.
5. **📊 Evaluation Agent**: The "Quality Control" that scores the final output on Correctness, Empathy, and Confidence.

---

## 🏗️ Architecture & Workflow

```
┌─────────────────┐
│ Customer Message│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Intent Agent   │  ← Classifies request & extracts entities
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Memory Agent   │  ← Retrieves customer history & context
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Resolution Agent│  ← Drafts response with web research
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Risk & Policy  │  ← Validates safety & policy compliance
│     Agent       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Evaluation Agent│  ← Scores quality (Correctness, Empathy)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Final Response  │
└─────────────────┘
```

---

## ✨ Key Features

- 🤖 **Multi-Agent Orchestration**: Hierarchical crew management with specialized agents
- 🔍 **Intent Detection**: Automatic classification and entity extraction
- 💾 **Persistent Memory**: Long-term customer preference tracking
- 🌐 **Web Research**: Real-time information gathering via SerperDev
- 🛡️ **Safety Guardrails**: Risk assessment and policy compliance checking
- 📊 **Quality Scoring**: Quantitative evaluation across multiple metrics
- 🔄 **Tool Integration**: SerperDev search and website scraping capabilities

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenAI API Key
- (Optional) SerperDev API Key for web search capabilities

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Ani-107/Customer-Support-AI-System-Crew-Ai.git
cd Customer-Support-AI-System-Crew-Ai
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure Environment:**
   Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL_NAME=gpt-4-turbo-preview
SERPER_API_KEY=your-serper-key-here
```

---

## 🛠️ Usage

### Run the Core System

Process a single message through the entire agentic pipeline:

```bash
python customer_support_ai.py
```

### Run Test Scenarios

Execute a suite of pre-defined customer support cases:

```bash
python examples/test_scenarios.py
```

---

## 📂 Project Structure

```
.
├── customer_support_ai.py    # Main system implementation
├── examples/
│   └── test_scenarios.py     # Test scenarios and examples
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── LICENSE                   # MIT License
```

---

## 🛠️ Tech Stack

### Core Framework
- **CrewAI** - Multi-agent orchestration framework
- **LangChain** - LLM integration and tooling
- **OpenAI** - GPT-4/GPT-3.5 models

### Tools & Integrations
- **SerperDev** - Web search API
- **ScrapeWebsiteTool** - Website content extraction
- **Python-dotenv** - Environment variable management

### Architecture
- **Hierarchical Process** - Manager LLM for task delegation
- **Sequential Task Flow** - Logical agent execution order
- **Tool Integration** - External API and scraping capabilities

---

## 📊 Technical Capabilities

### Hierarchical Orchestration
Managed by a "Manager LLM" to ensure logical task delegation and optimal agent coordination.

### Tool Integration
- **SerperDev**: Real-time web research for up-to-date information
- **ScrapeWebsiteTool**: Extract relevant content from web pages

### Safety First
Integrated risk assessment agent prevents common AI failures:
- Hallucination detection
- Policy violation checking
- Safety risk evaluation

### Quality Feedback Loop
Every response is quantitatively scored across three key metrics:
- **Correctness**: Factual accuracy
- **Empathy**: Emotional intelligence
- **Confidence**: Response certainty

---

## 🧪 Test Scenarios

The system includes comprehensive test scenarios for:

- 💳 **Billing Issues**: Handling double charges and refund requests
- 🔧 **Technical Support**: Login and account access problems
- 👤 **Account Management**: Subscription cancellations and modifications
- 📦 **Product Inquiries**: Feature availability and integrations

---

## 📖 API & Integration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `OPENAI_MODEL_NAME` | Model to use (default: gpt-4-turbo-preview) | No |
| `SERPER_API_KEY` | SerperDev API key for web search | Optional |

### Agent Configuration

The system uses a hierarchical crew setup:

```python
crew = Crew(
    agents=[intent_agent, memory_agent, resolution_agent, risk_agent, evaluation_agent],
    tasks=[intent_task, memory_task, resolution_task, risk_task, evaluation_task],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3),
    verbose=True
)
```

---

## 🤝 Contributing

Contributions are welcome! Whether it's:
- Adding a new specialized agent
- Improving safety guardrails
- Expanding the toolsets
- Enhancing test scenarios

Feel free to open a PR or issue!

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ani-107 (Anirudh Yadav Mekala)**
- GitHub: [@Ani-107](https://github.com/Ani-107)
- Profile: [View Profile](https://github.com/Ani-107)

---

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent orchestration framework
- Powered by [OpenAI](https://openai.com/) GPT models
- Inspired by modern AI support products:
  - Freshworks Freddy AI
  - HubSpot Breeze AI
  - Salesforce Einstein

---

## 📈 Roadmap

- [ ] Add REST API endpoint for integration
- [ ] Implement conversation history persistence
- [ ] Add support for multiple languages
- [ ] Create web dashboard for monitoring
- [ ] Add more specialized agents for different domains
- [ ] Implement A/B testing for agent configurations

---

<div align="center">

**Built with ❤️ using CrewAI and LangChain**

⭐ Star this repo if you find it helpful!

</div>

