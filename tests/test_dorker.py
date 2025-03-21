import pytest
from src.dorker import perform_dorking

def test_perform_dorking():
    query = "inurl:.php?id= site:*.go.id"
    urls = perform_dorking(query, num_results=2)
    assert isinstance(urls, list)
    assert len(urls) <= 2