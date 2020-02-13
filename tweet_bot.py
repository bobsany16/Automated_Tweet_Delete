from selenium import webdriver
from time import sleep
from secrets import username, password

class TwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://twitter.com')
   
        sleep(2)

        #To log in
        fb_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
        fb_btn.click()

        #username in 
        username_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label')
        username_in.send_keys(username)
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label')
        pw_in.send_keys(password)

        log_in_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        log_in_btn.click()

        

    """
    def toProfile(self):
        profile_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[2]/nav/a[7]/div/div/div/div[2]/div/div')
        profile_button.click()

        twt_reply = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/nav/div[2]/div[2]/a')
        twt_reply.click()"""
    
    def toTweet(self, string):

        #tweet_option = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[3]')

        to_write = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div')
        to_write.send_keys(string)

        sleep(2)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[2]/div/div/div/div[3]/div')
        tweet.click()
    
    """
    def deleteTweet(self):
        arrow_down = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[15]/div/article/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div')
        arrow_down.click()"""
myBot = TwitterBot()
myBot.login()
