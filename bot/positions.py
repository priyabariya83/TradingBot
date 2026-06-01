from bot.client import client

def get_open_positions():
    positions = client.futures_position_information()

    return [
        p for p in positions
        if float(p["positionAmt"]) != 0
    ]