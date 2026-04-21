import argparse
import logging
from client import get_client
from orders import place_order
from logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Trading Bot CLI")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    if args.side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    if args.type == "LIMIT" and not args.price:
        raise ValueError("Price required for LIMIT order")

    print("\nOrder Summary:")
    print(vars(args))

    confirm = input("Proceed? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        exit()

    client = get_client()

    logging.info(f"Request: {vars(args)}")

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nRESPONSE:")
    print(order)

    logging.info(f"Response: {order}")

    print("\nOrder placed successfully!")

except Exception as e:
    logging.error(str(e))
    print(f"\nError: {e}")
