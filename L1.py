import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Класс тестового примера наследуется от unittest.TestCase .
class PO(unittest.TestCase):
    
    #создаем экземпляр Chrome WebDriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    #Открываем и ищем элемент. Метод тестового примера всегда должен начинаться с символов test 
    def test_up(self):
        driver = self.driver
        link = "http://suninjuly.github.io/simple_form_find_task.html"
        driver.get(link)
        elem = driver.find_element(By.ID, "submit_button")

    #Закрываем браузер
    def tearDown(self):
        self.driver.quit()    

#шаблонный код для запуска набора тестов:
if __name__ == "__main__":
    unittest.main()