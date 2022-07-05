import pymysql
from selenium.common import NoSuchElementException

import db_connector as dba
from selenium import webdriver
from selenium.webdriver.common.by import By

db = pymysql.connect(host='remotemysql.com', port=3306, user='AEfWGNA9zC', password='g0PRYTjC6R', db='AEfWGNA9zC')
cur = db.cursor()
db.autocommit(True)

table = dba.Msql(table='config')
print(dba.Msql.select_all(table))

def browser(row):               # enter the row number to get the browser type
    inf = dba.Msql.select_all(table)
    brow = inf[row][1]
    return brow

def gateway(row):
    inf = dba.Msql.select_all(table)
    gate = inf[row][0]
    return gate


from_config_table = 2           # please choose the row from "config" table that you want
from_main_table = 5             # please choose the user id from "users" table that you want to insert
user_name = ''
if browser(from_config_table) == 'Chrome':
    driver = webdriver.Chrome( executable_path="C:\\Users\אלמוג\\Downloads\\chromedriver_win32\\ChromeDriver.exe")
    driver.implicitly_wait(5)
    url = str(f'http://{gateway(from_config_table)}/{from_main_table}')
    driver.get(url)
    try:
        user_name = driver.find_element(By.ID, value='user')
        print(f'the user name on this id : {user_name.text}')
    except NoSuchElementException:
        no_user = driver.find_element(By.ID, value='error')
        print(no_user.text)


    cur.execute(f"update AEfWGNA9zC.config set user_name = '{user_name.text}', creation_date = current_timestamp where id = '{from_config_table}'")
    print({f'config table is update where id = {from_config_table}': dba.Msql.select_all(table)[(from_config_table-1)]})
    driver.quit()

