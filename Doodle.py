from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

def doodle():
    name = "Rounak Vyas"  # input("Name: \n")
    email = "rounakv1@gmail.com"  # input("Email: \n")
    eventTitle = "sdfsd"  # input("Event Title: \n")
    description = "waedawsd"  # input("Description: \n")
    location = "asdas"  # input("Location: \n")
    fromDate = "20170617"  # input("Date(Day 1): \n")
    _time = "1200-1300"  # input("Time Interval: \n")
    _time2 = "1300-1500"  # input("Time Interval(2): \n")
    fromDate2 = "20170618"  # input("Date(Day 2): \n")
    _dtime = "1300-1900"  # input("Time Interval: \n")
    _dtime2 = "1400-1900"  # input("Time Interval(2, Optional): \n")
    fromDate3 = "20170619"  # input("Date(Day 3): \n")
    _ddtime = "1300-1900"  # input("Time Interval: \n")
    _ddtime2 = "1400-1800"  # input("Time Interval(2, Optional): \n")
    
    doodUrl = "http://doodle.com/create?type=date&locale=en&title=" + eventTitle + "&name=" + name + "&description=" + description + "&" + fromDate + "=" + _time + "||" + _time2 + "&" + fromDate2 + "=" + _dtime + "||" + _dtime2 + "&" + fromDate3 + "=" + _ddtime + "||" + _ddtime2 + "&location=" + location

    driver = webdriver.Chrome()
    driver.get(doodUrl)
    try:
        initemail = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("initiatorEmail"))
        driver.find_element_by_id("initiatorEmail").send_keys(email)
        next1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next1"))
        if driver.find_element_by_id("next1").is_enabled() and driver.find_element_by_id("next1").is_displayed():
            pass
        else:
            next1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next1"))
        next1.click()
        next2a = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next2a"))
        if driver.find_element_by_id("next2a").is_enabled() and driver.find_element_by_id("next2a").is_displayed():
            pass
        else:
            next2a = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next2a"))
        next2a.click()
        next2b = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next2b"))
        if driver.find_element_by_id("next2b").is_enabled() and driver.find_element_by_id("next2b").is_displayed():
            pass
        else:
            next2b = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next2b"))
        next2b.click()
        next3s = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next3s"))
        if driver.find_element_by_id("next3s").is_enabled() and driver.find_element_by_id("next3s").is_displayed():
            pass
        else:
            next3s = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("next3s"))
        next3s.click()
        finish4a = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("finish4a"))
        if driver.find_element_by_id("finish4a").is_enabled() and driver.find_element_by_id("finish4a").is_displayed():
            pass
        else:
            finish4a = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("finish4a"))
        finish4a.click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "participationLink")))
            if driver.find_element_by_id("participationLink").is_displayed() and driver.find_element_by_id("participationLink").is_enabled():
                print("Event has been scheduled.")
                print("Thank You for using Doodle Scheduler.")
            else:
                print("Error occurred. Please try again.")
        except TimeoutException:
            print("Timed out waiting for page to load")
        except NoSuchElementException:
            print("Unable to locate element.")
            print("Please try again.")
        except WebDriverException:
            print("Element is not clickable.")
            print("Please try again.")
    except TimeoutException:
        print("Timed out waiting for page to load")
        print("Please try again!")
    except NoSuchElementException:
        print("Unable to locate element.")
        print("Please try again.")
    except WebDriverException:
        print("Element is not clickable.")
        print("Please try again.")
    driver.quit()
doodle()
