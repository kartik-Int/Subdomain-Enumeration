import threading
import requests

domain ="youtube.com"  #change domain as per your need

discivered_subdomains=[]
with open("test_subdomains.txt") as f:
    hunululu = f.read().splitlines()
lock = threading.Lock()

def check_subdomain(subdomain):
    for proto in ['http','https']:
        url = f'{proto}://{subdomain}.{domain}'
        try:
            response = requests.get(url)
            print(f"Subdomain found for {url}: {response.status_code}")
            with lock:
                discivered_subdomains.append(subdomain)

            

        except requests.ConnectionError:
            pass


threads = []

for sub in hunululu:
    t = threading.Thread(target=check_subdomain, args=(sub,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discivered_subdomains:
        print(subdomain, file=f)  

print("\nResults saved to discovered_subdomains.txt\n")

choice = input("If you want to see discovered_subdomain, press 1 , otherwise press any key to exit\n")
if choice=='1':
    print("\nContents of discovered_subdomains.txt:")
    with open("discovered_subdomains.txt", 'r') as f:
        print(f.read())




