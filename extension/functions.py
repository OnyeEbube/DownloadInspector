import requests
import time

def check_malicious(download_link):
    # API endpoint for scanning the URL
    scan_url = 'https://www.filescan.io/api/scan/url'
    # Payload containing the URL to be scanned
    payload = {
        'url': download_link
    }
    # Headers including the API key and content type
    headers = {
        "x-apikey": API-KEY,
        "content-type": "application/x-www-form-urlencoded"
    }

    # Send a POST request to scan the URL
    response = requests.post(scan_url, data=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        flow_id = data['flow_id']
        # URL to check the scan report
        id = f"https://filescan.io/api/scan/{flow_id}/report?filter=general&filter=finalVerdict&sorting=string&other=emulationGraph"
        headers = {
            "x-apikey": API-KEY,
            "Content-Type": "application/json"
        }

        while True:
            # Send a GET request to retrieve the scan report
            response = requests.get(id, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data["allFinished"]:
                    is_malicious = False

                    for _, report in data['reports'].items():
                        print(report['finalVerdict']['verdict'])
                        if report['finalVerdict']['verdict'] == 'MALICIOUS':
                            is_malicious = True
                    return is_malicious
                if not data['allFinished']:
                    # Wait for 5 seconds before checking the report again
                    time.sleep(5)
