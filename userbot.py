api_id: int
api_hash: str
proxy: tuple
COMMAND_HEADER: str
disableCommandList: list
pluginDict: dict


class myInfo:
    id: int
    username: str
    nickname: str


def start():
    import os
    from telethon import TelegramClient, events
    import logging

    client = TelegramClient('BotMaid', api_id, api_hash, proxy=proxy)

    class pluginLoader:
        def __init__(self):
            pluginDict["plainMessageListenerList"] = []
            self.loadPlugins()

        def loadPlugins(self):
            for filename in os.listdir("plugins"):
                if not filename.endswith(".py") or filename.startswith("_"):
                    continue
                self.pluginRegister(filename)

        def pluginRegister(self, filename):
            pluginName = os.path.splitext(filename)[0]
            plugin = __import__("plugins." + pluginName, fromlist=[pluginName])
            for command in plugin.pluginClass.registCommand:
                if command in disableCommandList:
                    continue
                pluginDict[command] = plugin.pluginClass
            if plugin.pluginClass.listenPlainMessage:
                pluginDict["plainMessageListenerList"].append(plugin.pluginClass)

    async def init():
        meObj = await client.get_me()
        myInfo.id = meObj.id
        myInfo.username = meObj.username
        myInfo.nickname = (lambda name: name if name != "None" else "")(str(meObj.first_name)) + \
                          (lambda name: name if name != "None" else "")(str(meObj.last_name))
        pluginLoader()
        return

    client.start()
    client.loop.run_until_complete(init())

    @client.on(events.NewMessage)
    async def onMessageReceived(event):
        try:
            if event.sender_id == myInfo.id:
                if event.raw_text.startswith(COMMAND_HEADER):
                    commArgs = event.raw_text.split(" ")
                    commStr = commArgs[0][len(COMMAND_HEADER):]
                    await pluginDict[commStr].onCommandMessageReceivedListener(client, event, commStr, commArgs[1::])

            for plugin in pluginDict["plainMessageListenerList"]:
                await plugin.onMessageReceivedListener(client, event, event.raw_text)
        except Exception as ex:
            logging.warning("Exception: ", ex)

    client.run_until_disconnected()
