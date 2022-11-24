import requests

res = requests.post(
    'http://localhost:5000/json', 
    json = {
        'acc': 'admin',
        'pw': 'password'
    }, 
    headers={"Content-Type": "application/json"}
)

print(res.text)