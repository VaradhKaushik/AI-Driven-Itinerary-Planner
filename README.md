
# AI-Driven Itinerary Planner

The AI-Driven Itinerary Planner revolutionizes the travel planning experience by integrating advanced AI technologies to generate personalized and adaptive travel itineraries. This system leverages a Large Language Model (LLM), Retrieval-Augmented Generation (RAG), and real-time web scraping, dynamically adjusting itineraries based on real-time data such as pricing and available attractions.

## Features

- **Personalized Itineraries**: Generates travel plans that are tailored to user preferences and budget, enhancing the travel experience significantly.
- **Dynamic Adaptation**: Continuously updates travel plans based on real-time changes in pricing and availability.
- **Efficiency**: Reduces the itinerary planning time by over 95%, streamlining the process to under an hour.
- **User Satisfaction**: Provides budget-conscious recommendations, significantly increasing user satisfaction.

## Technologies Used

- **LLM (Llama2-7b)**: Understands and generates language-based responses tailored to user inputs.
- **Retrieval-Augmented Generation (RAG)**: Enhances the itinerary suggestions with real-time, contextually relevant data from Chroma DB.
- **Web Scraping**: Utilizes BeautifulSoup to fetch real-time updates on travel-related information such as hotel prices and availability.

## System Architecture

This project integrates various components including a chatbot interface for interaction, a backend leveraging Llama2-7b for processing and generating itineraries, and a web scraping module to fetch the latest data required for updating the travel plans.

## Getting Started

To set up this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VaradhKaushik/travel-planner.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```

## Usage

Interact with the chatbot by specifying your travel preferences such as destination, duration, budget, and interests. The system will generate a personalized travel plan that adapts in real-time based on available data.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgements

- Northeastern University for providing the academic environment to develop this project.
- Co-contributor Alexander Seljuk for significant contributions to the web scraping module.
- All open-source software and APIs utilized in this project.

## Contact

- Varadh Kaushik - kaushik.var@northeastern.edu
- LinkedIn - https://www.linkedin.com/in/varadh-kaushik/
- Project Link: [https://github.com/VaradhKaushik/travel-planner](https://github.com/VaradhKaushik/travel-planner)

