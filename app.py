from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound
import time
import sys
import threading

def playsound_audio():
    playsound("audio.mp3")

# NO issues
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://selfregistration.cowin.gov.in/')
print(driver.title)
print("Attempting to login...")

# Replace this with your mobile number
mob_num = "9988776655"

driver.find_element_by_id("mat-input-0").send_keys(mob_num)
driver.find_element_by_class_name("next-btn").click()

sum = 0 
try:
    otp = input("Please enter OTP:")
    driver.find_element_by_id("mat-input-1").send_keys(otp)
    driver.find_element_by_class_name("next-btn").click()

    print("OTP Entered")
    ## Here you need to click the schedule button for all the members

    # waiting for page request
    time.sleep(4)

    #for ele in driver.find_elements_by_class_name("calcls"):
        #driver.execute_script("arguments[0].scrollIntoView();",ele)
        #ele.click()

    driver.find_elements_by_class_name("calcls")[0].click()
    time.sleep(2)
    

    #driver.execute_script("arguments[0].scrollIntoView();",driver.find_elements_by_class_name("calcls")[1])
    #driver.find_elements_by_class_name("calcls")[1].click()

    #driver.find_element_by_class_name("register-btn").click()

    # Enter Pincode
    #pincode = input("Enter Pincode:")
    pincode = 201301
    driver.find_element_by_class_name("mat-input-element").send_keys(pincode)
    driver.find_element_by_class_name("pin-search-btn").click()
    # seach by pin code done

    # click on 18+
    driver.find_elements_by_class_name('form-check')[0].click()

    start_time = time.time()

    # search for unbooked
    tmp = [x for x in driver.find_elements_by_tag_name('a') if str(x.text).isnumeric()]
    print(f"Unbook slots: {len(tmp)} {tmp}")
except:
    print("!!!exception!!!")


try:
    while len(tmp)==0:
        # Enter Pincode
        driver.find_element_by_class_name("mat-input-element").send_keys(pincode)
        driver.find_element_by_class_name("pin-search-btn").click()
        # seach by pin code done
        # click on 18+
        time.sleep(1)
        driver.find_elements_by_class_name('form-check')[0].click()
        tmp = [x for x in driver.find_elements_by_tag_name('a') if str(x.text).isnumeric()]
        print(f"Unbook slots: {len(tmp)} {[x.text for x in tmp]} timestamp: {time.asctime()}")
        sum+=len(tmp)
        ### Please add sleep later
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    end_time = time.time()
    print(f"total time: {end_time-start_time}")
    # If while breaks, emit sound
    threading.Thread(target=playsound_audio).start()
    tmp[0].click
    print(f"Total unbooked slots found : {sum}")
    if sum!=0:
        tmp[0].click()
        driver.find_elements_by_class_name("time-slot")[3].click()









