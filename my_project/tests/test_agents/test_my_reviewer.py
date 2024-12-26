import pytest
from metagpt_extension.my_reviewer import MyReviewer

@pytest.mark.asyncio
async def test_my_reviewer_review_code(test_config_path):
    rev = MyReviewer(config_path=test_config_path)
    code_snips = {"content": "some code snippet"}
    result = await rev.review_code(code_snips)
    assert "content" in result or "ok" in result
