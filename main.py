import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

def fetch_views(video_url):
    resp = requests.get(video_url)
    if resp.status_code != 200:
        print(Fore.RED + "Failed to retrieve the webpage.")
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    re = soup.find("meta", itemprop="interactionCount")
    view_count = int(re["content"]) if re else None
    return view_count

def main():
    video_url = input(Fore.CYAN + "Enter the YouTube video URL: ")
    data = fetch_views(video_url)
    print(Fore.LIGHTGREEN_EX + f"> {data} views")


if __name__ == "__main__":
    main()
