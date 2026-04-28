from typing import TypedDict, List, Dict, Any, Literal
from langgraph.graph import StateGraph, END
from tools import extractor, validator, clarifier, EXPECTED_FIELDS

class State(TypedDict):
    raw_text: str
    extracted: Dict[str, Any]
    missing_fields: List[str]
    iterations: int
    max_iterations: int
    final_output: Dict[str, Any] | None

def extractor_node(state):
    print("→ Extractor node")
    return {**state, "extracted": extractor(state["raw_text"])}

def validator_node(state):
    print("→ Validator node")
    missing = validator(state["extracted"])
    return {**state, "missing_fields": missing}

def clarifier_node(state):
    print(f"→ Clarifier node (missing: {state['missing_fields']})")
    new_data = clarifier(state["raw_text"], state["missing_fields"])
    merged = state["extracted"].copy()
    merged.update(new_data)
    return {**state, "extracted": merged, "iterations": state["iterations"] + 1}

def formatter_node(state):
    final = {field: state["extracted"].get(field) for field in EXPECTED_FIELDS}
    return {**state, "final_output": final}

def router(state):
    if state["missing_fields"] and state["iterations"] < state["max_iterations"]:
        return "clarifier"
    return "formatter"

def build_graph():
    workflow = StateGraph(State)
    workflow.add_node("extractor", extractor_node)
    workflow.add_node("validator", validator_node)
    workflow.add_node("clarifier", clarifier_node)
    workflow.add_node("formatter", formatter_node)
    workflow.set_entry_point("extractor")
    workflow.add_edge("extractor", "validator")
    workflow.add_conditional_edges("validator", router, {
        "clarifier": "clarifier",
        "formatter": "formatter"
    })
    workflow.add_edge("clarifier", "validator")
    workflow.add_edge("formatter", END)
    return workflow.compile()