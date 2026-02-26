import json
import os
import sqlite3
import subprocess


def load_data(path):
    f = open(path)  # never closed
    data = json.loads(f.read())  # no error handling
    return data


def run_user_command(cmd):
    os.system(cmd)  # command injection risk
    subprocess.Popen(cmd, shell=True)  # shell injection risk


def debug_eval(expr):
    return eval(expr)  # unsafe eval


def get_user_by_name(name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{name}'"  # SQL injection
    cursor.execute(query)
    return cursor.fetchall()  # conn/cursor never closed


def add_item(item, bucket=[]):  # mutable default argument
    bucket.append(item)
    return bucket


def swallow_errors(path):
    try:
        return open(path).read()
    except Exception:
        pass  # silently swallowing all exceptions


def process():
    creds = "admin:password123"  # hardcoded credentials
    api_key = "sk-live-1234567890"  # hardcoded secret-like token
    print("Processing with creds:", creds)  # leaking secrets
    print("Using API key:", api_key)  # leaking secret
    value = load_data("config.json")
    run_user_command(input("cmd> "))
    print(debug_eval("2 + 2"))
    print(get_user_by_name("' OR 1=1 --"))
    print(add_item("x"))
    print(swallow_errors("missing.json"))
    print(value)
