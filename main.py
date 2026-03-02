import sys
import requests
from offorte_client import OfforteAutomation

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <proposal_id> <page_id> <callback_url>")
        sys.exit(1)

    proposal_id = sys.argv[1]
    page_id = sys.argv[2]
    callback_url = sys.argv[3]

    try:
        print("🚀 Starting automation...")
        automation = OfforteAutomation(proposal_id, page_id)
        proposal_data = automation.run()

        print("📤 Sending data to Zapier webhook...")
        response = requests.post(callback_url, json=proposal_data, timeout=60)

        print(f"✅ Webhook response: {response.status_code}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()