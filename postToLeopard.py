from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#input a scratch link and it will post to leopard and return the codesandbox link
def postToLeopard(url):
    # Set up the WebDriver (you may need to download the appropriate driver for your browser)
    driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')  # Change the path to your driver executable

    # Navigate to the website
    driver.get('https://leopardjs.com/')  # Replace with the URL of your target website

    form = driver.find_element_by_css_selector('form.flex')

    # Find the text field and enter the desired text
    text_field = driver.find_element_by_css_selector('input[placeholder="https://scratch.mit.edu/projects/345789566/"]')
    text_field.clear()  # Clear any existing text
    text_field.send_keys(url)  # Enter the desired text

    # Find the button and simulate a button press
    button = form.find_element_by_css_selector('button.bg-indigo-700')
    print("Button text:", button.text)
    button.click() 


    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    # Wait for the page to redirect and retrieve the redirected URL
    redirected_url = driver.current_url
    print("Redirected URL:", redirected_url)

    # Optionally, you can further interact with the redirected page or perform additional actions

    # Close the browser
    driver.quit()
    return redirected_url

if __name__ == "__main__":
    postToLeopard('https://scratch.mit.edu/projects/861175147/')