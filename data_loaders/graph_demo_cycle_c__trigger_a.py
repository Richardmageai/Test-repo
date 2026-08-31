from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_cycle_a")
    return {"relationship": "cycle_c_to_a"}
