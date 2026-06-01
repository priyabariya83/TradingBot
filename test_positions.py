from bot.client import client

try:
    info = client.futures_account()

    print("Success")

    print("Total Wallet Balance:",
          info["totalWalletBalance"])

    print("Available Balance:",
          info["availableBalance"])

except Exception as e:
    print("Error")
    print(e)
