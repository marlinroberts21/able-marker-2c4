# content of test_tmp_path.py
# pytest test_tmp_path.py

from pathlib import Path


CONTENT = "content"


def test_create_file(tmp_path: Path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT, encoding="utf-8")
    assert p.read_text(encoding="utf-8") == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    #assert 0