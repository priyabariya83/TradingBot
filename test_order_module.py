from bot.client import client
from bot.orders import place_order

try:
    order = place_order(
        client,
        "BTCUSDT",
        "BUY",
        "MARKET",
        0.001
    )

    print("SUCCESS")
    print(order)

except Exception as e:
    print(type(e))
    print(e)