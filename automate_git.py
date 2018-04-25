#!/usr/bin/env python
import json
import subprocess

import datetime

import os

dictObj = {
    'path': '',
    'branch': '',
    'remote': ''
}

fr = open("git.txt", "r", encoding='utf-8')
print('请输入仓库路径:', end='')
json_str = json.loads(fr.read())
path = input()
if len(path) == 0:
    if len(json_str['path']) == 0:
        path = os.getcwd()
    else:
        path = json_str['path']
else:
    os.chdir(path)

print(path)
json_str['path'] = path
subprocess.call(["git", "add", "."])
print('请输入提交备注:', end='')
txt = input()
subprocess.call(["git", "commit", "-m", "auto push at " + txt + " " + str(datetime.datetime.now())])  # 加上当前系统的时间
print('请输入拉取/推送的分支(默认origin/develop):', end='')
input_str = input()
if len(input_str) == 0:
    if len(json_str['branch']) == 0 or len(json_str['remote']) == 0:
        pull_push = "develop"
        remote = "origin"
    else:
        pull_push = json_str['branch']
        remote = json_str['remote']
else:
    split_str = input_str.split('/')
    remote = split_str[0]
    pull_push = split_str[1]
json_str['branch'] = pull_push
json_str['remote'] = remote
subprocess.call(["git", "pull", remote, pull_push])
subprocess.call(["git", "push", remote, pull_push])
fw = open("git.txt", "w", encoding='utf-8')
fw.write(json.dumps(json_str))
fw.close()
