from mage_ai.orchestration.run_status_checker import check_status


def sensor(*args, **kwargs):
    check_status("graph_demo_dense_root")
    check_status("graph_demo_dense_branch_alpha")
    return True
