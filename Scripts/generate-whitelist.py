import requests
import sys

source_url = "https://gitlab.com/andryou/andrews-settings/raw/master/rfdaffiliatedomains"
output_file = "whitelist.txt"

try:
    print(f"Fetching data from {source_url}...")
    resp = requests.get(source_url, timeout=30)
    resp.raise_for_status()  # Raise exception for non-200 status codes
    
    domains = resp.text.strip().splitlines()
    print(f"Processing {len(domains)} domains...")
    
    with open(output_file, "w") as f:
        f.write("! Auto-generated whitelist from rfdaffiliatedomains\n")
        count = 0
        for domain in domains:
            domain = domain.strip()
            if domain and not domain.startswith("!"):
                f.write(f"@@||{domain}^\n")
                count += 1
    
    print(f"Successfully wrote {count} domains to {output_file}")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}", file=sys.stderr)
    sys.exit(1)
except IOError as e:
    print(f"Error writing to file: {e}", file=sys.stderr)
    sys.exit(1)
