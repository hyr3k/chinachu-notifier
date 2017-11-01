#!/usr/bin/env python3

import configparser
import sys
import os
import json
import requests

config_dir = os.path.dirname(os.path.abspath(__file__))
config_path = config_dir + "/config.ini"

config = configparser.ConfigParser()
config.read(config_path)
if config['slack']['slack_notify'] == 'yes':
  slack_url = config['slack']['hook_url']
  slack_icon_emoji = config['slack']['icon_emoji']
  slack_channel = config['slack']['channel']
  slack_username = config['slack']['username']
  slack_post_text = config['slack']['post_text']
else:
  pass

# data path
argv1 = sys.argv[1]

# program data(JSON)
argv2 = sys.argv[2]

program_data = json.loads(argv2)

content = slack_post_text + program_data['fullTitle']

post_json = {
  "text":content,
  "username":slack_username,
  "icon_emoji":slack_icon_emoji,
  "channnel":slack_channel,
  }

if __name__ == '__main__':
  r = requests.post(slack_url, data = json.dumps(post_json))
