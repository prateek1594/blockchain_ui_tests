from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.transaction_header = (By.CSS_SELECTOR, "div[class='transactions'] h3")

    def open(self, url):
        self.driver.get(url)

    def transaction_heading(self):
        return self.driver.find_element(*self.transaction_header)
    
    def find_all_transactions(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.transaction-box')

    def check_transactions_count_header(self):
        try:
            header = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(self.transaction_header)
            )

            text = header.text
            expected_text = "25 of 2875"

            if expected_text in text:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error Occurred: {str(e)}")

    def get_hash_values(self, box):
        input_count = len(box.find_elements(By.TAG_NAME,'input'))
        output_count = len(box.find_elements(By.TAG_NAME,'output'))

        if input_count == 1 and output_count == 2:
            return box.get_attribute('data-toggle-tx')
        else:
            return None
