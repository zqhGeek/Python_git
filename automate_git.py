#!/usr/bin/env python

import subprocess

import datetime

import os

os.chdir("D:\IDEA_Project\python_git")
print(os.getcwd())
subprocess.call(["git", "add", "."])
print('请输入提交备注:', end='')
txt = input()
subprocess.call(["git", "commit", "-m", "auto push at " + txt + str(datetime.datetime.now())])  # 加上当前系统的时间
print('请输入拉取/推送的分支(默认master):', end='')
pull_push = input()
if len(pull_push) == 0:
    pull_push = "master"
subprocess.call(["git", "pull", "server", pull_push])
subprocess.call(["git", "push", "server", pull_push])
