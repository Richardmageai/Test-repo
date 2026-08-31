from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_cycle_c")
    return {"relationship": "cycle_b_to_c"}
