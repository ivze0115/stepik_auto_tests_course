from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.support.ui import Select

#def calc(x):
    #return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    num1_WebElement = browser.find_element_by_id("num1")
    num1_text = num1_WebElement.text
    num1_int = int(num1_text)
    
    #num1_text = num1.text()
    #print(num1_text)
    #num1_text_value = num1.get_attribute("num1")
    num2_WebElement = browser.find_element_by_id("num2")
    num2_text = num2_WebElement.text
    num2_int = int(num2_text)
    #num2_text = num2.text()
    #num2_text_value = num2.get_attribute("num2")
    calc_num=num1_int + num2_int
    calc_num_text = str(calc_num)
    #print(f'\n\n\n{calc_num}\n\n\n')


    select_required = Select(browser.find_element_by_tag_name("select"))
    select_required.select_by_value(f"{calc_num_text}") # ищем элемент с текстом "Python"
    
    #print(calc_num)
    #treasure_element = browser.find_element_by_id("treasure")
    #x = treasure_element.text
    #print(x)
    #x = treasure_element.get_attribute("valuex")
    #y = calc(int(x))
    #input_field = browser.find_element_by_id("answer")
    #input_field.send_keys(y)
    #for clss in ['form-control']: # required classes
        # also check <input> tag and 'required' attribute.
        #element = browser.find_element_by_css_selector (f'input.{clss}[required]')
        #element.send_keys(y)

    
    #robotCheckbox = browser.find_element_by_id("robotCheckbox")
    #robotCheckbox.click()

    #robotsRule = browser.find_element_by_id("robotsRule")
    #robotsRule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
