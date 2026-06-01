import requests

try:
    response = requests.get(
        "https://testnet.binancefuture.com/fapi/v1/ping",
        timeout=20
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

except Exception as e:
    print(type(e))
    print(e)