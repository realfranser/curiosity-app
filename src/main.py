from flask import Flask, request # Flask Request Library that notify when a rewuest is sent
import json #structuring data
import requests # Request Data Library, allows to send our own web request
#import os
from random import randint

app = Flask('bootcamp')

with open('facts.json') as json_file:
  data = json.load(json_file)

def get_topic(token):
  if token in ('h', 'H', 'History', 'history'):
    return 'history'
  
  if token in ('r', 'R', 'Random', 'random'):
    return 'random'

  if token in ('t', 'T', 'tech', 'Tech', 'Technology', 'technology'):
    return 'technology'
  
  if token in ('n', 'N', 'Nature', 'nature'):
    return 'nature'

  return 'no_token'


@app.route('/Finder', methods=['GET', 'POST'])
def Finder():
  token = request.values['Body']
  
  topic = get_topic(token)

  if topic == 'no_token':
    return """<?xml version="1.0" encoding="UTF-8"?>
  <Response>
    <Message>Ahoy! This app shows you a curiosity about theese topics: 
    technology, nature, history or random. In order to select one of the above just type \'t\', \'n\', \'h\' or \'r\'. Similar inputs are also valid.</Message> 
  </Response>"""

  curiosity_list = data[topic]['fact_list']
  list_size = len(curiosity_list)
  ran_index = randint(0, list_size)
  curiosity = curiosity_list[ran_index]
  return """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
      <Message>{}</Message> 
    </Response>""".format(curiosity)
    

app.run(debug=True, host='0.0.0.0', port=8080)