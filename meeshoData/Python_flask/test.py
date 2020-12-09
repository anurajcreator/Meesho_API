import requests as rq

Base = "http://127.0.0.1:5000/api/trendy-stone-work-anklet/p/jgkz"

res = rq.get(Base).json()

print(res)