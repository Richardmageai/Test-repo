from mage_ai.orchestration.run_status_checker import check_status


def sensor(*args, **kwargs):
    check_status("graph_demo_fan_in_a")
    check_status("graph_demo_fan_in_b")
    return True
