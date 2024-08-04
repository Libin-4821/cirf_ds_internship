# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:23:27 2024

@author: USER
"""

import requests
import json

GITHUB_USERNAME = "Libin-4821"
ACCESS_TOKEN = "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" 
REPO_NAME = "cirf_ds_internship"

API_ENDPOINT = f"https://api.github.com/user/repos"

payload = {
    "name": REPO_NAME,
    "description": "This is a new repository",
    "private": False,
    "auto_init": True,
    "gitignore_template": "Python"
}

headers = {
    "Authorization": f"Token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Repository created successfully!")
else:
    print(f"Failed to create repository: {response.status_code}")
    print(response.json())
