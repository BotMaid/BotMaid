keywordsDict = {}


class pluginClass:
    """根据关键词回复
    添加: keywords add <关键词>===<回复内容>
    删除: keywords del <关键词>"""
    registCommand = "keywords",
    listenPlainMessage = True

    async def onCommandMessageReceivedListener(client, event, command, args):
        import sqlite3
        if args[0] == "add":
            key, reply = " ".join(args[1:]).split("===")
            conn = sqlite3.connect("configs/keywords/keywords.db")
            cursor = conn.cursor()
            if cursor.execute('select * from keywords where [key]=? and [group]=?',
                              (key, event.chat_id)).fetchall():
                cursor.execute('update keywords set reply = ? where [key]=? and [group]=?',
                               (reply, key, event.chat_id))

            else:
                cursor.execute('insert into keywords ([key], reply, [group]) values (?,?,?)',
                               (key, reply, event.chat_id))
            cursor.close()
            conn.commit()
            conn.close()
            await client.edit_message(event.message, f"规则 {key} 添加成功")

        if args[0] == "del":
            key = args[1]
            conn = sqlite3.connect("configs/keywords/keywords.db")
            cursor = conn.cursor()
            try:
                conn.execute("delete from keywords where [key]=? and [group]=?", (key, event.chat_id))
            except:
                pass
            cursor.close()
            conn.commit()
            conn.close()
            await client.edit_message(event.message, f"规则 {key} 删除成功")

        if args[0] == "list":
            conn = sqlite3.connect("configs/keywords/keywords.db")
            cursor = conn.cursor()
            tempStr = "---key--- ---reply--- ---group---\n"
            try:
                if args[1].lower() == "all":
                    for key, reply, group in cursor.execute('select * from keywords').fetchall():
                        tempStr += f"---{key}--- ---{reply}--- ---{group}---\n"
                    await client.edit_message(event.message, tempStr)
                else:
                    raise Exception

            except:
                for key, reply, group in cursor.execute('select * from keywords where [group]=?',
                                                        (event.chat_id,)).fetchall():
                    tempStr += f"---{key}--- ---{reply}--- ---{group}---\n"
                await client.edit_message(event.message, tempStr)
            cursor.close()
            conn.close()

        pluginClass.reFlashDict()

    async def onMessageReceivedListener(client, event, rawMsg):
        if not keywordsDict:
            return
        try:
            for key in keywordsDict[str(event.chat_id)].keys():
                if key in rawMsg:
                    await client.send_message(event.chat_id, keywordsDict[str(event.chat_id)][key],
                                              reply_to=event.message.id)
        except Exception as ex:
            pass

    def reFlashDict():
        import os
        import sqlite3
        if not os.path.exists("configs/keywords"):
            os.makedirs("configs/keywords")
            conn = sqlite3.connect("configs/keywords/keywords.db")
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE keywords (
                                            [key]   TEXT,
                                            reply   TEXT,
                                            [group] TEXT
                                        );
                                        """)
            cursor.close()
            conn.commit()
        else:
            conn = sqlite3.connect("configs/keywords/keywords.db")

        cursor = conn.cursor()
        for key, reply, group in cursor.execute('select * from keywords').fetchall():
            if not keywordsDict.get(group, {}):
                keywordsDict[group] = {}
            keywordsDict[group][key] = reply
        cursor.close()
        conn.close()


pluginClass.reFlashDict()
