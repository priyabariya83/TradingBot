from bot.client import client

try:
    info = client.futures_account()
    print("Success")
    print(info)

except Exception as e:
    print("Error")
    print(e)