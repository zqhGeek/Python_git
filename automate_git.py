#!/usr/bin/env python
import json
import subprocess

import datetime

import os

dictObj = {
    'path': '',
    'branch': ''
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
print('请输入拉取/推送的分支(默认develop):', end='')
pull_push = input()
if len(pull_push) == 0:
    if len(json_str['branch']) == 0:
        pull_push = "develop"
    else:
        pull_push = json_str['branch']
json_str['branch'] = pull_push
subprocess.call(["git", "pull", "origin", pull_push])
subprocess.call(["git", "push", "origin", pull_push])
fw = open("git.txt", "w", encoding='utf-8')
fw.write(json.dumps(json_str))
fw.close()
