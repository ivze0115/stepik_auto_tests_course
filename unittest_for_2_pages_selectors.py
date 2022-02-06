import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestSuccessfullRegistration_link2(unittest.TestCase):
    def test_successfull_registration_for_page_2(self):
        try:
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
            self.browser.get(link2)


            self.first_name = self.browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
            self.first_name.send_keys("Test")
            self.last_name = self.browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
            self.last_name.send_keys("Test")
            self.email = self.browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
            self.email.send_keys("test@i.ua")

            self.button = self.browser.find_element_by_css_selector("button.btn")
            self.button.click()

            #time.sleep(10)

        # находим элемент, содержащий текст
            self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
            self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(self.welcome_text, "Congratulations! You have successfully registered!", "Should be equal")


        finally:
            self.browser.quit()

class TestSuccessfullRegistration_link1(unittest.TestCase):
    def test_successfull_registration_for_page_1(self):
        try:
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
            self.browser.get(link1)


            self.first_name = self.browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
            self.first_name.send_keys("Test")
            self.last_name = self.browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
            self.last_name.send_keys("Test")
            self.email = self.browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
            self.email.send_keys("test@i.ua")
            

            self.button = self.browser.find_element_by_css_selector("button.btn")
            self.button.click()
            

            #time.sleep(20)

        # находим элемент, содержащий текст
            self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
            self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(self.welcome_text, "Congratulations! You have successfully registered!", "Should be equal")
  

        finally:
            self.browser.quit()





if __name__=="__main__":
    unittest.main()
