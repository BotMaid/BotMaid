class pluginClass:
    """删除回复的消息"""
    registCommand = "del", "delete",
    listenPlainMessage = False
    listenChatAction = False

    async def onCommandMessageReceivedListener(self, client, event, command, args):
        if event.is_private:
            await client.delete_messages(event.chat_id, event.message.reply_to_msg_id)
        else:
            permissions = await client.get_permissions(event.chat, "me")
            if permissions.delete_messages and event.reply_to_msg_id:
                await client.delete_messages(event.chat_id, event.message.reply_to_msg_id)
        await client.delete_messages(event.chat_id, event.message)
