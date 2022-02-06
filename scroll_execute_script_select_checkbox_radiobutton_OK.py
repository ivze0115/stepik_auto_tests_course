from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(calc(x))

    answer_WebElement = browser.find_element_by_id("answer")
    answer_WebElement.send_keys(y)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()
    
    #print(f'\n\n\n{calc_num}\n\n\n')


    #select_required = Select(browser.find_element_by_tag_name("select"))
    #select_required.select_by_value(f"{calc_num_text}") # ищем элемент с текстом "Python"
 

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(5)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
