import pytest
from pages.transaction_page import TransactionPage

BASE_URL = "https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"

@pytest.mark.usefixtures("driver")
def test_header(driver):
    transactions_page = TransactionPage(driver)
    transactions_page.open(BASE_URL)
    assert transactions_page.check_transactions_count_header()

@pytest.mark.usefixtures("driver")
def test_find_and_print_hash(driver):
    page = TransactionPage(driver)
    page.open(BASE_URL)

    all_transactions = page.find_all_transactions()
    hash_values = []

    for box in all_transactions:
        get_hash_value = page.get_hash_values(box)
        if get_hash_value:
            hash_values.append(get_hash_value)
    for value in hash_values:
        print(value)
