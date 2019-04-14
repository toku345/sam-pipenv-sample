import json

from proverb.app import lambda_handler


def test_lambda_handler():
    ret = lambda_handler({}, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
