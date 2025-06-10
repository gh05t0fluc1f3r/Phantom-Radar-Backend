from app.db.mongo import db_client
from app.utils.kev import load_kev_list

def main():
    print("🔍 Enriching threats with KEV status...")
    kev_set = load_kev_list()
    threats = db_client.get_all("threats")

    enriched_count = 0
    for threat in threats:
        cve_id = threat["cve_id"]
        is_kev = cve_id in kev_set
        if threat.get("kev") != is_kev:
            db_client.update("threats", cve_id, {"kev": is_kev})
            enriched_count += 1

    print(f"✅ Enriched {enriched_count} CVEs with KEV status.")

if __name__ == "__main__":
    main()

