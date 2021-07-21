class pluginClass:
    """
    直接执行 shell 命令
    ⚠️注意: 不要执行无法自动结束的命令"""
    registCommand = "sh",
    listenPlainMessage = False

    async def onCommandMessageReceivedListener(client, event, command, args):
        import io
        import subprocess

        proc = subprocess.Popen(" ".join(args), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        proc.wait()
        stream_stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8')
        stream_stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8')

        str_stdout = str(stream_stdout.read())
        str_stderr = str(stream_stderr.read())

        tempStr = f"str_stdout:\n{str_stdout}\n\nstr_stderr:\n{str_stderr}"

        await client.edit_message(event.message, tempStr)
