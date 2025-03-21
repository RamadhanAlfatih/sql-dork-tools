import pytest
from src.sqlmapper import run_sqlmap

def test_run_sqlmap():
    url = "https://example.com/page.php?id=1"
    # This is a mock test; actual sqlmap testing requires a valid URL
    assert run_sqlmap(url) is None