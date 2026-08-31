from mage_ai.orchestration.triggers.api import trigger_workspace_pipeline


def load_data(*args, **kwargs):
    trigger_workspace_pipeline("graph_demo_workspace_trigger_target")
    return {"relationship": "trigger_workspace_pipeline"}
