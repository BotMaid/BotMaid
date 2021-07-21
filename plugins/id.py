class pluginClass:
    """打印相关 ID 信息"""
    registCommand = "id",
    listenPlainMessage = False

    async def onCommandMessageReceivedListener(client, event, command, args):
        # chat = await event.get_chat()
        # sender = await event.get_sender()
        tempText = "chat_id: {chat_id}\nsender_id: {sender_id}\nmessage_id: {message_id}\n".format(
            chat_id=event.chat_id,
            sender_id=event.sender_id,
            message_id=event.message.id)

        if event.message.reply_to_msg_id:
            tempText += "reply_to_msg_id:{reply_to_msg_id}".format(reply_to_msg_id=event.message.reply_to_msg_id)

        await client.edit_message(event.message, tempText)
