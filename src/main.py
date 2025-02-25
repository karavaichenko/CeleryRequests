from tasks import getRequestTask, postRequestTask, deleteRequestTask
from flask import Flask

app = Flask(__name__)

@app.route('/get')
def getByAddress(address):
    result = getRequestTask.delay(address)
    print('Task ID: ', result.id)
    print('Result: ', result.get())

@app.route('/post')
def postByAddress(address, data):
    result = postRequestTask.delay(address, data)
    print('Task ID: ', result.id)
    print('Result: ', result.get())
    
@app.route('/delete')
def deleteByAddress(address, authToken):
    result = deleteRequestTask(address, authToken)
    print('Task ID: ', result.id)
    print('Result: ', result.get())
