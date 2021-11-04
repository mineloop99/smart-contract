from brownie import fund_me
from brownie.network import account
from scripts.helper import get_account


def fund():
    fund = fund_me[-1]
    account = get_account()
    entrance_fee = fund.getEntranceFee()
    print(f"Entrance fee: ", entrance_fee)
    print("Funding...")
    fund.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund = fund_me[-1]
    account = get_account()
    fund.withdraw({"from": account})


def main():
    fund()
    withdraw()
