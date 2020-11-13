from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")


def withdraw(elements):
    try:
        for tempelement in elements:
            driver.execute_script("arguments[0].click();", tempelement)
            # tempelement.click()
            dialog = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn > span"))
            )
            dialog = driver.find_elements_by_css_selector(
                ".artdeco-modal__confirm-dialog-btn > span")
            driver.execute_script("arguments[0].click();", dialog[1])
    except:
        print()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/p/a"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "username"))
    )
    element.send_keys("yourUSERNAME")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "password"))
    )
    element.send_keys("yourPASSWORD")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/main/div[2]/form/div[3]/button"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[8]/div[3]/div/div/div/div/div/div/section/div[2]/div[2]/ul"))
    )
    while(True):
        elements = driver.find_elements_by_css_selector(
            ".artdeco-button--3 > span")
        if(len(elements) > 0):
            withdraw(elements)
        else:
            break

finally:
    print()
