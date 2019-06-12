from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tenhou.net/2/?q=238m1679p12349s3z4m")
textarea = driver.find_element_by_tag_name("textarea")
print(textarea.text)
