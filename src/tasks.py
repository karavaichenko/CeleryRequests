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

    response = requests.post(address, headers=headers, data=data)
    return response.content

@app.task
def deleteRequestTask(address: str, authToken):

    headers = {
        'Authorization': authToken
    }

    response = requests.delete(address, headers=headers)
    return response.content