import argparse

from bot.client import client
from bot.orders import place_order
from bot.validators import *

from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    print("\nORDER REQUEST")
    print("----------------------")
    print("Symbol :", args.symbol)
    print("Side   :", args.side)
    print("Type   :", args.type)
    print("Qty    :", args.quantity)

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nSUCCESS")
    print("----------------------")

    print(
        "Order ID :",
        order["orderId"]
    )

    print(
        "Status :",
        order["status"]
    )

except Exception as e:

    print("\nFAILED")
    print(e)