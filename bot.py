from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox() #webdriver for Firefox used

        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(5)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')  #to scroll down
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('') for elem in tweets]
            print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_css_selector(
                        'button[class="ProfileTweet-actionButton js-actionButton js-actionFavorite"]').click()
                    time.sleep(10)
                except Exception as ex:
                    print("Error")
                    time.sleep(20)

tb = TwitterBot('','') #enter your twitter email and password
tb.login()
tb.like_tweet('')#enter the topic you want the bot to browse and like tweets from
