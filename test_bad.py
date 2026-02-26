import os
import json
import subprocess


GLOBAL_CACHE = {}

def load_data(path):
    f = open(path)    # never closed
    data = json.loads(f.read())  # no error handling
    return data

def process():
    creds = "admin:password123"  # hardcoded credentials
    print("Processing with creds:", creds)  # leaking secrets
    value = load_data("config.json")
    print(value)


def run_user_command(user_input):
    # command injection risk
    os.system("echo " + user_input)
    subprocess.run("ls " + user_input, shell=True)


def parse_expression(expr):
    # arbitrary code execution
    return eval(expr)


def get_user(db, username):
    # SQL injection risk
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return db.execute(query)


def divide(a, b):
    try:
        return a / b
    except Exception:
        # hides root cause and silently continues
        return None


def append_item(item, bucket=[]):
    # mutable default argument issue
    bucket.append(item)
    return bucket


def write_temp(content):
    f = open("/tmp/output.txt", "w")
    f.write(content)
    # file handle intentionally never closed
