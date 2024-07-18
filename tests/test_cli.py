import os

from wcpy.cli import get_file_stats

test_dir = os.path.dirname(__file__)
test_txt_file_1 = os.path.join(test_dir, "file_1.txt")
test_txt_file_2 = os.path.join(test_dir, "file_2.txt")


def test_get_file_stats():
    stats = get_file_stats(test_txt_file_1)

    assert stats["lines"] == 3
    assert stats["words"] == 69
    assert stats["chars"] == 448
    assert stats["bytes"] == 448
    assert stats["max_line_length"] == 445
    assert stats["file_name"] == test_txt_file_1
