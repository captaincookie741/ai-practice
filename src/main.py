import os
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="mistralai/devstral-2512:free",
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
)

def chatbot_node(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

builder = StateGraph(MessagesState)
builder.add_node("chatbot", chatbot_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)
graph = builder.compile()

if __name__ == "__main__":
    state = {"messages": [HumanMessage(content="用一句话解释下什么是 LangGraph？")]}
    result = graph.invoke(state)
    print("AI:", result["messages"][-1].content)