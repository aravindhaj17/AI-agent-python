from pydantic import ValidationError
from models import ResearchResponse


def test_research_response_valid():
    data = {
        "topic": "Binary Search",
        "summary": "Binary search is an efficient algorithm.",
        "sources": ["Wikipedia"],
        "tools_used": ["wiki_tool"]
    }

    response = ResearchResponse(**data)

    assert response.topic == "Binary Search"
    assert isinstance(response.sources, list)


def test_research_response_invalid():
    data = {
        "topic": "Binary Search",
        # summary missing
        "sources": ["Wikipedia"],
        "tools_used": ["wiki_tool"]
    }

    try:
        ResearchResponse(**data)
        assert False  # should not reach here
    except ValidationError:
        assert True
