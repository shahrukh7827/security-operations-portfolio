import requests

def check_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    print("IP:", ip)
    print("Country:", data.get("country"))
    print("Org:", data.get("org"))

if __name__ == "__main__":
    ip = input("Enter suspicious IP: ")
    check_ip(ip)
