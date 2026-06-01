from bot.client import client

try:
    result = client.futures_ping()
    print("Futures API Connected")
    print(result)

except Exception as e:
    print("Error")
    print(e)