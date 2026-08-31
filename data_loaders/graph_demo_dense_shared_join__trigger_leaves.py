from mage_ai.orchestration.triggers.api import trigger_pipeline


def load_data(*args, **kwargs):
    trigger_pipeline("graph_demo_dense_leaf_north")
    trigger_pipeline("graph_demo_dense_leaf_south")
    trigger_pipeline("graph_demo_dense_finalizer")
    return {"relationship": "dense_join"}
