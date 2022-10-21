import json
from unittest.mock import mock_open, patch

from src.counter import count_ocurrences

WORDS = ["A Trybe é uma escola de desenvolvimento Web"]


def test_counter():
    with patch("builtins.open", mock_open(read_data=json.dumps(WORDS))):
        assert count_ocurrences("any", "trybe") == 1
