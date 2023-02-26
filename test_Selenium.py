from selenium import webdriver

def get_textDivs():
    elements = driver.find_elements("xpath","//div[@class='text']")
    for element in elements:
        print(element.text)

driver = webdriver.Chrome()
driver.get("https://bcncgroup.com")
driver.maximize_window()
get_textDivs()
driver.get("https://bcncgroup.com/who-we-are/")
get_textDivs()

#Adjusted for simplicity, as "home" and who we are" are different urls, normally we should navigate clicking the buttons
#which gives problems because of click intercepted, in which case i'd recommend using explicit/implicit wait with multiples EC
#or on my personal opinion i think FluentWait is best. Normally we have to deal with load times that are not instant like this website

#For more complicated tests isuess probably ChromeOptions are needed

#Also i would encourage using BDD like cucumber for better understanding of the tests, which i dont know is a thign we discussed