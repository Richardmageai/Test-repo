from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_fan_out_a")
    trigger_pipeline("graph_demo_fan_out_b")
    return {"relationship": "fan_out"}
