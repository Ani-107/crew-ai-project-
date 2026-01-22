import os
import warnings
warnings.filterwarnings("ignore")

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables (can also be set in .env file)
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"  # Replace with your actual API key
if not os.getenv("OPENAI_MODEL_NAME"):
    os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# ============================================================================
# AGENTS DEFINITION
# ============================================================================

# 1. Intent Detection Agent
intent_agent = Agent(
    role="Intent Detection Agent",
    goal="Identify user intent, entities, and confidence level from customer messages.",
    backstory=(
        "Specializes in classifying customer requests, extracting entities, "
        "and estimating confidence to route the request safely."
    ),
    verbose=True,
    allow_delegation=False,
)

# 2. Customer Memory Agent
memory_agent = Agent(
    role="Customer Memory Agent",
    goal="Retrieve and store relevant long-term and short-term customer context.",
    backstory=(
        "Manages persistent customer memory while avoiding memory pollution. "
        "Separates stable preferences from session-based context."
    ),
    verbose=True,
    allow_delegation=False,
)

# 3. Resolution Agent
resolution_agent = Agent(
    role="Resolution Agent",
    goal="Generate accurate, grounded responses using intent, memory, and knowledge.",
    backstory=(
        "Responsible for producing helpful, policy-compliant responses "
        "grounded in known facts and customer history."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[search_tool, scrape_tool]
)

# 4. Risk & Policy Agent
risk_agent = Agent(
    role="Risk & Policy Agent",
    goal="Assess legal, safety, and hallucination risks in proposed responses.",
    backstory=(
        "Evaluates risk exposure, detects unsafe or uncertain outputs, "
        "and recommends escalation or safeguards."
    ),
    verbose=True,
    allow_delegation=False,
)

# 5. Response Evaluation Agent
evaluation_agent = Agent(
    role="Response Evaluation Agent",
    goal="Score responses on correctness, empathy, and confidence.",
    backstory=(
        "Monitors AI quality in production and flags regressions "
        "or hallucination trends."
    ),
    verbose=True,
    allow_delegation=False,
)

# ============================================================================
# TASKS DEFINITION
# ============================================================================

# Task 1: Intent Classification
intent_task = Task(
    description="""
    Analyze the customer message:
    "{customer_message}"

    Identify:
    - Primary intent (e.g., billing_issue, technical_support, account_inquiry)
    - Key entities (e.g., subscription_id, amount, date)
    - Confidence score (0–1)
    """,
    expected_output="""
    JSON format:
    {{
      "intent": "billing_issue",
      "entities": {{"subscription_id": "12345", "issue": "double_charge"}},
      "confidence": 0.95
    }}
    """,
    agent=intent_agent,
)

# Task 2: Memory Retrieval
memory_task = Task(
    description="""
    Based on the detected intent and entities, retrieve relevant customer context.
    Separate long-term preferences from session context.
    
    Consider:
    - Previous interactions
    - Customer preferences
    - Account history
    - Current session context
    """,
    expected_output="""
    JSON format:
    {{
      "long_term_memory": ["Customer prefers email communication", "Premium subscriber since 2024"],
      "session_context": ["Current issue: billing", "First contact about this issue"]
    }}
    """,
    agent=memory_agent,
)

# Task 3: Response Generation
resolution_task = Task(
    description="""
    Generate a response using:
    - Detected intent and entities
    - Retrieved customer memory
    - Trusted knowledge sources (use tools if needed)

    Guidelines:
    - Be empathetic and professional
    - Avoid speculation
    - Cite assumptions explicitly
    - Provide actionable solutions
    - Reference customer history when relevant
    """,
    expected_output="A clear, helpful customer response that addresses their concern professionally.",
    agent=resolution_agent,
)

# Task 4: Risk Assessment
risk_task = Task(
    description="""
    Evaluate the proposed response for:
    - Hallucination risk (is the information factual?)
    - Policy violations (does it comply with company policies?)
    - Uncertainty (are there unverified claims?)
    - Legal/safety concerns

    Provide a decision: APPROVE or ESCALATE
    If ESCALATE, explain why.
    """,
    expected_output="""
    JSON format:
    {{
      "decision": "APPROVE",
      "risk_factors": ["Low hallucination risk", "Policy compliant"],
      "notes": "Response is grounded and safe to send"
    }}
    """,
    agent=risk_agent,
)

# Task 5: Evaluation & Scoring
evaluation_task = Task(
    description="""
    Score the final response on:
    - Correctness (0–10): Is the information accurate?
    - Empathy (0–10): Does it show understanding and care?
    - Confidence (0–10): Is the response clear and assured?

    Provide brief justification for each score.
    """,
    expected_output="""
    JSON format:
    {{
      "correctness": 9,
      "empathy": 8,
      "confidence": 9,
      "notes": "Response is accurate, empathetic, and provides clear next steps"
    }}
    """,
    agent=evaluation_agent,
)

# ============================================================================
# CREW ASSEMBLY
# ============================================================================

crew = Crew(
    agents=[
        intent_agent,
        memory_agent,
        resolution_agent,
        risk_agent,
        evaluation_agent
    ],
    tasks=[
        intent_task,
        memory_task,
        resolution_task,
        risk_task,
        evaluation_task
    ],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3
    ),
    verbose=True
)

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("CUSTOMER SUPPORT AI SYSTEM")
    print("=" * 80)
    print()
    
    # Example customer message
    inputs = {
        "customer_message": "I was charged twice for my subscription this month. Can you fix it?"
    }
    
    print(f"Customer Message: {inputs['customer_message']}")
    print()
    print("Processing through multi-agent system...")
    print("=" * 80)
    print()
    
    # Run the crew
    result = crew.kickoff(inputs=inputs)
    
    print()
    print("=" * 80)
    print("FINAL RESULT")
    print("=" * 80)
    print(result)
