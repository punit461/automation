from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.chrome.options import Options


# block to send messages 

def message_send():

    search_input3 = driver.find_element_by_xpath('/html/body/mw-app/div/main/mw-main-container/div/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea')
    search_input3.send_keys(message)
    search_input3.send_keys(Keys.ENTER)
    
# this block will check whether the chrome will run background or not 


def display_check(display):
    if display[0] == 'y':
        print(" Launching chrome")
        return True
    elif display[0] == "n":
        print("All operations Will be done in background")
        return True
    else:
        return False

while True:
    try:
        display = input('Do You want to see the display of sending messages type Yes or No ').lower()
        if display_check(display): break
    except ValueError:
        print("Sorry, Wrong Input Try Again")


# to check whether to send single message to all the contacts from google sheet or send custom message

def sms_check_value(sms_check):
    if sms_check == 1:
        print('Message from the Message Box will be Sent')
        return True
    elif sms_check == 2:
        print('Custom message from Message Column will be sent')
        return True
    else:
        return False



while True:
    try:
        sms_check = int(input('Send messages from (Message box Press 1) or (Press 2 for Sending Custom message) from C column '))
        if sms_check_value(sms_check): break
    except ValueError:
        print("Sorry, Wrong Input Try Again")

#To Run the Program headless without opening any physical window
if display[0] == 'n':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.binary_location = 'C:\link\Link_gen_lav\Canary\Chrome SxS\Application\chrome.exe'
    driver = webdriver.Chrome(options=chrome_options, executable_path='C:\Codes_projects_python\SMS Sender\chromedrivercanary.exe')
elif display[0] =='y':
    driver = webdriver.Chrome('C:\Codes_projects_python\SMS Sender\chromedriver')
#-----------------------------#----------------------------------

#authentication to Login and access google sheet and open and read the Sheet

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# open the google sheet thru which we can send the messages which contains mobile numbers and message
sheet = client.open('SMS - Google').sheet1


#Open The chrome and login using the credentials and opening the website



driver.get("https://messages.google.com/web/authentication")
driver.implicitly_wait(100)

# click toggle so that it rememebers the scanned qr code so that if refresh is done will not require to again scan.
driver.find_element_by_class_name('mat-slide-toggle-thumb').click()
time.sleep(25)


#---------------------------------y-------#--------------------------------
#To check the count of the Names to control the Loop 
# [ have inputed the counta function of excel in sheet on this cell i think it can also be done thru length function in python ( didnot work forme.)
z = int(sheet.cell(1,5).value)

#Initialize
a = 2


#while loop to check and tell the program to stop
while a <= z:
    # if loop to check the id are already generated?

    if sheet.cell(a, 4).value != 'Sent':
        driver.get('https://messages.google.com/web/conversations/new')
        time.sleep(10)

        # Mobile Number Area clearing and entering data
        Mobile = sheet.cell(a,2).value
        search_input2 = driver.find_element_by_class_name('input')
        search_input2.send_keys(Mobile)
        search_input2.send_keys(Keys.ENTER)
        time.sleep(10)



        # to check and send SMS # Message Area clearing and entering data

        if sms_check == 1:
            message = sheet.cell(2, 10).value
            message_send()


        elif sms_check == 2:
            message = sheet.cell(a, 3).value
            message_send()


        #update in sheet as message Status sent
        sheet.update_cell(a, 4, 'Sent')
        a+=1

    else:
        a += 1

driver.quit()
