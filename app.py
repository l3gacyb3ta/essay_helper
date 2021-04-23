from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib.parse

options = webdriver.ChromeOptions()
options.add_argument('window-size=1200x600')
options.add_argument("--no-sandbox");
options.add_argument("--disable-dev-shm-usage");
driver = webdriver.Chrome(chrome_options=options)

essay = open('essay.txt','r').read()
images = []
def get_image(term):
    driver.get('https://images.google.com/search?q='+term+'&tbm=isch')


    img = driver.find_element(By.CSS_SELECTOR, '.islrc > .isv-r:nth-child(1) .rg_i')
    img.click()
    img2 = driver.find_element(By.CSS_SELECTOR, '.tvh9oe:nth-child(2) .n3VNCb')

    return(img2.get_attribute('src'))

essay = urllib.parse.quote(essay, safe='')

searches = essay.split(".")

for search in searches:
    images.append(get_image(search))

open('images.txt', 'w').writelines(images)
