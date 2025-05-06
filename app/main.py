from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import aiofiles
import json
import os

app = FastAPI(
    title="Constituency Intelligence Service",
    version="0.1.0"
)

# Path to static demo data
STATIC_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "static-data")


@app.get("/healthz")
def health_check():
    return {"status": "ok"}


@app.get("/district/{district_id}/profile")
async def get_district_profile(district_id: str):
    file_path = os.path.join(STATIC_DATA_DIR, f"{district_id.lower()}.json")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="District profile not found")

    async with aiofiles.open(file_path, mode="r") as f:
        contents = await f.read()
        try:
            data = json.loads(contents)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Malformed district data")

    return JSONResponse(content=data)


@app.get("/district/{district_id}/issues")
async def get_district_issues(district_id: str):
    # Placeholder — expand this once you link in real issue parsing
    return {
        "district": district_id,
        "issues": ["housing", "public transit", "opioids"]
    }
