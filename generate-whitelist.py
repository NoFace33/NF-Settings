import requests

source_url = "https://gitlab.com/andryou/andrews-settings/raw/master/rfdaffiliatedomains"
output_file = "whitelist.txt"

resp = requests.get(source_url)
domains = resp.text.strip().splitlines()

with open(output_file, "w") as f:
    f.write("! Auto-generated whitelist from rfdaffiliatedomains\n")
    for domain in domains:
        domain = domain.strip()
        if domain and not domain.startswith("!"):
            f.write(f"@@||{domain}^\n")
