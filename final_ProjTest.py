import time
from tkinter import *
from selenium import webdriver


# changing weekdays into dates assuming it starts from Monday
def dood_API():
    mon_Day = time.strftime("%Y%m%d")
    int_Mon = int(mon_Day)
    int_Tue = int_Mon + 1
    int_Wed = int_Mon + 2
    int_Fri = int_Mon + 4
    str_Tue = str(int_Tue)
    str_Wed = str(int_Wed)
    str_Fri = str(int_Fri)

    # Basic URL from the DoodleAPI and modifying it acc to the required values
    # Change email to shubham143@gmail.com
    browser = webdriver.Chrome()
    basic_url = "http://doodle.com/create?type=date&locale=en&title=Table Tennis Club Practice&name=Shubham Vyas"
    modi_url = basic_url + "&" + str_Tue + "=1130-1300||1730-1900&" + str_Wed + "=1130-1300&" + str_Fri + "=1130-1300&eMailAddress=shubham143%40gmail.com"

    browser.get(modi_url)
    browser.find_element_by_id("initiatorEmail").send_keys("itsRon143@gmail.com")
    browser.find_element_by_id("next1").click()
    browser.find_element_by_id("next2a").click()
    browser.find_element_by_id("next2b").click()
    browser.find_element_by_id("next3s").click()
    browser.find_element_by_id("finish4a").click()


root = Tk()
label = Label(root, text="Click here for Poll", bg="blue", fg="white")
label.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
theButton = Button(bottomFrame, text="Poll", command=dood_API)
theButton.pack()


root.mainloop()

