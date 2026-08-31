from typing import Callable

from mage_ai.streaming.sources.base_python import BasePythonSource

if 'streaming_source' not in globals():
    from mage_ai.data_preparation.decorators import streaming_source


@streaming_source
class AgentDevSeedCustomSource(BasePythonSource):
    def init_client(self):
        return None

    def batch_read(self, handler: Callable) -> None:
        handler([
            {'event_id': 1, 'event_name': 'seeded_started'},
            {'event_id': 2, 'event_name': 'seeded_completed'},
        ])
