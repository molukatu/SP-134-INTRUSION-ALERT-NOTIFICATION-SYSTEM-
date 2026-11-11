from fastapi import FastAPI

app = FastAPI(title="SP-134 Intrusion Alert System")

@app.get("/")
def home():
    return {"message": "SP-134 is running", "status": "ok"}

@app.get("/api/health")
def health():
    return {"status": "healthy", "service": "SP-134"}

# Temporary in-memory alerts for Week 3 demo
fake_alerts = [
    {"id": 1, "type": "Port Scan", "severity": "High", "src_ip": "192.168.1.50", "status": "New"},
    {"id": 2, "type": "Brute Force", "severity": "Critical", "src_ip": "10.0.0.23", "status": "New"},
]

@app.get("/api/alerts")
def get_alerts():
    return {"count": len(fake_alerts), "alerts": fake_alerts}

@app.get("/api/dashboard/summary")
def summary():
    return {
        "total_alerts_today": len(fake_alerts),
        "critical": 1,
        "high": 1,
        "top_attacker_ips": ["10.0.0.23", "192.168.1.50"]
    }
