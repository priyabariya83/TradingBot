from bot.client import client

try:
    positions = client.futures_position_information()

    print("\nOPEN POSITIONS")
    print("------------------------")

    for p in positions:
        if float(p["positionAmt"]) != 0:
            print(
                p["symbol"],
                p["positionAmt"],
                p["entryPrice"]
            )

except Exception as e:
    print("Error")
    print(e)