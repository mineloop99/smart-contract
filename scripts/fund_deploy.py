from brownie import fund_me, network, config, MockV3Aggregator
from scripts.helper import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_DEVELOPMENT


def deploy_fund():
    account = get_account()
    # pass the price feed address
    # if on a persistent network use associated network
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_DEVELOPMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        print("Mocks deployed")
        price_feed_address = MockV3Aggregator[-1].address
    fund = fund_me.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to: {fund.address}")
    return fund


def main():
    deploy_fund()
