#!/usr/bin/env python

import ConfigParser
import email
import os
import sys
import urllib
import urllib2
from optparse import OptionParser

def post_groupme(settings, message):
    """ Post to groupme group """
    values = {}
    bot_id = settings.get('groupme', 'bot_id')
    url = settings.get('groupme', 'url')
    values['text'] = message
    values['bot_id'] = bot_id
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)

def parse_email(message):
    """ Raw mail message and return body string """
    constr_string = ''
    body = email.message_from_string(message)
    if body.is_multipart():
        for payload in body.get_payload():
            constr_string += payload.get_paylod()
    else:
        constr_string = body.get_payload()
    return constr_string

def read_config(file):
    """ Read config and return dict """
    config = ConfigParser.ConfigParser() 
    config.read(file)
    return config

def main():
    """ main """
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option("-c", "--config",
                      dest="config",
                      help="config file")
    (options, args) = parser.parse_args()
    config = read_config(options.config)
    message = sys.stdin.read()
    body = parse_email(message)
    post_groupme(config, body)

if __name__ == '__main__':
    main()
