from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Specify the path to the ChromeDriver executable
service = Service(r"C:\Users\zaida\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open the Myntra sneakers page
driver.get("https://www.myntra.com/school-shoes?plaEnabled=false")

# Initialize an empty list to store product URLs
all_product_urls = []

# Number of pages to search
numPages = 20

# Loop to go through multiple pages
for page in range(numPages):  # Change this to the desired number of pages
    # Give time for the page to load
    time.sleep(5)  # You can adjust this if needed

    # Find all product elements on the current page
    product_elements = driver.find_elements(By.XPATH, "//li[contains(@class, 'product-base')]//a")

    # Extract URLs from the product elements and add to the list
    product_urls = [element.get_attribute('href') for element in product_elements]
    all_product_urls.extend(product_urls)  # Add to the main list

    # Try to click the "Next" button to go to the next page
    try:
        next_button = driver.find_element(By.XPATH, "//li[contains(@class, 'pagination-next')]//span[contains(@class, 'pagination-arrowRight')]")
        next_button.click()  # Click the "Next" button
    except Exception as e:
        print(f"Error navigating to next page: {e}")
        break  # Exit the loop if the "Next" button is not found

# Save all collected product URLs to a text file
with open("k_product_urls_school_shoes.txt", "w") as file:
    for url in all_product_urls:
        file.write(url + "\n")  # Write each URL on a new line

# Optionally, print the collected URLs
print("Collected Product URLs:")
for url in all_product_urls:
    print(url)

# Close the driver
driver.quit()
