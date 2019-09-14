from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_post(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag)
        time.sleep(3)
        for i in range (1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            postLinks = [i.get_attribute('href')
                          for i in bot.find_elements_by_xpath("//a[@href]")]#Looking for all the element where they have an Anchor tag
            filteredLinks = list(filter(lambda x: '/p/' in x, postLinks))
            print(filteredLinks)
            for link in filteredLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//span[@aria-label='Like']").click()
                    time.sleep(15)
                except Exception as ex:
                    time.sleep()

run = InstagramBot('Your_Phone','Your_Password') #email and password respectively
run.login()
run.like_post('cake') #your Desired Hastag