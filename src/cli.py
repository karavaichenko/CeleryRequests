from main import getByAddress, postByAddress
import json

def getReq(args):
    try:
        getByAddress(args[1])
    except:
        print("Incorrect request address")

def postReq(args):
    try:
        with open(args[2], "r") as file:
            data = json.load(file)
        postByAddress(args[1], data)
    except(FileNotFoundError):
        print("Incorrect path to JSON")
    except:
        print("Incorrect request address")


while True:
    print("\n\nChoose request")
    print("get 'address'")
    print("post 'address' 'path_to_JSON'")
    print("exit\n\n")
    inp = input()
    args = inp.split()
    if args[0] == "exit":
        break
    elif len(args) < 2:
        print("Error: Expected more arguments")
    elif args[0] == "get":
        getReq(args)
    elif args[0] == "post":
        postReq(args)