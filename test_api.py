from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_endpoints():
    print("[API TEST] Testing Web UI HTML Pages...")
    for path in ["/", "/scanner", "/register", "/students", "/attendance", "/settings"]:
        res = client.get(path)
        print(f"GET {path:15} -> Status: {res.status_code}")
        assert res.status_code == 200, f"Failed GET {path}"

    print("\n[API TEST] Testing REST API Endpoints...")
    res = client.get("/api/system/status")
    print(f"GET /api/system/status -> Status: {res.status_code}, data: {res.json()['ai_engine']}")
    assert res.status_code == 200

    res = client.get("/api/students")
    print(f"GET /api/students       -> Status: {res.status_code}, count: {res.json()['count']}")
    assert res.status_code == 200

    res = client.get("/api/attendance/stats")
    print(f"GET /api/attendance/stats -> Status: {res.status_code}, rate: {res.json()['stats']['attendance_rate']}%")
    assert res.status_code == 200

    res = client.get("/api/attendance/history")
    print(f"GET /api/attendance/history -> Status: {res.status_code}, count: {res.json()['count']}")
    assert res.status_code == 200

    res = client.get("/api/export/csv")
    print(f"GET /api/export/csv    -> Status: {res.status_code}, bytes: {len(res.content)}")
    assert res.status_code == 200

    res = client.get("/api/export/excel")
    print(f"GET /api/export/excel  -> Status: {res.status_code}, bytes: {len(res.content)}")
    assert res.status_code == 200

    print("\nALL API ENDPOINTS TESTED AND VERIFIED! [OK]")

if __name__ == "__main__":
    test_endpoints()
