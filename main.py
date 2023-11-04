from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

time.sleep(1)
but_for_accept_private_policy = driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
but_for_accept_private_policy.click()
time.sleep(1)
go_but = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                             '/div[1]/a/span[4]')
go_but.click()
time.sleep(40)

back_to_results_but = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                          '/div[3]/div[3]/div/div[8]/div/a')
back_to_results_but.click()
time.sleep(1)

speed_for_download = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                         '/div[3]/div[3]/div/div[3]/div'
                                                         '/div/div[2]/div[1]/div[1]/div/div[2]/span').text
speed_for_upload = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[3]/div/div[3]/div/div/div[2]'
                                                       '/div[1]/div[2]/div/div[2]/span').text

print(f"Download: {speed_for_download}, Upload: {speed_for_upload}")
