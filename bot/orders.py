import logging

def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        if order_type.upper() == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type.upper() == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(
            f"ORDER SUCCESS: {order}"
        )

        return order

    except Exception as e:

        logging.error(
            f"ORDER FAILED: {e}"
        )

        raise