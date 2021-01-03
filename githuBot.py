from sıgnIn import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Github:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.search = 'SelmanKahya'  # Takipçi isimlerini almak istediğin kullanıcı
        self.browser = webdriver.Chrome(executable_path='C:/Users/Oğuzhan/Desktop/SeleniumDrivers/chromedriver.exe')
        self.liste = []
        self.max_Followers = 150  #Takipçi listesinden almak istediğin takipçi sayısı

    def Sıgn(self):
        self.browser.get('https://github.com/login')
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]').send_keys(self.search,Keys.ENTER)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[2]/nav[1]/a[10]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="user_search_results"]/div/div[1]/div[2]/div[1]/div[1]/a[1]').click()
        time.sleep(2)

    def follow(self):
        users = self.browser.find_elements_by_css_selector('.d-inline-block.no-underline.mb-1 .link-gray')
        for id in users:
            self.liste.append(id.text)

    def Followers(self):
        self.browser.get(f'https://github.com/{self.search}?tab=followers')
        time.sleep(2)
        self.follow()

        while True:
            if len(self.liste)<self.max_Followers:
                links = self.browser.find_element_by_class_name('pagination').find_elements_by_tag_name('a')
                if len(links) == 1:
                    if links[0].text =='Next':
                        links[0].click()
                        time.sleep(1)
                        self.follow()
                    else:
                        break
                else:
                    for link in links:
                        if link.text == 'Next':
                            link.click()
                            time.sleep(1)
                            self.follow()
                        else:
                            continue
            else:
                break
        self.browser.close()

git = Github(username,password)
git.Sıgn()
git.Followers()
print(f"Followers : {len(git.liste)} , Followers Nick :\n{git.liste}")