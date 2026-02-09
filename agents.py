import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END
from typing import TypedDict

# Import the personalities
from prompts import CFO_PROMPT, UNION_LEADER_PROMPT, VISIONARY_PROMPT, CEO_PROMPT

load_dotenv()

# Setup the Brain (Llama 3.3)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.6
)

# 1. THE STATE (The Meeting Minutes)
class AgentState(TypedDict):
    topic: str
    cfo_opinion: str
    union_opinion: str
    visionary_opinion: str
    ceo_verdict: str  # <--- Added CEO Verdict

# 2. THE NODES (The Agents)

def cfo_node(state: AgentState):
    """CFO goes first. Pure analysis."""
    print("💰 CFO is speaking...")
    messages = [
        SystemMessage(content=CFO_PROMPT),
        HumanMessage(content=f"Topic: {state['topic']}")
    ]
    response = llm.invoke(messages)
    return {"cfo_opinion": response.content}

def union_node(state: AgentState):
    """Union Leader reads CFO's opinion and reacts."""
    print("🤝 Union Leader is speaking...")
    messages = [
        SystemMessage(content=UNION_LEADER_PROMPT),
        HumanMessage(content=f"""
        Topic: {state['topic']}
        
        The CFO just said: "{state['cfo_opinion']}"
        
        React to the topic, but also CRITIQUE the CFO's perspective if it hurts employees.
        """)
    ]
    response = llm.invoke(messages)
    return {"union_opinion": response.content}

def visionary_node(state: AgentState):
    """Visionary reads both and pivots to the future."""
    print("🚀 Visionary is speaking...")
    messages = [
        SystemMessage(content=VISIONARY_PROMPT),
        HumanMessage(content=f"""
        Topic: {state['topic']}
        
        CFO Concerns: "{state['cfo_opinion']}"
        Union Concerns: "{state['union_opinion']}"
        
        Ignore the petty fighting. Show us the BIG PICTURE future.
        """)
    ]
    response = llm.invoke(messages)
    return {"visionary_opinion": response.content}

def ceo_node(state: AgentState):
    """CEO makes the final call."""
    print("👑 CEO is deciding...")
    messages = [
        SystemMessage(content=CEO_PROMPT),
        HumanMessage(content=f"""
        Topic: {state['topic']}
        
        Arguments heard:
        1. CFO (Financial): {state['cfo_opinion']}
        2. Union (People): {state['union_opinion']}
        3. Visionary (Future): {state['visionary_opinion']}
        
        Issue your final verdict.
        """)
    ]
    response = llm.invoke(messages)
    return {"ceo_verdict": response.content}

# 3. THE GRAPH (The Workflow)
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("CFO", cfo_node)
workflow.add_node("Union_Leader", union_node)
workflow.add_node("Visionary", visionary_node)
workflow.add_node("CEO", ceo_node)

# Connect Edges (The Conversation Chain)
workflow.set_entry_point("CFO")
workflow.add_edge("CFO", "Union_Leader")
workflow.add_edge("Union_Leader", "Visionary")
workflow.add_edge("Visionary", "CEO")
workflow.add_edge("CEO", END)

# Compile
app = workflow.compile()