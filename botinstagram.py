from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Executar no CMD "pip install packaging" quando der erro nos imports de packaging


class InstagramBot:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.username = username
        self.password = password

    def login(self):
        dr = self.driver
        dr.get("https://www.instagram.com")
        dr.implicitly_wait(10)
        el_user = dr.find_element(
            by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        el_user.clear()
        el_user.send_keys(self.username)
        el_pass = dr.find_element(
            by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        el_pass.clear()
        el_pass.send_keys(self.password)
        el_btnLogin = dr.find_element(
            by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button'
        )
        el_btnLogin.click()
        time.sleep(5)
        self.getPosts("tecnologia")

    def getPosts(self, hashtag):
        dr = self.driver
        try:
            dr.get("https://www.instagram.com/explore/tags/" + hashtag)
        except:
            Exception
        time.sleep(5)
        listTags = []
        for i in range(1, 10):
            self.scrollPage()
            elements = dr.find_elements(by=By.TAG_NAME, value="a")
            if len(elements) > 59:
                for tag in elements:
                    listTags.append(tag)
        time.sleep(5)
        self.filterPosts(listTags)

    def scrollPage(self):
        dr = self.driver
        for count in range(0, 4):
            dr.execute_script(
                "window.scrollTo(document.body.scrollTop, document.body.scrollHeight)"
            )
            time.sleep(2)
            dr.execute_script(
                "window.scrollTo(document.body.scrollHeight, document.body.scrollTop)"
            )

    def filterPosts(self, listTags):
        dr = self.driver
        listPosts = []

        for atr in listTags:
            try:
                item = atr.get_attribute("href")
                if item.__contains__("https://www.instagram.com/p/"):
                    listPosts.append(item)
            except:
                Exception

        time.sleep(5)
        self.likePosts(listPosts)

    def likePosts(self, posts):
        dr = self.driver
        count = 0
        for post in posts:
            if count < 200:
                try:
                    dr.get(post)
                    time.sleep(5)
                    el_btnPost = dr.find_elements(by=By.CLASS_NAME, value="_abl-")
                    el_btnPost[1].click()  # click curtir
                    time.sleep(3)
                    count += 1
                    print("Curtidas: " + count)
                    time.sleep(20)
                except:
                    Exception

    def newComment(self):
        dr = self.driver
        try:
            el_comment = dr.find_element(by=By.TAG_NAME, value="textarea")
            el_comment.send_keys("")
            el_btnSendComment = dr.find_element(
                by=By.XPATH,
                value='//*[@id="mount_0_0_g0"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div[2]/button',
            )
            el_btnSendComment.click()
        except:
            Exception


instaBot = InstagramBot("USERNAME", "PASSWROD")
instaBot.login()
