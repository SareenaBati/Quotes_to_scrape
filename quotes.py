import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")
    driver.maximize_window()
    return driver


def test_first_quote():

    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        quoteElem = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='text'])[1]"))
        )
        actualResult = quoteElem.text.strip()
        expectedResult = "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, " First quote does not match!")
        print("Success: First quote verification passed!")
    finally:
        driver.quit()


def test_second_quote():
    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        quoteElem = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='text'])[2]"))
        )
        actualResult = quoteElem.text.strip()
        expectedResult = "“It is our choices, Harry, that show what we truly are, far more than our abilities.”"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, " Second quote does not match!")
        print(" Success: Second quote verification passed!")
    finally:
        driver.quit()


def test_third_quote():

    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        quoteElem = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='text'])[3]"))
        )
        actualResult = quoteElem.text.strip()
        expectedResult = "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, " Third quote does not match!")
        print(" Success: Third quote verification passed!")
    finally:
        driver.quit()


def test_next_button():

    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        nextBtn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//nav//a[contains(text(),'Next')]"))
        )
        actualResult = nextBtn.text.strip()
        expectedResult = "Next →"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, " Next button text does not match!")
        print("Success: Next button verification passed!")

        nextBtn.click()
        print(" Success: Next button clicked!")
    finally:
        driver.quit()


def test_third_quote_not_equal():
    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        quoteElem = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='text'])[3]"))
        )
        actualResult = quoteElem.text.strip()
        expectedResult = "none"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertNotEqual(actualResult, expectedResult, "Third quote should not be 'none'!")
        print(" Success: Third quote verification (not equal) passed!")
    finally:
        driver.quit()


def test_tag_assert_is_not():

    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        tag = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='tag-item']/a[@class='tag' and text()='love']"))
        )
        actualResult = tag.text.strip()
        expectedResult = "Viewing tag: love"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertIsNot(actualResult, expectedResult,
                                        " 'love' tag should not match 'Viewing tag: love'!")
        print(" Success: assertIsNot verification passed!")
    finally:
        driver.quit()


def test_tag_assert_is():

    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        tag = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='tag-item']/a[@class='tag' and text()='love']"))
        )
        actualResult = tag.text.strip()
        expectedResult = "love"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, " 'love' tag does not match expected value!")
        print(" Success: assertIs verification passed!")
    finally:
        driver.quit()


