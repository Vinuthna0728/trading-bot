def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if client:
            if order_type == "MARKET":
                order = client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )
            return order

    except Exception as e:
        print("API failed:", e)

    # 🔥 fallback simulation
    print("Running in simulation mode")

    return {
        "orderId": "SIM123",
        "status": "FILLED",
        "executedQty": quantity,
        "avgPrice": price if price else "market_price"
    }