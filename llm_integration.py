import re
import hscraper

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.llms import huggingface_pipeline
import os
from langchain_community.llms import HuggingFaceEndpoint


# Note that the docstrings here are crucial, as they will be passed along
# to the model along with the class name.
class HotelTool(BaseModel):
    """Finds live hotel availability and prices for a given location and dates. Also filters them by price and number of guests."""

    city: int = Field(..., description="City to search for the hotels")
    from_date: int = Field(..., description="Date of the first day of stay, yyyy-mm-dd format")
    to_date: int = Field(..., description="Last date of stay, yyyy-mm-dd format")
    people: int = Field(..., description="Number of people")
    min_price: int = Field(..., description="Minimum budget for the stay in us dollars, min if not specified")
    max_price: int = Field(..., description="Maximum price for the stay in us dollars, max if not specified")

    def call(self):
        """Call the hotel scraping tool to find hotels with the given parameters."""
        hotels = self.scrape_hotels(self.city, self.from_date, self.to_date, self.people, max_price=self.max_price)
        return hotels



class DataExtractor:

    def __init__(self):
        pass
    def extract(self, request):
        # city_index = request.find('city:')
        # from_index = request.find('from:')
        # to_index = request.find('to:')
        # max_price_index = request.find('max price:')
        # people_index = request.find('people:')
        pattern = r"(\w+):[ ]{1}([^,]+)"

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
        "response": "Available hotels: " + ", ".join([f"{hotel['name']} (address: {hotel['address']}, Rating: {hotel['rating']}, Stars: {hotel['stars']})" for hotel in hotel_data])
    }   


#print(langchain_hotels_wrapper("city:Los Angeles, from:2024-06-15, to:2024-06-29, people:2, max_price:2000"))
