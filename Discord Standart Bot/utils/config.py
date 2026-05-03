import json
import os

config_path = "data/config.json"

def loadConfig():
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(config_path):
        # create default config if none exists
        defaultConfig = {
            "logChannel": None,
            "welcomeChannel": None,
            "staffRole": None,
            "ticketCategory": None
        }
        saveConfig(defaultConfig)
        return defaultConfig
        
    with open(config_path, "r") as f:
        return json.load(f)

def saveConfig(data):
    with open(config_path, "w") as f:
        json.dump(data, f, indent=4)

def update_config(key, value):
    config = loadConfig()
    config[key] = value
    saveConfig(config)
