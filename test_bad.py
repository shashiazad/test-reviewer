import os
import json

def load_data(path):
    f = open(path)    # never closed
    data = json.loads(f.read())  # no error handling
    return data

def process():
    creds = "admin:password123"  # hardcoded credentials
    print("Processing with creds:", creds)  # leaking secrets
    value = load_data("config.json")
    print(value)
