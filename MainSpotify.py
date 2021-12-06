from selenium import webdriver
import time
import muter # import other file
#Spotify VERSION
#LAUNCH THIS FILE TO START


path = "C:\Program Files (x86)\chromedriver.exe" #make sure this is the path that you are using for Selenium Chromedriver

browser = webdriver.Chrome(path)

browser.get("https://open.spotify.com/") #spotify web player

time.sleep(5) #needed otherwise it doesn't see the ad


def main():
    x = 0

    while x == 0:
        search = browser.find_elements_by_class_name("KmNp5hmZdIJVfnAZBfu8")

        if search != []:
            muter.volume_muter()
            time.sleep(3)
        else:
            muter.volume_unmuter()
            time.sleep(3)

if __name__ == '__main__':
    main()

