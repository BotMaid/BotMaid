class pluginClass:
    """这是说明"""

    # 要注册的命令
    registCommand = "example", "example1",

    # 是否监听所有消息
    listenPlainMessage = False
    # 群聊事件（加群退群等）
    listenChatAction = False

    # 配置文件建议放在 configs 目录下
    # 直接 configs/fileName 这样使用即可

    async def onCommandMessageReceivedListener(self, client, event, command, args):
        chat_id = event.chat_id
        sender_id = event.sender_id
        message_id = event.message.id

    async def onMessageReceivedListener(self, client, event, rawMsg):
        pass
