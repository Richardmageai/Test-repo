from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_dense_branch_alpha")
    trigger_pipeline("graph_demo_dense_branch_beta")
    trigger_pipeline("graph_demo_dense_branch_gamma")
    return {"relationship": "dense_root"}
