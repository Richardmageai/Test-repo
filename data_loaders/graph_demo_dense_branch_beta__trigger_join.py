from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_dense_shared_join")
    return {"relationship": "beta_to_join"}
