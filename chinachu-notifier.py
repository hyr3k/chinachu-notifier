#!/usr/bin/env python3

import configparser
import sys
import os
import json
import slackweb

config_dir = os.path.dirname(os.path.abspath(__file__))
config_path = config_dir + "/config.ini"

config = configparser.ConfigParser()
config.read(config_path)
if config['slack']['slack_notify'] == 'yes':
  slack_url = config['slack']['hook_url']
  slack_icon = config['slack']['icon_url']
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

slack = slackweb.Slack(url=slack_url)

slack.notify(text=content, channel=slack_channel, username=slack_username)