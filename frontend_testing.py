from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:\\Users\אלמוג\\Downloads\\chromedriver_win32\\ChromeDriver.exe")
driver.implicitly_wait(5)
driver.get('http:///127.0.0.1:5001/users/2')
try:
    user_name = driver.find_element(By.ID, value='user')
    print(f'the user name on this id : {user_name.text}')
except NoSuchElementException:
    no_user = driver.find_element(By.ID, value='error')
    print(no_user.text)


driver.quit()


