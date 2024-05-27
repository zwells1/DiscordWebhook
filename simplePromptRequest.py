from source import midjourney_api
import json
import os
import sys
import time

#channel specific details
path = os.path.join(os.path.dirname(__file__), "source\submodule\DiscordInfo\MidjourneyDetails.json")

discordDetails = None

try:
    with open(path, "r") as file:
        discordDetails = json.load(file)
except Exception as e:
    print("no file found")
    time.sleep(2)
    sys.exit(1)

data = discordDetails["general_test"][0]

prompt= "happy cat at beach, eating ice cream, minimalist --ar 3:1"

application_id = data["application_id"]
guild_id = data["guild_id"]
channel_id = data["channel_id"]
version = data["version"]
id = data["id"]
authorization = data["authorization"]

midjourney = midjourney_api.MidjourneyApi(prompt, application_id, guild_id, channel_id, version, id, authorization)
