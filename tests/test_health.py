from app.main import app

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"

def test_liveness():
    client = app.test_client()
    resp = client.get("/liveness")
    assert resp.status_code == 200
    assert resp.json["status"] == "I'm alive!"