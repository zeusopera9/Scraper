from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize the window

# Initialize WebDriver (replace "path/to/chromedriver" with actual path)
driver = webdriver.Chrome(service=Service(r"C:\Users\zaida\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"), options=options)

# URL of the Myntra category page
url = "https://www.myntra.com/men-sneakers"
driver.get(url)

# Scroll and load more items
for _ in range(5):  # Adjust the range depending on how many products you want
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait to load new items

# Scraping the shoe data
shoes_data = []

# Wait until the products are loaded
wait = WebDriverWait(driver, 10)
products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.product-base")))

for product in products:
    try:
        brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
        name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text
        price = product.find_element(By.CSS_SELECTOR, "div.product-price span").text
        shoes_data.append({"brand": brand, "name": name, "price": price})
    except Exception as e:
        print("Error fetching product details:", e)

# Close the WebDriver
driver.quit()

# Display the scraped data
for shoe in shoes_data:
    print(shoe)
