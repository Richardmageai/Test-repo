if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_qa_seed(data, *args, **kwargs):
    return data
