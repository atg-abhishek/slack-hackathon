#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from slackclient import SlackClient
import time
import yaml
import json
import requests

def save_string_as_json_file(filename, content):
  with open('{}.json'.format(filename), 'w') as outfile:
    json_content = json.loads(content)
    json.dump(json_content, outfile)

config = yaml.load(file('parserbot.conf', 'r'))
api_key = config["SLACK_API_TOKEN"]
offices = config["OFFICES"]
manager_id = config["MANAGER_ID"]

client = SlackClient(api_key)

if client.rtm_connect():
  print("Connected:")
  for office in offices:
    print(office)
    channel_id = client.server.channels.find(office).id
    history = client.api_call("channels.history", channel=channel_id).replace('\u2019', '\'') # hacky way of fixing encoding with apostrophe
    # print(len(json.loads(history)['messages']))
    # save_string_as_json_file(filename=office, content=history)

  while True:
    last_read = client.rtm_read()
    if last_read:
      try:
          parsed = last_read[0]['text']
          #reply to channel message was found in.
          message_channel = last_read[0]['channel']
          if message_channel.startswith('D') and "update" in parsed: #TODO: Restrict access with last_read[0]['user']:
            # print last_read[0]
            client.rtm_send_message(message_channel,
                                      "No problem! Please give me a minute to analyze the latest messages. :clock1:")

            r = requests.get("http://ec2-52-87-240-146.compute-1.amazonaws.com:23001/trigger")
            # r = requests.get("http://google.com")
            client.rtm_send_message(message_channel,
                                      "Got the results back! Check them out at http://bit.ly/28cy4vX")
      except:
          pass
    time.sleep(1)