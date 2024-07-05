import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from amadeus import Client, ResponseError
import requests
import json
import os
import re

#BeautifulSoup:::Airport Codes
url_soup = "https://www.ccra.com/airport-codes/"
x = urllib.request.urlopen(url_soup).read()
soup = BeautifulSoup(x, 'html.parser')

counta = 0
a = []
b = []
c = []

for city in soup.find_all('td', class_="column-1"):
  a.append(city.text.split(",")[0])
  counta += 1
for country in soup.find_all('td', class_="column-2"):
  b.append(country.text)
for code in soup.find_all('td', class_="column-3"):
  c.append(code.text[:3])

#API-1:::Amadeus
amadeus = Client(
    client_id='OyUpebALji08rrNc0woDXTv5bqmhKJTI',
    client_secret='RFXWYoWPbOnmEeGR'
)

#API-2:::Aeris Weather
headers = {
  'x-rapidapi-key': "a5b4106189mshaf20e4233ec98aap179b4ajsnae89c5080a3c",
  'x-rapidapi-host': "aerisweather1.p.rapidapi.com"
}

#function of using API-2:::Aeris Weather
def weather():
  print()
  for n in range (counta):
    try:
      if dcity == a[n]:
        loc = dcity+','+b[n]
    except NameError:
      print("Error.")

  url_api2 = "https://aerisweather1.p.rapidapi.com/forecasts/%s" %(loc)

  response = requests.request("GET", url_api2, headers=headers)
  response_dict = json.loads(response.text)

  info = response_dict['response']
  detailed = info[0]['periods']

  datee =[]
  weather = []
  avgtemp = []
  maxtemp = []
  mintemp = []
  sunrise = []
  sunset= []

  print(dcity, "'s weather: ")
  for n in range(len(detailed)):
    datee.append(detailed[n]['validTime'][0:10])
    weather.append(detailed[n]['weather']) 
    avgtemp.append(detailed[n]['avgTempC'])
    maxtemp.append(detailed[n]['maxTempC'])
    mintemp.append(detailed[n]['minTempC'])
    sunrise.append(detailed[n]['sunriseISO'][11:19])
    sunset.append(detailed[n]['sunsetISO'][11:19])
    if ddate == datee[n]:
      print("Date                   : ", datee[n])
      print("Weather                : ", weather[n])
      print("Average Temperature    : ", avgtemp[n], "°C")
      print("Maximum Temperature    : ", maxtemp[n], "°C")
      print("Minimum Temperature    : ", mintemp[n], "°C")
      print("Sunrise at             : ", sunrise[n])
      print("Sunset at              : ", sunset[n])
      print()

#function of using BeautifulSoup:::News
def news():
  url = "https://cities-today.com/?s=%s" %(dcity)
  x = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(x, 'html.parser')

  count = 0
  for news in soup.find_all('h2', class_="entry-title"):
    count += 1
    print()
    print(str(count) + '.')
    print(news.a.text)
    print("Link: ", news.a["href"])

#################FIRST INPUT:::Airport Code
print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒findurFlight⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")
while 1:
  ocity = input("Please enter your origin city      : ")
  dcity = input("Please enter your destination city : ")
  
  if ocity not in a or dcity not in a:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒findurFlight⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒⭒")
  if ocity not in a:
    print("Sorry. We don't have the city data for",ocity+".")
  if dcity not in a:
    print("Sorry. We don't have the city data for",dcity+".") 
  if ocity not in a or dcity not in a:
    continue

  #################FIRST OUTPUT
  print()
  print("This is the code for your origin airport:")
  for n in range (counta):
    if ocity == a[n]:
      print("❋", c[n])
  print()
  print("This is the code for your destination airport:")
  for n in range (counta):
    if dcity == a[n]:
      print("❋", c[n])

  break

#################SECOND INPUT:::Airport Code - Amadeus
print()
origin = input("Origin Airport Code       : ")
destin = input("Destination Airport Code  : ")
while True:
  ddate = input("Departure Date(YYYY-MM-DD): ")
  day = re.search("(2021-.+-.+)", ddate)
  if not day:
    print("Please enter a new date.")
  elif day:
    break
try:
  response = amadeus.shopping.flight_offers_search.get(
      originLocationCode=origin,
      destinationLocationCode=destin,
      departureDate=ddate,
      adults='1')
  curr = 34.3
  total = response.data
  for x in total:
    number = x['id']
    price = x['price']
    duration = x['itineraries'][0]['duration']
    segment = x['itineraries'][0]['segments'][0]
    deptime = segment['departure']['at']
    arrtime = segment['arrival']['at']
    twd = float(price['total']) * curr
    #################SECOND OUTPUT
    print(number +'.')
    print("Departure time   : ", deptime[len(ddate)+1:-3])
    print("Arrival time     : ", arrtime[len(ddate)+1:-3])
    print("Duration         : ", duration[2:])
    print("Price            : ", 'TWD', round(twd, 2), '(', price['currency'], price ['total'], ')')
    print()
  
  x = 1
  ##################THIRD INPUT:::number - Flight
  while True:
    while x == 1:
      prefer = int(input("Which one will you book? "))-1
      try:
        number = total[prefer]['id']
        price = total[prefer]['price']
        duration = total[prefer]['itineraries'][0]['duration']
        segment = total[prefer]['itineraries'][0]['segments'][0]
        deptime = segment['departure']['at']
        arrtime = segment['arrival']['at']
        twd = float(price['total']) * curr
        print()
        print(number +'.')
        print("Departure time   : ", deptime[len(ddate)+1:-3])
        print("Arrival time     : ", arrtime[len(ddate)+1:-3])
        print("Duration         : ", duration[2:])
        print("Price            : ", 'TWD', round(twd, 2), '(', price['currency'], price ['total'], ')')
        x = 2
      except IndexError as error:
        print("Number out of list.")
        print("Please enter the number in the list. ")
        x = 1
        continue
      
    #################FOURTH INPUT:::yes/no
    while x == 2:
      sure = input("Are you sure it's correct? (Yes/No) ")
      print()
      sure = sure.lower()
      if sure == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your request has been processed.")
        x = 3
      elif sure == 'no':
        x = 1
        #continue
      else:
        print("Please enter an appropriate answer.")
        x = 2

  #################FIFTH INPUT:::yes/no
    while x == 3:
      cont = input("Would you still like to know more? (Yes/No) ")
      cont = cont.lower()
      if cont == 'yes':
        print("1. Weather")
        print("2. News")
        x = 4
        while x == 4:
          ##################SIXTH INPUT:::1/2 - weather/news
          choice = input("Which one? ")
          if(choice == "1"):
            weather()
            print()
            x = 3
          elif choice == "2":
            news()
            print()
            x = 3
          else:
            print("Please enter 1 or 2.")
            x = 4
      elif cont == 'no':
        print("Got it. Thank you for using our service.")
        os._exit(0)
      else:
        print("Input unknown.")

except ResponseError as error:
  print(error)