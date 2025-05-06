from fastapi import FastAPI

app = FastAPI(
    title="Constituency Intelligence Service",
    version="0.1.0"
)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/district/{district_id}/profile")
def get_district_profile(district_id: str):
    return {"district": district_id, "profile": "stub"}

@app.get("/district/{district_id}/issues")
def get_district_issues(district_id: str):
    return {"district": district_id, "issues": ["stubbed-issue-1", "stubbed-issue-2"]}
