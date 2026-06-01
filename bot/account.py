from bot.client import client

def get_account_balance():
    return client.futures_account_balance()