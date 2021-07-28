import configparser


class pluginClass:
    """自动删除新加用户，管理员手动添加（非邀请链接）不会删除"""
    registCommand = "autoKick",
    listenPlainMessage = False
    listenChatAction = True

    autoKickList = []

    def __init__(self):
        try:
            import os
            if not os.path.exists("configs/autoKick"):
                os.makedirs("configs/autoKick")
            config = configparser.ConfigParser()
            config.read("configs/autoKick/config.ini")
            if "autoKickGroup" in config:
                if "Groups".lower() in config["autoKickGroup"]:
                    self.autoKickList += config.get("autoKickGroup", option="Groups", fallback="").split("|")
                    return

            config["autoKickGroup"] = {}
            config["autoKickGroup"]["Groups"] = ""
            with open('configs/autoKick/config.ini', 'w') as configfile:
                config.write(configfile)
        except Exception as ex:
            print(ex)

    async def onCommandMessageReceivedListener(self, client, event, command, args):
        config = configparser.ConfigParser()
        config.read("configs/autoKick/config.ini")

        if args[0].lower() in ["true", "add", "on"]:
            permissions = await client.get_permissions(event.chat, "me")
            if permissions.ban_users and permissions.anonymous:
                config["autoKickGroup"]["Groups"] += f"|{event.chat_id}"
                await client.delete_messages(event.chat_id, event.message)
            else:
                await client.edit_message(event.message, "需要给予 匿名 和 封禁用户(ban) 权限才能正常使用")
        if args[0].lower() in ["false", "delete", "del", "off"]:
            config["autoKickGroup"]["Groups"] = config["autoKickGroup"]["Groups"].replace(f"|{event.chat_id}", "")

        with open('configs/autoKick/config.ini', 'w') as configfile:
            config.write(configfile)
        self.__init__()

    async def onChatActionListener(self, client, event):
        try:
            if str(event.chat_id) in self.autoKickList:
                await event.delete()

                if event.user_joined:
                    import time

                    hintMsg = await client.send_message(event.chat_id, "本群不允许人加入，10秒后你将会被移除")
                    await client.edit_permissions(event.chat, event.user, send_messages=False)
                    time.sleep(10)
                    await client.delete_messages(event.chat, hintMsg)
                    await (await client.kick_participant(event.chat, event.user)).delete()
        except:
            await self.checkPermission(client, event)

    async def checkPermission(self, client, event):
        config = configparser.ConfigParser()
        config.read("configs/autoKick/config.ini")

        permissions = await client.get_permissions(event.chat, "me")
        if not (permissions.ban_users and permissions.anonymous):
            config["autoKickGroup"]["Groups"] = config["autoKickGroup"]["Groups"].replace(f"|{event.chat_id}", "")

        with open('configs/autoKick/config.ini', 'w') as configfile:
            config.write(configfile)
        self.__init__()
