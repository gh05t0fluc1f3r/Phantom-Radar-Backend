from fastapi import APIRouter, Query
from app.services.nvd import fetch_cve_details
from app.models import ThreatModel
from app.db import db_client

router = APIRouter(prefix="/threats", tags=["Threats"])

@router.post("/ingest")
def ingest_threats():
    results = fetch_cve_details()
    db_client.insert_many("threats", results)
    return {"message": f"Inserted {len(results)} records"}

@router.get("/filter")
def filter_threats(keyword: str = "", severity: str = None):
    return db_client.search("threats", keyword, severity)
