---
title: The Council Agent
emoji: ⚡
colorFrom: red
colorTo: gray
sdk: docker
pinned: false
license: mit
short_description: Multi agent environment.
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


🏛️ THE COUNCIL: User Manual & Technical Documentation
Version: 1.0 (Beta) | Architect: Rohit's AI Studio
1. Introduction
The Council is an advanced AI-Powered Strategy Simulator designed to help leaders, managers, and researchers make better decisions. Unlike standard chatbots that give a single generic answer, The Council simulates a Board of Directors meeting where distinct AI personalities debate your problem from different angles (Financial, Human, and Strategic) before a "CEO" delivers a binding verdict.
2. How to Use the App
Step 1: Enter Your Dilemma
Open the application in your browser.
In the text box, type a strategic question or management problem.
Examples:
"Should we implement a 4-day work week?"
"Should we replace 50% of junior staff with AI?"
"Should we switch to 100% remote work?"
Step 2: Convene The Council
Click the "⚡ CONVENE THE COUNCIL" button.
The system will process your request (approx. 10-20 seconds) as the agents deliberate.
Step 3: Analyze the Debate
Three distinct cards will appear, representing the different perspectives:
💰 The CFO (Green Card): Focuses on ROI, budget, risks, and financial sustainability.
🤝 The Union Leader (Red Card): Focuses on employee well-being, ethics, morale, and jobs.
🚀 The Visionary (Purple Card): Focuses on long-term growth, innovation, and future trends.
Step 4: The Verdict
Scroll to the bottom to see 👑 The CEO's Verdict (Gold Card).
This is the final, binding resolution that synthesizes all arguments into a clear "Go" or "No-Go" decision with next steps.
Step 5: Export Report
Click "📥 Download Official Report (PDF)" to generate a professional document containing the entire debate and verdict, ready for email or presentation.
3. Under the Hood: The "Brain" Logic 🧠
The intelligence of The Council is powered by a Sequential Multi-Agent System. It does not use a random conversation; it follows a strict LangGraph Workflow to ensure logical coherence.
The Agent Workflow (The Chain of Thought)
Input: The user provides a Topic.
Node 1: The CFO:
Analyzes the Topic strictly for financial implications.
Output: A cost-benefit analysis.
Node 2: The Union Leader:
Listens to the CFO. (This is key: The Union Leader is aware of the cost-cutting arguments).
Reacts: Defends the human element and critiques the CFO's numbers if they hurt people.
Node 3: The Visionary:
Listens to both the CFO and Union Leader.
Synthesis: Ignores the petty squabbles and proposes a futuristic "Third Way."
Node 4: The CEO (The Judge):
Reviews all three opinions.
Verdict: Issues a final decision that balances money, people, and future growth.
How Agents "Talk" (Prompt Engineering)
Each agent is powered by a specific System Prompt that defines their personality:
CFO Prompt: "You are a conservative CFO. You care about profit, risk, and saving money. Be skeptical."
Union Prompt: "You are a passionate Union Leader. You care about jobs, fair pay, and work-life balance. Fight for the employees."
CEO Prompt: "You are the decisive CEO. Listen to your team, but make the hard call. Be authoritative."
4. Technology Stack 🛠️
This application was built using state-of-the-art Open Source AI technologies.
Component
Technology Used
Purpose
The Brain (LLM)
Llama 3 70B (via Groq)
The intelligence model. We use the 70B parameter model for high-level reasoning.
Speed Layer
Groq API
Provides near-instant inference speed (LPU), making the debate feel real-time.
Orchestration
LangGraph
Manages the "State" and passes messages between agents (CFO->Union->CEO).
Framework
LangChain
Connects the Python code to the LLM API.
Frontend
Streamlit
The user interface (UI), responsible for the dark mode, cards, and animations.
Reporting
FPDF
Generates the downloadable PDF reports on the fly.
Deployment
Docker & Hugging Face
Containers used to host the app securely in the cloud.

5. Deployment Guide (For Developers)
To run this application locally or deploy it:
Clone the Repository:
Bash
git clone https://huggingface.co/spaces/rohgoswa/the-council


Install Dependencies:
Bash
pip install -r requirements.txt


Set API Key:
Get a free API Key from Groq Cloud.
Create a .env file: GROQ_API_KEY=gsk_...
Run the App:
Bash
streamlit run app.py


© 2026 Rohit's AI Studio. All Rights Reserved.Building the future of Management Technology.