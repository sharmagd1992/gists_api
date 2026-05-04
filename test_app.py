from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_octocat_gists():
    response = client.get("/octocat")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    if len(data) > 0:
        gist = data[0]
        assert "id" in gist
        assert "url" in gist