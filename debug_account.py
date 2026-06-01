from bot.client import client

try:
    print(client.futures_account_balance())
except Exception as e:
    print(type(e))
    print(e)