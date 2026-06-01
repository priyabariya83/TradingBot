from bot.client import client

try:
    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print("SUCCESS")
    print(order)

except Exception as e:
    print(type(e))
    print(e)