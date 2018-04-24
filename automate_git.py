#!/usr/bin/env python

import subprocess

import datetime

subprocess.call(["git", "add", "."])
print('请输入提交备注:', end='')
txt = input()
subprocess.call(["git", "commit", "-m", "auto push at " + txt + str(datetime.datetime.now())])  # 加上当前系统的时间
pull_push = "master"
print('请输入拉取/推送的分支(默认master):', end='')
pull_push = input()
subprocess.call(["git", "pull", "server", pull_push])
subprocess.call(["git", "push", "server", pull_push])
