class pluginClass:
    """~~你搁着套娃呢~~
    help <插件名字> - 查看插件帮助信息"""
    registCommand = "help",
    listenPlainMessage = False

    async def onCommandMessageReceivedListener(client, event, command, args):
        from userbot import pluginDict
        if not args:
            tempText = "已加载的插件有:\n"

            for key in pluginDict.keys():
                if key == "plainMessageListenerList":
                    continue
                tempText += f"`{key}`\n"

            tempText += "加载完成"

        else:
            tempText = ""
            for commandSingle in args:
                try:
                    tempText += "{pluginName}:\n".format(pluginName=commandSingle)
                    tempText += "{helpText}\n".format(helpText=pluginDict[commandSingle].__doc__)
                    tempText += "\n"
                except:
                    tempText += "该插件未找到 或 未提供说明\n\n"

        await client.edit_message(event.message, tempText)
