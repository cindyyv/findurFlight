# findurFlight

A terminal-based flight search and information tool to help users find flights and access crucial information such as weather and news about the destination before booking.

## Project Context
This project was completed as the final project for the "Introduction to Computer and Programming" course during my freshman year.

## Motivation
Travelling often requires researching multiple sources for information about the destination. This project aims to simplify this by providing flight details, weather, and news about the destination all in one place, helping users make informed decisions before booking flights.

## Project Plan
### APIs Used
* Amadeus: For flight information.
* weather.com: For weather data.
* BeautifulSoup: For web scraping news about the destination.
### Tasks
1. Structure the Program: Set up the project structure and import necessary libraries.
2. Test APIs: Ensure APIs from Amadeus and weather.com work as expected.
3. Integrate APIs: Collect and save data from Amadeus and weather.com, and scrape news using BeautifulSoup.
4. Combine Data: Integrate all collected data into a cohesive output.
5. Finalize and Debug: Ensure the program runs smoothly and looks presentable.

## User Interaction
Users can search for flights by inputting the origin, destination, and date. The output includes flight details (e.g., price, duration) and optional detailed information about the destination's weather and news.

### Interaction Flow
Input origin and destination cities, and flight date.
View available flights with details.
Choose a flight to book.
Optionally, view detailed weather and news information about the destination.

## Timeline
### Initial Plan
* Week 1 (12/17 - 12/24): Structure program and test APIs.
* Week 2 & 3 (12/24 - 01/07): Integrate APIs and collect data.
* Week 4 (01/07 - 01/14): Combine data, debug, and finalize program.
### Updates
* Update 1: Completed Amadeus API integration and found limitations with weather.com API.
* Update 2: Switched to aerisweather API for up-to-date weather data and added airport code lookup using BeautifulSoup.

## Running the Program
### Prerequisites
* Install necessary libraries:
```
pip install BeautifulSoup4 amadeus requests
```
### Steps
1. Import required libraries (urllib, BeautifulSoup, Amadeus, requests, json, os, re).
2. Run the program and follow on-screen prompts:
   * Input origin city, destination city, and departure date.
   * Select a flight from the list.
   * Confirm flight selection.
   * Choose to view additional information (weather or news) if desired.

## Reflection
This project was challenging yet rewarding. Overcoming issues with the weather API and successfully combining multiple data sources provided a great learning experience in working with APIs and web scraping.

Thank you for checking out findurFlight! Your feedback and contributions are welcome.
