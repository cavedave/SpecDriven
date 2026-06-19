import pytest

from file_size import format_file_size


def test_zero_bytes():
    assert format_file_size(0) == "0 B"


def test_bytes_under_one_kib():
    assert format_file_size(512) == "512 B"
    assert format_file_size(1023) == "1023 B"


def test_kilobytes():
    assert format_file_size(1536) == "1.5 KB"
    assert format_file_size(1024) == "1.0 KB"


def test_megabytes():
    assert format_file_size(1_048_576) == "1.0 MB"


def test_negative_raises():
    with pytest.raises(ValueError, match="non-negative"):
        format_file_size(-1)
