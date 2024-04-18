
from bs4 import BeautifulSoup
import requests


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url = "https://www.booking.com/hotel/us/the-lenox.html?checkin=2022-12-28&checkout=2022-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=USD"
resp = requests.get(target_url, headers=headers)
print(resp.status_code)


def scrape(url):
    l=list()
    g=list()
    o={}
    k={}
    fac=[]
    fac_arr=[]

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    o["name"]=soup.find("h2",{"class":"pp-header__title"}).text
    o["address"]=soup.find("span",{"class":"hp_address_subtitle"}).text.strip("\n")
    outer_div=soup.find("div",{"class":"a3b8729ab1 d86cee9b25"})
    contents = outer_div.contents
    o["rating"] = contents[0].strip()
    try:
        o["stars"] = len(soup.find("span",{"class":"a455730030 d542f184f1"}).contents)
    except:
        o["stars"] = 0

    fac=soup.find_all("span",{"class":"a5a5a75131"})
    for i in range(0,len(fac)):
        fac_arr.append(fac[i].text.strip("\n"))
    ids= list()
    targetId=list()
    try:
        tr = soup.find_all("tr")
    except:
        tr = None
    for y in range(0,len(tr)):
        try:
            id = tr[y].get('data-block-id')
        except:
            id = None
        if( id is not None):
            ids.append(id)
    print("ids are ",len(ids))
    for i in range(0,len(ids)):
        try:
            allData = soup.find("tr",{"data-block-id":ids[i]})
            try:
                rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
            except:
                rooms=None
            if(rooms is not None):
                last_room = rooms.text.replace("\n","")
            try:
                k["room"]=rooms.text.replace("\n","")
            except:
                k["room"]=last_room
            price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
            k["price"]=price.text.replace("\n","")
            g.append(k)
            k={}
        except:
            k["room"]=None
            k["price"]=None

    location_blocks = soup.find_all('div', class_='dc5041d860 c72df67c95 fb60b9836d')

    # Find all distance blocks
    distance_blocks = soup.find_all('div', class_='a53cbfa6de f45d8e4c32 c875b9e968')

    # Assuming each location block corresponds to a distance block in order
    locations_and_distances = []
    for location, distance in zip(location_blocks, distance_blocks):
        location_name = location.get_text().strip()
        distance_text = distance.get_text().strip()
        locations_and_distances.append((location_name, distance_text))
       

    l.append(g)
    l.append(o)
    l.append(fac_arr)
    l.append(locations_and_distances)
    return l



def scrape_hotels(city, checkin_date, checkout_date, adults = 2, children = 0, min_price = "min", max_price = "max"):
    url = f"https://www.booking.com/searchresults.html?ss={city}&lang=en-us&sb=1&src_elem=sb&src=index&checkin={checkin_date}&checkout={checkout_date}&group_adults={adults}&no_rooms=1&group_children={children}&nflt=price%3DUSD-{min_price}-{max_price}-1"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    hotels = soup.find_all('a', class_='a78ca197d0')
    hotel_links = [link['href'] for link in hotels]
    return hotel_links

def format_hotels(hotels):
    print(hotels)
    hotel_string = ""
    for h in range(len(hotels[0])):
        hotel = hotels[h]
        rooms = hotel[0]
        info = hotel[1]
        facilities = hotel[2]
        locations = hotel[3]
        hotel_string += "Hotel info: "
        for key, value in info.items():
            hotel_string += key + ": " + str(value) + ", "
        for i in range(min(len(rooms), 3)):
            room = rooms[i]
            hotel_string += "Room: " + room['room'] + ","
            hotel_string += "Price: " + room['price'] + ". "
        # for i in range(0, len(facilities)):
        #     hotel_string += facilities[i] + ", "
        # for i in range(0, len(locations)):
        #     hotel_string += locations[i][0] + " " + locations[i][1] + ", "
        hotel_string += "\n" + hotel[4] + "\n"
    return hotel_string

    
        

def find_hotels(city, checkin_date, checkout_date, adults = 2, children = 0, min_price = "min", max_price = "max", num_hotels = 5,):
    suffix = f"ss={city}&lang=en-us&sb=1&src_elem=sb&src=index&checkin={checkin_date}&checkout={checkout_date}&group_adults={adults}&no_rooms=1&group_children={children}&nflt=price%3DUSD-{min_price}-{max_price}-1"
    urls = scrape_hotels(city, checkin_date, checkout_date, adults, children, min_price, max_price)
    hotels = [scrape(urls[i]) for i in range(len(urls)) if i < num_hotels]
    for hotel, url in zip(hotels, urls):
        hotel.append(url[:url.find("?")] + "?" + suffix)
    return format_hotels(hotels)

#print(find_hotels("Tokyo", "2024-06-15", "2024-06-17", 2, 0, 600, 1000))
