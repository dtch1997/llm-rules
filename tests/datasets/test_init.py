import pytest

from llm_rules.datasets import list_datasets, build_dataset

@pytest.mark.parametrize("dataset_id", list_datasets())
def test_build_dataset(dataset_id):
    # NOTE: n_samples must be even
    dataset = build_dataset(dataset_id, n_samples=2)
    assert len(dataset.data) == 2
    assert len(dataset.data[0].text) > 0
    assert dataset.data[0].label in [0, 1]
    assert len(dataset.rule) > 0