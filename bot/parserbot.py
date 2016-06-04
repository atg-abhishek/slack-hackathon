#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from slackclient import SlackClient
import time
import yaml
import json

config = yaml.load(file('parserbot.conf', 'r'))
api_key = config["SLACK_API_TOKEN"]
offices = config["OFFICES"]

client = SlackClient(api_key)

if client.rtm_connect():
  print("connected")
  for office in offices:
    print(office)
    channel_id = client.server.channels.find(office).id
    history = client.api_call("channels.history", channel=channel_id)
    with open('{}.json'.format(office), 'w') as outfile:
      json.dump(json.loads(history), outfile)
