if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_qa_seed(*args, **kwargs):
    return [
        {
            'source': 'mage-qa-overwrite-protection',
            'version': 'v1',
        },
    ]
