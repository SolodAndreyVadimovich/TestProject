import pytest
from aggregation import apply_aggregation

TEST_DATA = [
    {"price": "100"},
    {"price": "300"},
    {"price": "600"},
]


def test_avg_aggregation():
    result = apply_aggregation(TEST_DATA, "price=avg")
    assert result["price_avg"] == 333.3333333333333


def test_min_aggregation():
    result = apply_aggregation(TEST_DATA, "price=min")
    assert result["price_min"] == 100


def test_max_aggregation():
    result = apply_aggregation(TEST_DATA, "price=max")
    assert result["price_max"] == 600


def test_invalid_column():
    with pytest.raises(ValueError):
        apply_aggregation(TEST_DATA, "unknown=avg")


def test_non_numeric_column():
    data = [{"price": "a"}, {"price": "b"}]
    with pytest.raises(ValueError):
        apply_aggregation(data, "price=avg")
