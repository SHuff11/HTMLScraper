import requests
import argparse


parser = argparse.ArgumentParser(usage='This program will send out an http request to access the content of the webpage you\'ve provided',)
parser.add_argument('webpage', type=str, help='Enter the URL of the webpage to send the http request to')
args = parser.parse_args()

webpage = args.webpage

if not (webpage.startswith('http://') or webpage.startswith('https://')):   
    webpage = 'http://' + webpage

response = requests.get(webpage)
print(response.headers)

#bring in data

response_headers = response.headers



#loop through dict data for providing keys and values in text formate
for key,value in response_headers.items():
    # import pdb; pdb.set_trace()
    print(key, value)

#brand new flask server
#
