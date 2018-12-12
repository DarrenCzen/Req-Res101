# This file helps me to understand how GET requests & responses work in python with http
# In every http process, requests are sent by client to the server and expects a response from the server

# URI, Unique Resource Identifier, eg: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier, contains Scheme, Hostname and FilePath
# helps to identify how the client goes about accessing a resource in the server

# HTTP GET Requests
# GET is the method that clients use when they want a server to send a resource like a webpage or a file

# 1xx - Informational, 2xx - Success, 3xx - Redirection, 4xx - Client Error, 5xx - Server Error
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Scraping Random Make Up Information Of Imaginary People From UINames Website

import requests

def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)

    decodedMsg = r.json()

    return "My name is {} {} and the PIN on my card is {}.".format(
        decodedMsg['name'], decodedMsg['surname'], decodedMsg['credit_card']['pin']
    )

if __name__ == '__main__':
    print(SampleRecord())