from app.main import app

def test_liveness():
    client = app.test_client()
    resp = client.get("/liveness")
    assert resp.status_code == 200
    assert resp.json["status"] == "I'm alive!"