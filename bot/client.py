from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(
    API_KEY,
    API_SECRET,
    testnet=True
)

server_time = client.get_server_time()
system_time = int(time.time() * 1000)

client.timestamp_offset = (
    server_time["serverTime"] - system_time
)

print("Server Time :", server_time["serverTime"])
print("System Time :", system_time)
print("Offset      :", client.timestamp_offset)