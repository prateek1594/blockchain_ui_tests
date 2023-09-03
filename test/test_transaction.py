import pytest
from pages.transaction_page import TransactionPage

@pytest.mark.usefixtures("driver")
def test_header(driver)):
    transactions_page = TransactionPage(driver)
    transactions_page.open("https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")
    assert transactions_page.check_transactions_count_header()

@pytest.mark.usefixtures("driver")
def test_find_and_print_hash(driver):
    page = TransactionPage(driver)
    page.open("https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")

    all_transactions = page.find_all_transactions()
    hash_values = []

    for box in all_transactions:
        get_hash_values = page.get_hash_values(box)
        if hash_values:
            hash_values.append(get_hash_values)
    
    for value in hash_values:
        print(values)
