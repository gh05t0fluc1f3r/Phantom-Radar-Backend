import requests

def fetch_cve_details():
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {"resultsPerPage": 10}
    headers = {"apiKey": "YOUR_API_KEY_HERE"}

    response = requests.get(url, headers=headers, params=params)
    results = []
    if response.status_code == 200:
        for item in response.json().get("vulnerabilities", []):
            cve = item.get("cve")
            results.append({
                "cve_id": cve.get("id"),
                "description": cve.get("descriptions")[0].get("value"),
                "published": cve.get("published"),
                "modified": cve.get("lastModified"),
                "cvss_score": cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseScore"),
                "cvss_severity": cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseSeverity"),
                "cpe": cve.get("configurations", {}).get("nodes", [{}])[0].get("cpeMatch", []),
                "cwe": cve.get("weaknesses", [{}])[0].get("description", [{}])[0].get("value"),
                "source": "nvd",
                "kev": cve.get("isKev") or False
            })
    return results
