from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (make sure to provide the correct path to your WebDriver)
service = Service(r"C:\Users\zaida\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Open the product page (replace with the actual URL)
    driver.get('https://www.myntra.com/casual-shoes/u.s.+polo+assn./us-polo-assn-men-white-clarkin-sneakers/10339033/buy')

    # Wait until the product title is visible
    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pdp-title'))
    ).text
    print(f'Title: {title}')

    # Extracting the product name
    name = driver.find_element(By.CLASS_NAME, 'pdp-name').text
    print(f'Name: {name}')

    # Extracting the price
    price = driver.find_element(By.CSS_SELECTOR, '.pdp-price strong').text
    print(f'Price: {price}')

    # Extracting the MRP
    mrp = driver.find_element(By.CSS_SELECTOR, '.pdp-mrp').text
    print(f'MRP: {mrp}')

    # Extracting the discount
    discount = driver.find_element(By.CSS_SELECTOR, '.pdp-discount').text
    print(f'Discount: {discount}')

    # Extracting the overall rating
    rating = driver.find_element(By.CSS_SELECTOR, '.index-overallRating > div').text
    print(f'Rating: {rating}')

    # Extracting the ratings count
    ratings_count = driver.find_element(By.CLASS_NAME, 'index-ratingsCount').text
    print(f'Ratings Count: {ratings_count}')

    # Click the "See More" button to reveal additional details
    try:
        see_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'index-showMoreText'))
        )
        see_more_button.click()
        
        # Wait for the new content to load
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'index-rowKey'))  # Adjust as necessary
        )
    except Exception as e:
        print("Could not click 'See More' button:", e)

    # Dictionary to store key-value pairs
    details = {}

    # Finding all key-value pairs
    keys = driver.find_elements(By.CLASS_NAME, 'index-rowKey')
    values = driver.find_elements(By.CLASS_NAME, 'index-rowValue')

    # Loop through keys and values to populate the dictionary
    for key, value in zip(keys, values):
        details[key.text] = value.text

    # Print the collected details
    for key, value in details.items():
        print(f'{key}: {value}')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
