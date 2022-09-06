"""Chatbot101 with AWS Lambda Console Script.
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
"""

import requests
import json
from webexteamsbot import TeamsBot
from models import Response
from functools import partial
import argparse
import getpass
#Set Token Statically
TOKEN = ""
#Create Token flag
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--token", type=str, help="The webex bot token", default="")
args = parser.parse_args()
if TOKEN:
    pass
elif args.token:
    #set Token to TOKEN via --token flag
    TOKEN = args.token
else:
    #Get Token via cli input
    TOKEN = getpass.getpass("Enter Webex Token: ")



# An example using a Response object.  Response objects allow more complex
# replies including sending files, html, markdown, or text. Rsponse objects
# can also set a roomId to send response to a different room from where
# incoming message was recieved.
def ret_message(incoming_msg):
    """
    Sample function that uses a Response object for more options.
    :param incoming_msg: The incoming message object from Teams
    :return: A Response object based reply
    """
    # Create a object to create a reply.
    response = Response()

    # Set the text of the reply.
    response.text = "Here's a fun little meme."

    # Craft a URL for a file to attach to message
    u = "https://sayingimages.com/wp-content/uploads/"
    u = u + "aaaaaalll-righty-then-alrighty-meme.jpg"
    response.files = u
    return response


def current_time(bot, incoming_msg):
    """
    Sample function that returns the current time for a provided timezone
    :param incoming_msg: The incoming message object from Teams
    :return: A Response object based reply
    """
    # Extract the message content, without the command "/time"
    timezone = bot.extract_message("/time", incoming_msg.text).strip()
    timezone = timezone or "est"
    # Craft REST API URL to retrieve current time
    #   Using API from http://worldclockapi.com
    u = "http://worldclockapi.com/api/json/{timezone}/now".format(
        timezone=timezone)
    r = requests.get(u).json()

    # If an invalid timezone is provided, the serviceResponse will include
    # error message
    if r["serviceResponse"]:
        return "Error: " + r["serviceResponse"]

    # Format of returned data is "YYYY-MM-DDTHH:MM<OFFSET>"
    #   Example "2018-11-11T22:09-05:00"
    returned_data = r["currentDateTime"].split("T")
    cur_date = returned_data[0]
    cur_time = returned_data[1][:5]
    timezone_name = r["timeZoneName"]

    # Craft a reply string.
    reply = "In {TZ} it is currently {TIME} on {DATE}.".format(
        TZ=timezone_name, TIME=cur_time, DATE=cur_date
    )
    return reply


def instatiate_bot(event, debug=True):
    return TeamsBot("WebexBot", event, TOKEN, debug=debug)


def default(message):
    return "Thank you for submitting your question or comment.\
 Our team is hard at work, however we will respond to your question or comment within 1 business day.\
 Until then, here’s CX Cloud FedRAMP Asked & Answered to review while we work hard to answer your question."


def hey(message):
    return f"Hey {message.personEmail}"


def main(event, context):
    webex_bot = instatiate_bot(event)
    # add commands here
    webex_bot.add_command("/time", "A default msg", partial(current_time, webex_bot))
    webex_bot.set_help_message("Howdy")
    webex_bot.set_greeting(default)
    # Respond to message
    reply = webex_bot.process_incoming_message()
    print(reply)
    msg = {"message": reply}
    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }
