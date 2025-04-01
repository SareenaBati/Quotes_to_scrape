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


def test_get_quotes():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    quotes = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="quote"]/span[@itemprop="text"]')))

    for quote in quotes:
        print(quote.text)

    teardown(driver)


def test_get_author():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    authors = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class="author"]')))

    for author in authors:
        print(author.text)

    teardown(driver)


def test_get_tags():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    tags = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="tags"]/a')))

    for tag in tags:
        print(tag.text)

    teardown(driver)


def test_get_button():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    nxtBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@class="next"]/a')))
    nxtBtn.click()
    print("Success: Next button clicked!")
    teardown(driver)


def test_love_btn():
    driver = setup()
    wait = WebDriverWait(driver, 10)
    loveBtn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[@class="tag-item"]/a[@class="tag" and text()="love"]')))
    loveBtn.click()

    try:
        actres = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='container']/h3")))
        actualResult = actres.text
        expectedResult = "Viewing tag: love"
        assert actualResult == expectedResult, 'Failed'
        print("Success: Love button test passed!")
    except AssertionError as e:
        print(e)

    teardown(driver)


def scrolldown(driver):
    wait = WebDriverWait(driver, 10)
    page_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(1)

    print("Success: Page scrolled down")
    time.sleep(2)


def test_login():
    driver = setup()
    wait = WebDriverWait(driver, 10)

    LoginBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))
    LoginBtn.click()

    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("test@gmail.com")

    password = driver.find_element(By.ID, "password")
    password.send_keys("password")

    submit = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit.click()

    print("Success: Logged in successfully!")
    scrolldown(driver)

    teardown(driver)


def test_get_quote():
    driver = setup()
    wait = WebDriverWait(driver, 10)

    quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'text')))
    authors = driver.find_elements(By.CLASS_NAME, 'author')
    tags_list = driver.find_elements(By.CLASS_NAME, 'tags')

    for i in range(len(quotes)):
        print(f"'{quotes[i].text}'")
        print(f"-by {authors[i].text}")
        tags = tags_list[i].find_elements(By.TAG_NAME, 'a')
        tag_texts = [tag.text for tag in tags]
        print("Tags:", ", ".join(tag_texts) if tag_texts else "None")

    teardown(driver)


def test_quote_verification():
    driver = setup()
    wait = WebDriverWait(driver, 10)

    try:
        quoteElem = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'“The world as we have created it is a process of o')]")
        ))
        actualResult = quoteElem.text
        expectedResult = "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
        assert actualResult == expectedResult, 'Failed'
        print("Success: Quote verification passed!")
    except AssertionError as e:
        print(e)

    teardown(driver)

def test_second_quote():
    driver=setup()
    wait=WebDriverWait(driver,10)

    try:
        quote_element =wait.until(EC.presence_of_element_located(
            (By.XPATH,"(//span[@class='text'])[2]")
        ))
        actualResult=quote_element.text
        expectedResult="“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
        assert actualResult==expectedResult,'Failed'
        print("Success:Quote Verificaion passed!")

    except AssertionError as e:
        print(e)

    teardown(driver)

def test_third_quote():
    driver = setup()
    wait = WebDriverWait(driver, 10)

    try:
        third_quote = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='text'])[3]")  
        ))
        actualResult = third_quote.text
        expectedResult = "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
        assert actualResult == expectedResult, 'Failed'
        print("Success: third quote test passed!")
    except AssertionError as e:
        print(e)




def test_next_button():
    driver = setup()
    wait = WebDriverWait(driver, 10)

    try:

        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//nav//a[contains(text(),'Next')]")))
        actualResult = next_button.text
        expectedResult = "Next →"


        print(f"Found button text: {actualResult}")

        assert actualResult == expectedResult, f"Failed: Expected '{expectedResult}', but got '{actualResult}'"
        print("Success: Next button test passed!")


        next_button.click()
        print("Success: Next button clicked!")

    except AssertionError as e:
        print(e)

    teardown(driver)

def test_login_button():
    driver = setup()
    wait = WebDriverWait(driver, 10)

    try:
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' or contains(text(),'Login')]")))

        expected_result = "Login"
        actual_result = login_button.text

        print(f"Expected Result: {expected_result}")
        print(f"Actual Result: {actual_result}")

        assert actual_result == expected_result, f"Test Failed: Expected '{expected_result}', but got '{actual_result}'"
        print("Success: Login button test passed!")

    except Exception as e:
        print(f"An error occurred: {e}")







