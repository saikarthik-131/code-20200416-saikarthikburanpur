import pytest

from main import caluclateBMI


def test_method():
    assert caluclateBMI({"Gender": "Male", "HeightCm": 171, "WeightKg": 96}) == 32.8