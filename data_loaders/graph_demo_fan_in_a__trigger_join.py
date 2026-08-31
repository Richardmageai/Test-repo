from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_fan_in_join")
    return {"relationship": "trigger_pipeline"}
