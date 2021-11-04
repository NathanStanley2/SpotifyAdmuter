from selenium import webdriver
import time
import muter # import other file
#YOUTUBE VERSION
#LAUNCH THIS FILE TO START

# video that always gets an ad https://www.youtube.com/watch?v=nPw5pDTuwPw #football #with ad does mute

# video that does not get an ad https://www.youtube.com/watch?v=L_LUpnjgPso

#ytp-ad-player-overlay - youtube's class html ad

#bugs - SMALL - if not window open, crashes on check, on UI have if x is hit, close program


path = "C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(path)

browser.get("https://www.youtube.com/")

time.sleep(5) #needed otherwise it doesn't see the ad


#print(browser.current_url) use for checking if on youtube if url contatins youtube,

def main():

   # time.sleep(5)

    search = browser.find_elements_by_class_name("ytp-ad-player-overlay") #class way #breaks here when no window
    #print(search)

    if search != []:
        muter.volume_muter()
        #print("mute for x time")
        time.sleep(3)
        main() #check for ad again after sleep
    else:
        muter.volume_unmuter()
        #print("no ad no mute")
        time.sleep(3)
        main()

if __name__ == '__main__':
    main()

