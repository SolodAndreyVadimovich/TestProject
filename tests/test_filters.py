import pytest
from filters import apply_filter

TEST_DATA = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
]


def test_filter_price_greater_than():
    result = apply_filter(TEST_DATA, "price>500")
    assert len(result) == 2
    assert all(int(r["price"]) > 500 for r in result)


def test_filter_rating_equals():
    result = apply_filter(TEST_DATA, "rating=4.6")
    assert len(result) == 1
    assert result[0]["name"] == "redmi note 12"


def test_filter_brand_equals_text():
    result = apply_filter(TEST_DATA, "brand=apple")
    assert len(result) == 1
    assert result[0]["name"] == "iphone 15 pro"


def test_filter_less_than():
    result = apply_filter(TEST_DATA, "price<500")
    assert len(result) == 1
    assert result[0]["name"] == "redmi note 12"
