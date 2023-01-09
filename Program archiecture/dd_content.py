import csv
import random
from urllib import request
import json
import datetime
import tweepy

"""
Retrieve a random quote from the specified CSV file.
"""
def get_random_quote(quotes_file='quotes.csv'):
    try:  # load motivational quotes from csv file
        with open(quotes_file) as csvfile:
            quotes = [{'author': line[0],
                       'quote': line[1]} for line in csv.reader(csvfile,delimiter='|')]

    except Exception as e:  # use a default quote to help things turn out for the best
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright side of Life.'}]

    return random.choice(quotes)

"""
Retrieve the current weather forecast from OpenWeatherMap.
"""
def get_weather_forecast(coords={'lat':28.4717,'lon':-80.5378}):  # default location at cape canaveral,FL
    try:  # retrieve forecast for specified coordinates
        api_key = 'YOUR OPENWEATHERMAP API KEY GOES HERE'  # replace with your own OpenWeatherMap API key
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'],  # city name
                    'country': data['city']['country'],  # country name
                    'periods': list()}  # list to hold forecast data for future periods

        for period in data['list'][0:9]:  # populate list with next 9 forecast periods
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon':f'http://openweathermap.org/img/wn/{period}["weather"][0]["icon"]}.png'})
        return forecast

    except Exception as e:
        print(e)

"""
Retrieve the current trends from Twitter.
"""
def get_twitter_trends(woeid=23424977):
    try:  # retrieve Twitter trends for specified location
        api_key = 'YOUR TWITTER API KEY GOES HERE'  # replace with your own Twitter API key
        api_secret_key = 'YOUR TWITTER API SECRET KEY GOES HERE'  # replace with your own Twitter API secret key
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        return tweepy.API(auth).trends_place(woeid)[0]['trends']  # NOTE: Tweepy 4.0.0 renamed the 'trends_place' method to 'get_place_trends'

    except Exception as e:
        print(e)

def wikipedia_article():
    pass


if __name__ == '__main__':
    #### test get_random_quote() #####
    print('\nTesting Quote generation...')

    quote = get_random_quote()
    print(type(quote))
    print(f'- Random quote is "{quote["quote"]}" - {quote["author"]}')

    quote = get_random_quote(quotes_file=None)
    print(f'- Default quote is "{quote["quote"]}" - {quote["author"]}')