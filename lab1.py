import requests

response = requests.get('https://github.com/XiZhang9/404/raw/master/lab1.py')

print (response.text)
