if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def trigger_seeded_downstream(*args, **kwargs) -> None:
    from mage_ai.orchestration.db.models.schedules import PipelineSchedule
    from mage_ai.orchestration.triggers.api import trigger_pipeline

    frames = [
        arg
        for arg in args
        if hasattr(arg, 'index') and not callable(arg.index)
    ]
    source_rows = sum(len(frame.index) for frame in frames)
    try:
        trigger_pipeline(
            'agent_dev_seed_pipeline_053',
            variables={
                'seeded_by': 'agent_aws_dev_slot_seed',
                'source_pipeline_uuid': 'agent_dev_seed_pipeline_026',
                'source_rows': source_rows,
            },
            check_status=True,
            error_on_failure=True,
            poll_interval=1,
            poll_timeout=600,
            parent_pipeline_run_id=kwargs.get('pipeline_run_id'),
            parent_pipeline_uuid='agent_dev_seed_pipeline_026',
            schedule_name='Agent dev dependency - agent_dev_seed_pipeline_026 to agent_dev_seed_pipeline_053',
            verbose=False,
            _should_schedule=True,
        )
    finally:
        dependency_schedules = PipelineSchedule.repo_query.filter(
            PipelineSchedule.name == 'Agent dev dependency - agent_dev_seed_pipeline_026 to agent_dev_seed_pipeline_053',
            PipelineSchedule.pipeline_uuid == 'agent_dev_seed_pipeline_053',
        ).all()
        for dependency_schedule in dependency_schedules:
            dependency_schedule.update(status='inactive')
