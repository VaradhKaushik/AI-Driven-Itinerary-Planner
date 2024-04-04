from bs4 import BeautifulSoup
import requests

l=list()
o={}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url = "https://www.booking.com/hotel/us/the-lenox.html?checkin=2022-12-28&checkout=2022-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=USD"
resp = requests.get(target_url, headers=headers)
print(resp.status_code)

def scrape(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup