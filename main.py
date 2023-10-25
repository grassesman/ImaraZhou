from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.options import Options
import time

start = time.time()
my_dict = {
    "url": "https://neworld.cloud/auth/login",
    "username": "3378096510@qq.com",
    "username_xpath": "//*[@id='email']",
    "password": "imarazhou123",
    "password_xpath": "//*[@id='passwd']",
    "submit_button_xpath": "//*[@id='login-dashboard']",
    "check_in_button_xpath": "//*[@id='check-in']",
    "txt_path": "config.txt"
}

# 打开文件，使用 'r' 模式表示只读
file_path = my_dict["txt_path"]
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"文件 '{file_path}' 不存在")

# 打开文件以写入文本，如果文件不存在将创建它
with open('existing_file.txt', 'a') as file:
    file.write('\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# update dict
my_dict.update({"username": lines[0], "password": lines[1]})

# 创建Chrome浏览器的选项对象
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options=chrome_options)

# 打开网页
driver = webdriver.Chrome()
driver.maximize_window()
# 登录OA
driver.implicitly_wait(3)
driver.get(my_dict["url"])

# login
driver.find_element(By.XPATH, my_dict["username_xpath"]).send_keys(my_dict["username"])
driver.find_element(By.XPATH, my_dict["password_xpath"]).send_keys(my_dict["password"])
driver.find_element(By.XPATH, my_dict["submit_button_xpath"]).click()
time.sleep(2)
with open('existing_file.txt', 'a', encoding='utf-8') as file:
    file.write("\n" + "已登录")
try:
    driver.find_element(By.XPATH, my_dict["check_in_button_xpath"]).click()
    with open('existing_file.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + "已签到")
except Exception:
    with open('existing_file.txt', 'a', encoding='utf-8') as file:
        file.write("\n" + "异常")

driver.quit()
end = time.time()

print('执行耗时：%s s' % (end - start))
