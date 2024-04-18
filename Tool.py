from langchain_core.tools import tool
import hscraper
from langchain.chains import BaseTool


@tool
def scrape(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


class MyCustomTool(BaseTool):
    def call(self, input_text):
        # Code to interact with your tool
        
        response = hscraper.find_hotels(input_text)
        return response