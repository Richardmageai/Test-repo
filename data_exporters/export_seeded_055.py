from pathlib import Path

import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_seeded_054(*args, **kwargs) -> None:
    frames = [arg for arg in args if hasattr(arg, 'copy')]
    df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    output_dir = Path('/tmp/mage_agent_seed/agent_dev_seed_pipeline_055')
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'export_seeded_055.parquet'
    try:
        df.to_parquet(output_path)
    except Exception:
        df.to_csv(output_path.with_suffix('.csv'), index=False)
