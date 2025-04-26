from selenium import webdriver #selenium allows python to control broswer. webdriver is a tool that accesses the webbroswer
from selenium.webdriver.firefox.service import Service #service tells selenium where to find geckodriver. basically the translator
from selenium.webdriver.common.by import By #By finds elements on the page, when we want to use buttons or read text, we use "Find it BY id"
import time #using this as a pause for inputs

GECKODRIVER_PATH = "/opt/homebrew/bin/geckodriver" #saving location of geckodriver as a variable

service = Service(GECKODRIVER_PATH) #creates a service object that knows where geckodriver is
options = webdriver.FirefoxOptions() #creates browser settings called options
driver = webdriver.Firefox(service=service, options = options) #openes firefox using service and options

login_time_left = 20

driver.get("https://app.getsling.com")#navigate to sling
print(f"You have {login_time_left} seconds left to log into Sling...")
for remaining in range(login_time_left, 0, -1):
    print(f"{remaining} seconds remaining", end="\r")
    time.sleep(1)


driver.get("https://app.getsling.com/shifts?mode=custom&tab=myschedule&date=2025-04-13")
#tells slenium to navigat to scheduling page
time.sleep(5) #5 second timer to load

shifts = driver.find_elements(By.CLASS_NAME, "shift") #Finds the shifts 
days = driver.find_elements(By.CLASS_NAME, "table-cell") #finds the day 

print(f"Found {len(shifts)} shifts (Including Duplicates and empty shifts)")

datedShifts = []

for day in days:
    shift_date = day.get_attribute("data-shift-date")
    if not shift_date:
        continue

    shiftsInDay = day.find_elements(By.CLASS_NAME, "shift")
    
    for shift in shiftsInDay:
        shift_text = shift.text.strip()
        if shift_text == "":
            continue
        if "unavailable" in shift_text.lower():
            continue
        if "-" in shift_text:
            parts = shift_text.split("-")
            start_time = parts[0].strip()
            end_time = parts[1].strip()
        
        datedShifts.append((shift_date, start_time, end_time))

    
print(f"\nFound {len(datedShifts)} shifts over 2 weeks!\n")

for date, start, end in datedShifts:
    print(f"{date} | Start: {start} | End: {end}")
    
    
    
#Start of timesheet area

driver.get("https://trs.ucmerced.edu/") #open timesheet area
timesheet_buttons = driver.find_elements(By.CLASS_NAME, "custom")
timesheet_buttons[1].click()





driver.quit() #end of program