from bot.client import client

try:
    server_time = client.get_server_time()

    print("Connected Successfully")
    print(server_time)

except Exception as e:
    print("Connection Failed")
    print(e)