import configparser
import logging
import userbot

config = configparser.ConfigParser()
config.read("config.ini")

userbot.api_id = int(config["BotConfig"]["api_id"])
userbot.api_hash = config["BotConfig"]["api_hash"]

if config["BotConfig"]["useProxy"] == "True":
    userbot.proxy = (
        int(config["BotConfig"]["proxyType"]),
        config["BotConfig"]["proxyURL"],
        int(config["BotConfig"]["proxyPort"]))
else:
    userbot.proxy = ()

userbot.COMMAND_HEADER = config["PluginsConfig"]["COMMAND_HEADER"]
userbot.disableCommandList = config["PluginsConfig"]["disableCommand"].split(" ")

loggingObj = __import__("logging")
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=getattr(loggingObj, config["BotConfig"]["logLevel"].upper(), logging.INFO))

userbot.pluginDict = {}

userbot.start()
