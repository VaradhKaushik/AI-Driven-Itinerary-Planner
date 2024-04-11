import re
import hscraper

class DataExtractor:

    def __init__(self):
        pass
    def extract(self, request):
        # city_index = request.find('city:')
        # from_index = request.find('from:')
        # to_index = request.find('to:')
        # max_price_index = request.find('max price:')
        # people_index = request.find('people:')
        pattern = r"(\w+):([^,]+)"

        # Find all matches
        matches = re.findall(pattern, request)

        # Convert matches to dictionary
        params = dict(matches)

        return params
    
    def findHotels(self, params):
        return hscraper.scrape_hotels(params['city'], params['from'], params['to'], params['people'], 0, "min", params['max_price'])
    
    def extractHotelDetails(self, num_hotels, hotel_url):
        hotels = []
        for i in range(num_hotels):
            print(hotel_url[i])
            hotels.append(hscraper.scrape(hotel_url[i]))
        print(hotels)
        return hotels

de = DataExtractor()

        
def langchain_hotels_wrapper(request):
    params = de.extract(request)

    hotels = de.findHotels(params)
    
    # Call your hotel availability function
    available_hotels = de.extractHotelDetails(10, hotels)
    hotel_data = []
    for hotel in available_hotels:
        hotel_data.append(hotel[1])
    # Format the output for the user
    return {
        "response": "Available hotels: " + ", ".join([f"{hotel['name']} (Price: {hotel['address']}, Rating: {hotel['rating']})" for hotel in hotel_data])
    }   

print(langchain_hotels_wrapper("city:Chicago, from:2024-06-15, to:2024-06-29, people:2, max_price:2000"))
