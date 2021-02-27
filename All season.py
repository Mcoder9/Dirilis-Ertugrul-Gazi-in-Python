'''
******For dirilis ertugrul lovers*****
This is scraper and it will scrap all the Title, Links and Passwords of the vedios

Note:
it's for only DIRILIS ERTUGRUL ALL SEASONS IN URDU WITH URDU SUBTITLES. If you want to scrap krulas usman season check my github repository.

******Thank you**********
'''

# Import required modules
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Webdriver browser setup (Chrome and Firefox both can be used)
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
print('''Select a browser to perform. Chrome & Firefox both are available.
    1> Chrome
    2> Firefox
    ''')
browser = int(input('>'))
if browser == 1:
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == 2:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Give the correct path of %s' % browser)

print('''DIRILIS ERTUGRUL ALL SEASONS IN URDU SUBTITLES
    1> Season One
    2> Season Two
    3> Season Three
    4> Season Four
    5> Season Five
    6> All
    ''')

season = int(input('Select season number: '))
data = []


def season_01():
    print('Season 01 Started')
    url = 'https://dailyurdupoetry.com/dirilis-ertugrul-season-1-in-urdu-episode-1-giveme5/'
    for i in range(2,78):
        driver.get(url)
        title = driver.find_element_by_css_selector('h1 span.post-title').text
        link = driver.find_element(By.CSS_SELECTOR, "div.tab-pane iframe").get_attribute('src')
        print(f'{title}\n{link}')
        print('*****************'.center(50))
        url = f'https://dailyurdupoetry.com/dirilis-ertugrul-season-1-in-urdu-episode-{i}-giveme5/'
        data.append([title,link])
    df = pd.DataFrame(data,columns=["Title","Link"])
    df.to_csv('season_01.csv')
    print('Season 01 Ended')

def season_02():
    print('Season 02 Started')
    url = 'https://dailyurdupoetry.com/dirilis-ertugrul-season-2-in-urdu-episode-1-giveme5/'
    for i in range(2,106):
        driver.get(url)
        title = driver.find_element_by_css_selector('h1 span.post-title').text
        link = driver.find_element(By.CSS_SELECTOR, "div.tab-pane iframe").get_attribute('src')
        print(f'{title}\n{link}')
        print('*****************'.center(50))
        url = f'https://dailyurdupoetry.com/dirilis-ertugrul-season-2-in-urdu-episode-{i}-giveme5/'
        data.append([title,link])
    df = pd.DataFrame(data,columns=["Title","Link"])
    df.to_csv('season_02.csv')
    print('Season 02 Ended')

def season_03():
    print('Season 03 Started')
    url = 'https://www.giveme5.tv/dirilis-season-3-urdu/epi-01s3'
    for i in range(2,51):
        driver.get(url)
        driver.implicitly_wait(10)
        title = driver.find_element_by_css_selector('#comp-kc8k65by span span').text
        _pass = driver.find_element_by_css_selector('#comp-kc8k65ic span span').text.split(':')[1]
        part1 = driver.find_element_by_css_selector('div#comp-kl8zd75v a').get_attribute('href')
        part2 = driver.find_element_by_css_selector('div#comp-kl8zh6w1 a').get_attribute('href')
        print(f'{title}\nPart 01: {part1}\nPart 02: {part2}\nPassword: {_pass}')

        if i<=9:
            url=f'https://www.giveme5.tv/dirilis-season-3-urdu/epi-0{i}s3'
        else:
            url=f'https://www.giveme5.tv/dirilis-season-3-urdu/epi-{i}s3'
        data.append([title,part1,part2,_pass])
    df = pd.DataFrame(data,columns=['Title','Part 01','Part 02','Password'])
    df.to_csv('season_03.csv')
    print('Season 03 Ended')

def season_04():
    print('Season 04 Started')
    url = 'https://www.giveme5.tv/dirilis-season-4-urdu/epi-01s4'
    for i in range(2,62):
        driver.get(url)
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
            driver.find_element_by_xpath("//input[@class='np_ViewPassword-input ']").send_keys(_pass)
            driver.find_element(By.XPATH,"//input[@class='np_ViewPassword-submit']").click()
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
        data.append([title, link, _pass])
    df = pd.DataFrame(data,columns=['Title','Link','Pass'])
    df.to_csv('season_04.csv')
    print('Season 04 Ended')

def season_05():
    print('Season 05 Started')
    def part_02():
        driver.switch_to.default_content()
        # Scroll to the iframe
        action = ActionChains(driver)
        scroll = driver.find_element_by_css_selector('span._3fUtn')
        action.move_to_element(scroll).perform()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "div#comp-kbs163ey iframe")))
        try:
            driver.find_element_by_css_selector("input.np_ViewPassword-input ").send_keys(psw)
            driver.find_element(By.CSS_SELECTOR,"input.np_ViewPassword-submit").click()
        except :
            pass
        try:
            link2 = driver.find_element_by_css_selector('p.np_AlertdialogError-text a').get_attribute('href')
        # Get iframe sorce link if vedio link is unavailable
        except:
            driver.switch_to.default_content()
            link2 = driver.find_element_by_css_selector('div#comp-kbs163ey iframe').get_attribute('src')
        print('Part 02: ',link2)

    def part_01():
        url = 'https://www.giveme5.tv/dirilis-season-5-urdu/epi-01s5'
        for i in range(2,60):
            driver.get(url)
            driver.implicitly_wait(5)
            title = driver.find_element_by_css_selector('div#comp-kbs0zvuj').text
            parts = title.split('(')[-1].replace(')','')
            psw = driver.find_element_by_css_selector('#comp-kbs26rv3 span>span').text.split()[-1]

            # Scroll to the iframe
            action = ActionChains(driver)
            scroll = driver.find_element_by_css_selector('#comp-kbs26rv3 span>span')
            action.move_to_element(scroll).perform()

            wait = WebDriverWait(driver, 10)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='Dailymotion video player']")))


            # Apply and submit password if vedio protected
            try:
                driver.find_element_by_css_selector("input.np_ViewPassword-input ").send_keys(psw)
                driver.find_element(By.CSS_SELECTOR,"input.np_ViewPassword-submit").click()
            except :
                pass

            # Get Link of vedio
            try:
                link = driver.find_element_by_css_selector('p.np_AlertdialogError-text a').get_attribute('href')
            # Get iframe sorce link if vedio link is unavailable
            except:
                driver.switch_to.default_content()
                link = driver.find_element_by_css_selector('div#comp-kbtujaxh iframe').get_attribute('src')

            print(f'{title}\n{link}\nPassword: {psw}')
            if parts.lower() == 'two parts':
                part_02()

            print('*****************'.center(50))

            if i<=9:
                url=f'https://www.giveme5.tv/dirilis-season-5-urdu/epi-0{i}s5'
            else:
                url=f'https://www.giveme5.tv/dirilis-season-5-urdu/epi-{i}s5'
    part_01()
    print('Season 05 Ended')


if season == 1: season_01()
elif season == 2: season_02()
elif season == 3: season_03()
elif season == 4: season_04()
elif season == 5: season_05()
else:
    season_01(),season_02(),season_03(),season_04(),season_05()

driver.quit()
