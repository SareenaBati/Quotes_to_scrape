import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def setup():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")
    driver.maximize_window()
    return driver


def teardown(driver):
    driver.quit()

# assertequal
def first_quote(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(),'“The world as we have created it is a process of o')]")))

def second_quote(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//span[@class='text'])[2]")))

def third_quote(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//span[@class='text'])[3]")))

def check_quotes(driver):
    wait=WebDriverWait(driver,10)
    return wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'text')))

def next_button(driver):
    button= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//nav//a[contains(text(),'Next')]")))




def test_first_quote():
    driver = setup()

    try:
        quoteElem = first_quote(driver)
        actualResult = quoteElem.text
        expectedResult = "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, f'Failed: Expected "{expectedResult}", but got "{actualResult}"')
        print("Success: Quote verification passed!")

    except Exception as e:
        print(f"Error: {e}")


def test_second_quote():
    driver=setup()

    try:
        quoteElem = second_quote(driver)
        actualResult=quoteElem.text
        expectedResult="“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")
        unittest.TestCase().assertEqual(actualResult, expectedResult,
                                        f'Failed: Expected "{expectedResult}", but got "{actualResult}"')
        print("Success: Quote verification passed!")

    except AssertionError as e:
        print(e)

    teardown(driver)

def test_thirds_quote():
    driver=setup()
    try:
        quoteElem = third_quote(driver)
        actualResult = quoteElem.text
        expectedResult = "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")
        unittest.TestCase().assertEqual(actualResult,expectedResult,f'Failed:Expected"{expectedResult}",but got "{actualResult}')
        print("Success: Quote verification passed!")
    except AssertionError as e:
        print(e)


def test_nexts_button():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav//a[contains(text(),'Next')]")))
        actualResult = next_button.text
        expectedResult = "Next →"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")
        unittest.TestCase().assertEqual(actualResult,expectedResult,f'Failed:Expected"{expectedResult}",but got "{actualResult}')
        print("Success: Next button test passed!")

        next_button.click()
        print("Success: Next button clicked!")

    except AssertionError as e:
        print(e)

    teardown(driver)


# assert not equal

# def test_next_button():
#     driver = setup()
#     wait = WebDriverWait(driver, 10)
#     try:
#         next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav//a[contains(text(),'Next')]")))
#         actualResult = next_button.text
#         expectedResult = "none"
#         pprint(f"Actual Result: {actualResult}")
#         print(f"Expected Result:{expectedResult}")
#         unittest.TestCase().assertNotEqual(actualResult,expectedResult,f'Failed:Expected "{expectedResult}",but got "{actualResult}')
#         print("Success: Next button test passed!")
#
#         next_button.click()
#         print("Success: Next button clicked!")
#
#     except AssertionError as e:
#         print(e)
#
#     teardown(driver)


def test_third_quote():
    driver = setup()
    try:
        quoteElem = third_quote(driver)
        actualResult = quoteElem.text
        expectedResult = "“none”"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")

        unittest.TestCase().assertNotEqual(actualResult, expectedResult,
                                            f'Failed: Expected "{expectedResult}", but got "{actualResult}"')
        print("Success: Quote verification passed (values are different)!")
    except AssertionError as e:
        print(e)

# assertIs
def test_next_button():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav//a[contains(text(),'Next')]")))
        actualResult = next_button.text
        expectedResult = "none"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")
        unittest.TestCase().assertIs(actualResult,expectedResult,f'Failed:Expected "{expectedResult}",but got "{actualResult}')
        print("Success: Next button test failed!")

        next_button.click()
        print("Success: Next button clicked!")

    except AssertionError as e:
        print(e)

    teardown(driver)

def test_tags():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    try:
        tags = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="tag-item"]/a[@class="tag" and text()="love"]')))
        actualResult = tags.text
        expectedResult = "Viewing tag: love"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")
        unittest.TestCase().assertIsNot(actualResult, expectedResult,
                                     f'Passed:Expected "{expectedResult}",but got "{actualResult}')
        print("Success:assertIsNot ")

    except AssertionError as e:
        print(e)

    teardown(driver)

def test_tag():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    try:
        tag = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="tag-item"]/a[@class="tag" and text()="love"]')))
        actualResult = tag.text
        expectedResult = "Viewing tag: love"
        print(f"Actual Result: {actualResult}")
        print(f"Expected Result:{expectedResult}")
        unittest.TestCase().assertIs(actualResult, expectedResult,
                                     f'Failed:Expected "{expectedResult}",but got "{actualResult}"')
        print("Success:assertIs ")

    except AssertionError as e:
        print(e)

    teardown(driver)















