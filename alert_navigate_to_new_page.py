from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import os
#from selenium.webdriver.support.ui import Select



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(calc(x))

    #input1 = browser.find_element_by_name("firstname")
    #input1.send_keys("Ivan")
    #input1 = browser.find_element_by_name("first_name")
    #input1.send_keys("Ivan")
    #input2 = browser.find_element_by_name("lastname")
    #input2.send_keys("Sirko")
    #input3 = browser.find_element_by_name("email")
    #input3.send_keys("ivan@i.ua")

    #file_element = browser.find_element_by_name("file")

    #current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    #file_path = os.path.join(current_dir, 'result1.txt')           # добавляем к этому пути имя файла 
    #file_element.send_keys(file_path)
    
    #input3 = browser.find_element_by_class_name("form-control.city")
    #input3.send_keys("Sumy")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Ukraine")
    
    answer_WebElement = browser.find_element_by_id("answer")
    answer_WebElement.send_keys(y)
    '''
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()
    
    #print(f'\n\n\n{calc_num}\n\n\n')


    #select_required = Select(browser.find_element_by_tag_name("select"))
    #select_required.select_by_value(f"{calc_num_text}") # ищем элемент с текстом "Python"
 
    '''
    button2 = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button2.click()

    time.sleep(5)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
