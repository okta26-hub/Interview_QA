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
        self.driver.find_element(By.CSS_SELECTOR, "#input").send_keys("+10") # isi angka
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#hitung").click() # klik button
        time.sleep(5)    
        
        #validasi

        expected_result = "Faktorial dari +10 adalah: 3628800"
        actual_result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(actual_result, expected_result, msg="Hasil tidak sesuai dengan harapan")
        print("Hasil Testing Sesuai Dengan Test Case Yang Dikerjakan")

    def tearDown(self):
        self.driver.quit() # tutup koneksi socket pada akhir pengujian
        
if __name__ == "__main__":
    unittest.main()