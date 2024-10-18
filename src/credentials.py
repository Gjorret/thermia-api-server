import os

try:
    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
except KeyError as e:
    raise KeyError(f"Environment variable {e.args[0]} not found. Please set the environment variable before running the script.")