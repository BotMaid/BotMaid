class pluginClass:
    """~~复读机~~
    用法 re <次数>"""
    registCommand = "re",
    listenPlainMessage = False
    listenChatAction = False

    async def onCommandMessageReceivedListener(self, client, event, command, args):
        if event.reply_to_msg_id:
            await client.delete_messages(event.chat_id, event.message)
            try:
                time = int(args[0])
            except Exception:
                time = 1
            for i in range(time):
                await client.forward_messages(event.chat_id, event.reply_to_msg_id, event.chat_id)
