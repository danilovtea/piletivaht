import requests

urls = [
    "https://linnateater.ee/mangukava/",
    "https://www.draamateater.ee/mangukava/"
]

found = False

for url in urls:
    r = requests.get(url)
    if "Osta pilet" in r.text:
        print(f"PILET LEITUD: {url}")
        found = True

if not found:
    print("MIDAGI EI LEITUD")
