from selenium import webdriver
import time

#login variables
username = 'your_ticket_username'
password = 'your_ticket_password'


DRIVER_PATH = 'your_driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
#replace with link specific to your helpdesk
driver.get('http://osTicket/scp/login.php')

#find username input
username_input = driver.find_element_by_id('name')
#find password input
password_input = driver.find_element_by_id('pass')
#find login button
login_button = driver.find_element_by_name('submit')

############# Login #############
#entering username
username_input.send_keys(username)
#enter user password
password_input.send_keys(password)
#press login button
login_button.click()
#################################

#Go to dashboard
time.sleep(3)
#replace with link specific to your helpdesk
driver.get('http://osTicket/scp/dashboard.php#topic')
#find export button
#Change to the value that you want to download ex. Departments, Topic, Agent
topic = 'topic'
javascript = 'document.querySelector("button[value=' + topic + ']").click();'
#Download file
time.sleep(2)
driver.execute_script(javascript)

#close window
# If error downloading file, just increase this time.
time.sleep(3)
#close window
driver.quit()




