import selenium
import time
import vlc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import getpass


def main():
    # get user credentials
    user = input("MSU netid: ")
    userpass = getpass.getpass(prompt = "Password: ")

    # open chrome driver
    driver = webdriver.Chrome()
    driver.get("https://schedule.msu.edu/Planner.aspx")
    assert "MSU" in driver.title

    # enter in username
    username = driver.find_element_by_id("netid")
    username.clear()
    username.send_keys(user)
    
    # enter in password
    password = driver.find_element_by_id("pswd")
    password.clear()
    password.send_keys(userpass)

    # submit
    driver.find_element_by_name("submit").click()

    # get audio file path
    wd = os.path.dirname(os.path.realpath(__file__))
    audioFile = wd + "\\beep-01a.mp3"

    # find open course
    while True:
        if ("Planned - Open" in driver.page_source):
            for i in range(5):
                p = vlc.MediaPlayer(audioFile)
                p.play()
                time.sleep(2)
            print("found")
        time.sleep(15)
        driver.refresh()

        

if __name__ == "__main__":
    main();