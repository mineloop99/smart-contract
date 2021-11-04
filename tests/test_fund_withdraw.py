from brownie import network, accounts, exceptions
from scripts.helper import get_account, LOCAL_BLOCKCHAIN_DEVELOPMENT
from scripts.fund_deploy import deploy_fund
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund = deploy_fund()
    entrance_fee = fund.getEntranceFee() + 100
    tx = fund.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund.withdraw({"from": account})
    tx2.wait(1)
    assert fund.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_DEVELOPMENT:
        pytest.skip("only for local testing")
    fund = deploy_fund()
    bad_actor = accounts.add()
    with pytest.raises(ValueError):
        fund.withdraw({"from": bad_actor})
