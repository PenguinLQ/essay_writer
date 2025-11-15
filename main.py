from pydantic import BaseModel, ValidationError
from typing import List, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

_ = load_dotenv()
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model_name = os.getenv("MODEL_NAME")

class Model(BaseModel):
    x: str

class AgentState(TypedDict):
    task: str
    plan: str
    content: List[str]

def main():
    test_agent_state()


def test_agent_state():
    state: AgentState = {}
    state['task'] = "1"
    state['plan'] = "2"
    # print(state)
    content = state.get('content', [])
    print(content)


class Queries(BaseModel):
    queries: List[str]

def test_output():
    model = ChatOpenAI (
        base_url = base_url,
        api_key = api_key,
        model = model_name,
        temperature = 0
    )

    task = "what is the difference between langchain and langsmith"

    RESEARCH_PLAN_PROMPT = """You are a researcher charged with providing information that can \
be used when writing the following essay. Generate a list of search queries that will gather \
any relevant information. Only generate 3 queries max.

Format the output as JSON with the following keys:
queries
    """
    queries = model.with_structured_output(Queries).invoke([
        SystemMessage(content=RESEARCH_PLAN_PROMPT),
        HumanMessage(content=task)
    ])

    for q in queries.queries:
        print(q)

    # response = model.invoke([
    #     SystemMessage(content=RESEARCH_PLAN_PROMPT),
    #     HumanMessage(content=task)
    # ])

    # print(response.content)


def validate():
    try:
        Model()
    except ValidationError as exc:
        # print(repr(exc.errors()[0]['type']))
        print(exc)

def test_string():
    model_name = "qwen3:max"

    res: str = "Hello from essay-writer!"
    if (model_name.startswith("qwen")):
        res += "\nQwen"

    print(res)

if __name__ == "__main__":
    main()
