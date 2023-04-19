import os
import requests as req
import json


class tools:
    def changeFileName(path, targetName):
        fileNames = os.listdir(path)
        i = 1
        for name in fileNames:
            src = os.path.join(path, name)
            dst = targetName + '.' + str(i) + '.jpg'
            dst = os.path.join(path, dst)
            os.rename(src, dst)
            i += 1

    def PushDiscord(msg):
        webhook_url = "https://discord.com/api/webhooks/1098274897865756703/TIi4WmcVharS3S74LpJFIHrmgJv2zRkIRc4XBanK0tou3X7BosP0XZYygZxBk7Q5eHhb"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "content": msg 
        }
        req.post(webhook_url, data=json.dumps(payload), headers=headers)






# dataDir = './dataset/AI-DATASET/data'
# train_dir = os.path.join(dataDir, 'trainData')
# examDir = os.path.join(train_dir, 'noodle_cup')

# tools.changeFileName(examDir, 'noodle_cup')
