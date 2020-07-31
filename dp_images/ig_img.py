from selenium import  webdriver
from selenium.webdriver.firefox.options import  Options
from time import  sleep
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
options = Options()
options.headless = True
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(executable_path= "path-to-firefox driver",options= options)
url = "https://www.instadp.com"

print("Waiting for the username!")
driver.get(url)
try:
    user_name = input("Enter the username properly: ")
    search_bar = driver.find_element_by_xpath("/html/body/header/div/div[1]").click()
    search_bar_click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/input")
    search_bar_click.send_keys(user_name)
    search_bar_click.send_keys(Keys.ENTER)
    sleep(5)
    profile = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul[2]/li[1]/a").click()
    sleep(4)
    full_size = driver.find_element_by_xpath("/html/body/article/div[2]/ul/li[2]").click()
    sleep(2)
    download_button = driver.find_element_by_xpath("/html/body/article/div[2]/section[2]/div[5]/a[1]/img").click()
    #optional to download images
    # driver.save_screenshot("file.png")
    try:
        sleep(5)
        url_img = driver.find_element_by_xpath('//*[@id="iv-container"]/div[6]/div/img').get_attribute("src")
        path = "path/dp_images/saved_images" # if not make a directory saved_images
        try:
            if not os.listdir(path):
                urllib.request.urlretrieve(url_img, f"saved_images/{user_name}.jpg")
                print("Image Saved")
                driver.close()
                exit()
            else:
                for img in os.listdir(path):
                    if f"{user_name}.jpg" != img :
                        urllib.request.urlretrieve(url_img, f"saved_images/{user_name}.jpg")
                        print("Image saved")
                        driver.close()
                        exit()
                    else:
                        print(f"Image {user_name} exits")
                        driver.close()
                        exit()
        except Exception:
            print("something went wrong in downloading image")
            driver.close()
            exit()
        
    except  Exception:
        print(f"Cannot download the image: {user_name}")
        driver.close()
        exit()

except Exception:
    print("Something wrong in fetching username or with website")
    driver.quit()
    exit()