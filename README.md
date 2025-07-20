Multithreaded Subdomain Scanner

This Python script performs a fast subdomain enumeration on a target domain using a wordlist. It attempts to connect to each potential subdomain using both HTTP and HTTPS protocols and logs the ones that are reachable.

---

Features

- Scans for active subdomains of any target domain
- Uses both `http://` and `https://` schemes for better coverage
- Multithreaded for high-speed scanning
- Outputs results to `discovered_subdomains.txt`
- Interactive prompt to view results

---

Requirements

Install required Python packages:

```bash
pip install requests
