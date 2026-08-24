# This will be the new API layer for the project
# Goals:
# 1. Be able to communicate with the loacl Postgres image using FastAPI
# 2. Once able to communicate and get data, export this file as a Docker image to be pulled down in the future

# import the FastAPI package
import fastapi

# Verify that FastAPI has been installed and print the current version. Throw an error otherwise
try:
    print(fastapi.__version__)
except:
    print(Exception)