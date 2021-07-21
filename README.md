# 介绍

待会再写

# 使用说明

- clone 项目并进入文件夹 `git clone https://github.com/BotMaid/BotMaid.git && cd BotMaid`

- 首先复制 `配置文件`

- `cp config.gen.ini config.ini`

- 在 `conifg.ini` 中填写你的 `api_id` 和 `api_hash` [申请地址](https://my.telegram.org/)

- 安装依赖 `pip3 install -r requirements.txt`

- 启动程序登录账号

  `python3 main.py`

  此步需要填入 **包括国际区号** 的完整电话号码（eg：+17899871234）

  然后 tg 会发给你的其他客户端发送验证码，填入验证码后，回车，如有两步验证密码，则再输入两步验证密码即可。

⚠️ 请注意保护好您已登录的 BotMaid.session 。此文件可以进行账号 **所有** 操作，请不要分享给他人使用

# 持久化运行

```shell
cat <<'EOF' > /etc/systemd/system/botmaid.service
[Unit]
Description=BotMaid daemon
After=network.target

[Install]
WantedBy=multi-user.target

[Service]
Type=simple
WorkingDirectory=/path_to/BotMaid
ExecStart=/usr/bin/python3 main.py
Restart=always
EOF
```

其中 /path_to/BotMaid 需要换成项目文件的 **绝对位置**

如果你不知道位于哪里，你可以输入 `pwd` 来查看当前目录的 绝对位置

启动程序：`systemctl start botmaid`

设置为开机自启：`systemctl enable botmaid`

停止程序：`systemctl stop botmaid`

# 进阶配置

还没写，不过有几个点提醒一下，可以先自行 Google ，还是不知道在说什么的可以等我补上这一节

1. 不要用 root 用户运行，新建个用户单独运行 BotMaid

2. 非 root 运行等时候注意文件权限， systemctl 脚本中也需要指定用户

```shell
User=myuser
Group=myuse
```

