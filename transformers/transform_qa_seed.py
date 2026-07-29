if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform_qa_seed(data, *args, **kwargs):
    return [
        {
            **row,
            'status': 'ready-for-overwrite-protection-qa',
        }
        for row in data
    ]
