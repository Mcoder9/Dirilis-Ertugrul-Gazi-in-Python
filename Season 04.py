'''
******For dirilis ertugrul lovers*****
This is scraper and it will scrap all the Title, Links and Passwords of the vedios

Note:
it for only season 4 with urdu subtitles. If you want to scrap other season check my github repository

******Thank you**********
'''



# Import required modules
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Webdriver browser setup (Chrome and Firefox both can be used)
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
browser = 'chrome'
if browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Give the correct path of %s' % browser)



url = 'https://www.giveme5.tv/dirilis-season-4-urdu/epi-01s4'
for i in range(2,62):
    driver.get(url)
    driver.implicitly_wait(10)
    # Get title of the vedio
    title = driver.find_element_by_css_selector('#comp-kc2t81ve span > span').text
    # Get password of the vedio
    _pass = driver.find_element_by_css_selector('#comp-kc2t81wh1 span>span').text.split()[1]

    # Scroll to the iframe
    scroll = driver.find_element_by_css_selector('#comp-kc2t81wh1 span>span')
    action = ActionChains(driver)
    action.move_to_element(scroll).perform()

    # Wait for iframe to be load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='Dailymotion video player']")))

    # Apply and submit password if vedio protected
    try:
        send_pass = driver.find_element_by_xpath("//input[@class='np_ViewPassword-input ']").send_keys(_pass)
        submit = driver.find_element(By.XPATH,"//input[@class='np_ViewPassword-submit']").click()
    except :
        pass

    # Get Link of vedio
    try:
        link = driver.find_element_by_css_selector('p.np_AlertdialogError-text>a').get_attribute('href')
    # Get iframe sorce link if vedio link is unavailable
    except:
        driver.switch_to.default_content()
        link = driver.find_element_by_css_selector('.VideoPlayer34179784__playerContainer > iframe').get_attribute('src')

    print(f'{title}\n{link}\nPassword: {_pass}')
    print('*****************'.center(50))

    # Urls for next episode
    if i<=9:
        url=f'https://www.giveme5.tv/dirilis-season-4-urdu/epi-0{i}s4'
    else:
        url=f'https://www.giveme5.tv/dirilis-season-4-urdu/epi-{i}s4'
