from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# 1. SETUP LLM
llm = ChatGroq(
    temperature=0.5, 
    model_name="llama-3.3-70b-versatile", 
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 2. DEFINING THE AGENTS (The "Human-Friendly" Version)

# CFO: Smart with money, but speaks clearly
cfo_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are The CFO (Chief Financial Officer). "
               "Your job is to analyze the financial risks, costs, and profit potential. "
               "CRITICAL INSTRUCTION: Speak in plain, clear English. Avoid complex corporate jargon. "
               "Don't use words like 'fiscal prudence' or 'synergies'. Instead use 'saving money' or 'working together'. "
               "Be direct, skeptical, and focused on the bottom line."),
    ("human", "Topic: {topic}")
])

# Union Leader: Protects people, simple and emotional language
union_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are The Union Leader. "
               "Your job is to protect the employees, their jobs, and their well-being. "
               "CRITICAL INSTRUCTION: Speak with passion but use simple, everyday language. "
               "Focus on people, not numbers. If the plan hurts workers, fight it. "
               "Make your argument personal and relatable."),
    ("human", "Topic: {topic}")
])

# Visionary: Future ideas, but grounded in reality
visionary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are The Visionary (Chief Strategy Officer). "
               "Your job is to look 5 years into the future. "
               "CRITICAL INSTRUCTION: Don't use buzzwords like 'paradigm shift' or 'disruptive innovation'. "
               "Explain your big ideas simply. Give concrete examples of how this changes the game. "
               "Be optimistic and creative."),
    ("human", "Topic: {topic}")
])

# CEO: The Decision Maker (Clear, Decisive, No Fluff)
ceo_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are The CEO. "
               "Your job is to make a final binding decision based on your team's advice. "
               "CRITICAL INSTRUCTION: "
               "1. Start with a clear 'YES', 'NO', or 'MODIFY' verdict. "
               "2. Speak in simple, authoritative English. Explain your decision so a 12-year-old could understand it. "
               "3. Give 3 clear, actionable next steps. "
               "4. Do not waffle. Be decisive."),
    ("human", "Topic: {topic}\n\nCFO Opinion: {cfo}\nUnion Opinion: {union}\nVisionary Opinion: {visionary}")
])

# 3. CREATING THE CHAINS
cfo_chain = cfo_prompt | llm | StrOutputParser()
union_chain = union_prompt | llm | StrOutputParser()
visionary_chain = visionary_prompt | llm | StrOutputParser()
ceo_chain = ceo_prompt | llm | StrOutputParser()

# 4. THE LANGGRAPH WORKFLOW
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    topic: str
    cfo_opinion: str
    union_opinion: str
    visionary_opinion: str
    ceo_verdict: str

def run_cfo(state):
    return {"cfo_opinion": cfo_chain.invoke({"topic": state["topic"]})}

def run_union(state):
    return {"union_opinion": union_chain.invoke({"topic": state["topic"]})}

def run_visionary(state):
    return {"visionary_opinion": visionary_chain.invoke({"topic": state["topic"]})}

def run_ceo(state):
    return {"ceo_verdict": ceo_chain.invoke({
        "topic": state["topic"],
        "cfo": state["cfo_opinion"],
        "union": state["union_opinion"],
        "visionary": state["visionary_opinion"]
    })}

# Build Graph
workflow = StateGraph(State)
workflow.add_node("cfo", run_cfo)
workflow.add_node("union", run_union)
workflow.add_node("visionary", run_visionary)
workflow.add_node("ceo", run_ceo)

workflow.set_entry_point("cfo")
workflow.add_edge("cfo", "union")
workflow.add_edge("union", "visionary")
workflow.add_edge("visionary", "ceo")
workflow.add_edge("ceo", END)

app = workflow.compile()