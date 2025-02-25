from celeryConf import app
import requests

@app.task
def getRequestTask(address: str):
    response = requests.get(address)
    return response.content 

@app.task
def postRequestTask(address: str, data):

    headers = {
        'Content-Type': 'aplication/json',
    }

    response = requests.post(address, data=data, headers=headers)
    return response.content