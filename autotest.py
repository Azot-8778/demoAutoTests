from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options

link = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get(link)

time.sleep(5)

def checkBackButton():
    into_card = driver.fid_element(By.CLASS_NAME, "_container_vlg32_23")
    into_card.click()
    time.sleep(5)
    back_to_main_button = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div[5]/div/button/span[2]")
    back_to_main_button.click()

    assert driver.current_url == link, "URL не соответствует главной странице"
    print("passed")

def checkLinePangination():

    forvard_arrow = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[1]/ul/li[9]/button")
    forvard_arrow.click()
    second_page = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item-active")
    assert second_page.get_attribute("title") == "2", "Активная страница не является 2"

    back_arrow = driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div[1]/ul/li[1]/button")
    back_arrow.click()
    first_page = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item-active")
    assert first_page.get_attribute("title") == "1", "Активная страница не является 1"
    print("passed")

checkLinePangination()