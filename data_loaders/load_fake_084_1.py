import random
from pathlib import Path

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_fake_083_data(**kwargs):
    rng = random.Random('agent_dev_seed_pipeline_084:load_fake_084_1')
    rows = [
        {
            'customer_id': customer_id,
            'pipeline_uuid': 'agent_dev_seed_pipeline_084',
            'segment': rng.choice(['growth', 'core', 'enterprise']),
            'events': rng.randint(1, 25),
            'revenue': round(rng.uniform(10, 500), 2),
        }
        for customer_id in range(1, 26)
    ]
    df = pd.DataFrame(rows)
    output_dir = Path('/tmp/mage_agent_seed/agent_dev_seed_pipeline_084')
    output_dir.mkdir(parents=True, exist_ok=True)
    df.to_json(output_dir / 'load_fake_084_1.jsonl', orient='records', lines=True)
    return df


@test
def test_output(df) -> None:
    assert df is not None, 'The output is undefined'
    assert len(df.index) > 0, 'Expected seeded rows'
