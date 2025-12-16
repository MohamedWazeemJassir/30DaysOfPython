import requests


requests.post("https://ntfy.sh/day9notifications", 
    data="Process Done !!!!!".encode(encoding='utf-8'))
