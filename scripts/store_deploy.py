import os
from brownie import accounts, config, network, simple_storage


def deploy_storage():
    account = get_account()
    sto = simple_storage.deploy({"from": account})
    stored_value = sto.retrieve()
    print(stored_value)
    transaction = sto.store(15, {"from": account})
    transaction.wait(1)
    update_stored_value = sto.retrieve()
    print(update_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(os.getenv("PRIVATE_KEY"))


def main():
    deploy_storage()
