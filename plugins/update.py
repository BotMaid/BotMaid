class pluginClass:
    """更新 BotMaid"""
    registCommand = "update",
    listenPlainMessage = False

    async def onCommandMessageReceivedListener(client, event, command, args):
        import os
        import sys
        os.system("git pull")
        await client.edit_message(event.message, "更新完成，正在重启 BotMaid")
        # sys.exit(0)
        await client.disconnect()
