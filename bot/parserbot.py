#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from slackclient import SlackClient
import time
import yaml

config = yaml.load(file('parserbot.conf', 'r'))
api_key = config["SLACK_API_TOKEN"]
client = SlackClient(api_key)

if client.rtm_connect():
    print("connected")
    # while True:
    last_read = client.rtm_read()
    channel1_id = client.server.channels.find("london").id

    history = client.api_call("channels.history", channel=channel1_id)
    print(history)

    if last_read:
        try:
            parsed = last_read[0]['text']
            #reply to channel message was found in.
            message_channel = last_read[0]['channel']
            # print(message_channel)
            if parsed and 'food:' in parsed:
                choice = random.choice(['hamburger', 'pizza'])
                client.rtm_send_message(message_channel,
                                        'Today you\'ll eat %s.' % choice)
        except:
            pass
