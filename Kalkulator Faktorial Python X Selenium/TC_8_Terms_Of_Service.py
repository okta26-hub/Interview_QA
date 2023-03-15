import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_Input(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_input(self):
        # steps
        self.driver.get("https://qa.putraprima.id/") # buka situs
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "body > div > div > div > div:nth-child(2) > a:nth-child(1)").click() # klik button
        time.sleep(3)    
        
        #validasi

        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")
    
    def tearDown(self):
        self.driver.quit() # tutup koneksi socket pada akhir pengujian

if __name__ == "__main__":
    unittest.main()