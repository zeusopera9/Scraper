import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver executable
service = Service(r"C:\Users\Yakshit\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Initialize list to store product details
product_data = []

# Read URLs from file
with open("m_product_urls_sandals.txt", "r") as file:
    urls = [line.strip() for line in file.readlines()]

# Loop through each URL and fetch product details
for url in urls:
    driver.get(url)
    
    try:
        # Give the page some time to load
        time.sleep(5)
        
        # Wait for product title to be visible
        title = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'pdp-title'))
        ).text

        # Extract other product details
        name = driver.find_element(By.CLASS_NAME, 'pdp-name').text
        price = driver.find_element(By.CSS_SELECTOR, '.pdp-price strong').text
        mrp = driver.find_element(By.CSS_SELECTOR, '.pdp-mrp').text
        discount = driver.find_element(By.CSS_SELECTOR, '.pdp-discount').text
        rating = driver.find_element(By.CSS_SELECTOR, '.index-overallRating > div').text
        ratings_count = driver.find_element(By.CLASS_NAME, 'index-ratingsCount').text

        # Extract product description
        description = driver.find_element(By.CLASS_NAME, 'pdp-product-description-content').text

        # Click the "See More" button to reveal additional details
        try:
            see_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'index-showMoreText'))
            )
            see_more_button.click()
            
            # Wait for new content to load
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'index-rowKey'))
            )
        except Exception as e:
            print("Could not click 'See More' button:", e)

        # Dictionary to store key-value pairs of additional details
        details = {
            "Title": title,
            "Name": name,
            "Price": price,
            "MRP": mrp,
            "Discount": discount,
            "Rating": rating,
            "Ratings Count": ratings_count,
            "Description": description  # Adding the description here
        }

        # Extract additional key-value pairs
        keys = driver.find_elements(By.CLASS_NAME, 'index-rowKey')
        values = driver.find_elements(By.CLASS_NAME, 'index-rowValue')
        
        for key, value in zip(keys, values):
            details[key.text] = value.text

        # Append the details to the product data list
        product_data.append(details)

    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

# Close the WebDriver
driver.quit()

# Convert the product data to a DataFrame
df = pd.DataFrame(product_data)

# Save the DataFrame to a CSV file
df.to_csv("m_product_details_sandals.csv", index=False)
print("Product details have been saved to m_product_details_flip_flops.csv.")