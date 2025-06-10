from app.services.nvd import fetch_cve_details
from app.db.mongo import db_client

def main():
    print("🔄 Fetching CVEs from NVD...")
    cves = fetch_cve_details()
    existing_ids = db_client.get_existing_ids("threats")

    new_data = [cve for cve in cves if cve['cve_id'] not in existing_ids]

    if new_data:
        db_client.insert_many("threats", new_data)
        print(f"✅ Inserted {len(new_data)} new CVEs.")
    else:
        print("✅ No new CVEs to insert.")

if __name__ == "__main__":
    main()

