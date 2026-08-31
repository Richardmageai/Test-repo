import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform_seeded_077(*args, **kwargs):
    frames = [arg for arg in args if hasattr(arg, 'copy')]
    df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    if df.empty:
        return pd.DataFrame([{'pipeline_uuid': 'agent_dev_seed_pipeline_078', 'events': 0}])
    df = df.copy()
    df['weighted_events'] = df['events'] * (2 + 1)
    df['block_uuid'] = 'transform_metrics_078'
    return df
