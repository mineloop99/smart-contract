from brownie import simple_storage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    sto = simple_storage.deploy({"from": account})
    starting_value = sto.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_deploy():
    # Arrange
    account = accounts[0]
    sto = simple_storage.deploy({"from": account})
    # Act
    expected = 15
    sto.store(expected, {"from": account})
    # Assert
    assert sto.retrieve() == expected
