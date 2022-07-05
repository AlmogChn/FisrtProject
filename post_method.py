import requests
res = requests.put('http://127.0.0.1:5000/users/2', json={"user_name":'aalmog'})
if res.ok:
    print(res.json())
else:
    print(res.json())