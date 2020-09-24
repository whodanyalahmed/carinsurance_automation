import csv
from selenium import webdriver
from selenium.common import exceptions
import sys
import time
from random import randint
from selenium.webdriver.chrome.options import Options
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import credentials as cred
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#open chrome browser
driver = webdriver.Chrome("driver\\chromedriver.exe")
def automateSite():
    print("""
    
    **** Enter All Informations Below ****
    
    """)
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    DOB = input("Enter Date-Of-Birth MM/DD/YYYY: ")
    Gender = input("Enter Gender (Male/Female): ")
    Gender.lower()
    Address = input("Enter Address: ")
    State = input("Select State Like(NM,NJ): ")
    City = input("Enter City: ")
    zipCode = input("Enter Zip Code: ")
    Product = input("Select product (Auto , Motorcycle/ATV , Boat/PWC , Motor Home , Renters , Travel Trailer , Commercial Auto , EPLI, NPDO, Cyber and other):")
    Product.lower()

    print("""
    
    **** Vehicle Information ****
    
    """)
    Year = input("Enter Vehicle Year: ")
    Make = input("Enter Vehicle Make: ")
    Model = input("Enter Vehicle Model: ")

    print("""
    
    **** Information for natlloydscorp.com ****
    
    """)

    DFE = input("Enter Date Of Effectivness: ")

    print("""
    
    **** Information for foragentsonly.com ****
    
    """)

    print("""
	***************** Select Options for How long has the insured lived at their current address? ********************

	1 - 2 Months or Less

	2 - More Than 2 Months and Less Than 1 Year

	3 - 1 Year or More

	""")

    while(True):
        option = int(input("Select One of Above Options : "))
        if option == 1:
            livinDuration = "2 Months or Less"
            break
        elif option == 2:
            livinDuration = "More Than 2 Months and Less Than 1 Year"
            break
        elif option == 3:
            livinDuration = "1 Year or More"
            break
    
    print("""
	***************** Select Options for Was the above disclosure read or provided to the consumer? ********************

	1 - Yes

	2 - No

	""")

    while(True):
        option = int(input("Select One of Above Options Again : "))
        if option == 1:
            yesno = "yes"
            break
        elif option == 2:
            yesno = "no"
            break
    print("""
    
    **** Information for superioraccess.com ****
    
    """)

    print("""
	***************** Select Options for Personal or Commercial? ********************

	1 - Personal

	2 - Commercial

	""")
    while(True):
        option = int(input("Select One of Above Options Again : "))
        if option == 1:
            quoteType = "Personal"
            break
        elif option == 2:
            quoteType = "Commercial"
            break
    
    Business = input("Please Enter Line of Business : ")
    jobSearch = input("What does the applicant do for a living? : ")
    
    # ***************************** 1 **********************************

    def travelers(firstName, lastName, State, City, zipCode):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading travelers.com/foragents
        """)
        try:
            driver.get("https://www.travelers.com/foragents")  
            time.sleep(5)
            agentCode = driver.find_element_by_id("username")
            agentCode.clear()
            agentCode.send_keys(cred.travelerUserName)
            password = driver.find_element_by_id("password")
            password.clear()
            password.send_keys(cred.travelerPassword)
            driver.find_element_by_id("btn-trans-login").click()
            print("Wait Its loading Page :)")
            time.sleep(20)
            newQoute = driver.find_element_by_xpath('//*[contains(text(), "Quote & Issue")]')
            newQoute.click()
            time.sleep(5)
            fName = driver.find_element_by_name("firstName")
            fName.clear()
            fName.send_keys(firstName)
            lName = driver.find_element_by_name("lastName")
            lName.clear()
            lName.send_keys(lastName)
            state = driver.find_element_by_name('state')
            state.click()
            for option in state.find_elements_by_tag_name('option'):
                if option.text == State:
                    break
                else:
                    state.send_keys(Keys.DOWN)
            city = driver.find_element_by_name("city")
            city.clear()
            city.send_keys(City)
            zipcode = driver.find_element_by_name("zip")
            zipcode.clear()
            zipcode.send_keys(zipCode)
            time.sleep(3)
            driver.find_element_by_id("search-button").click()
        except:
            pass
    travelers(firstName, lastName, State, City, zipCode)

    # ***************************** 2 **********************************

    def empowerins(firstName, lastName, DOB, Gender, Address, City, zipCode, Product):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading empowerins.com
        """)
        try:
            driver.execute_script("window.open('about:blank', 'tab2');")
            driver.switch_to.window("tab2")
            driver.get("https://agents.empowerins.com/LogOn.aspx?LogOut=true")
            time.sleep(5)
            agentCode = driver.find_element_by_id("txtUserName")
            agentCode.clear()
            agentCode.send_keys(cred.empowerinsUserName)
            password = driver.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys(cred.empowerinsPassword)
            driver.find_element_by_id("btnLogIn").click()
            print("Wait Its loading Page :)")
            time.sleep(10)
            newQoute = driver.find_element_by_xpath('//*[contains(text(), "new quote")]')
            newQoute.click()
            time.sleep(5)
            fName = driver.find_element_by_id("txtDriver1First")
            fName.clear()
            fName.send_keys(firstName)
            lName = driver.find_element_by_id("txtDriver1Last")
            lName.clear()
            lName.send_keys(lastName)
            gender = driver.find_element_by_id("ddlDriver1Sex")
            gender.send_keys(Keys.ENTER)
            if(Gender == 'male'):
                gender.send_keys(Keys.DOWN)
                time.sleep(2)
                gender.send_keys(Keys.ENTER)
            dob = driver.find_element_by_id("txtDriver1DOB")
            dob.clear()
            dob.send_keys(DOB)
            address = driver.find_element_by_id("txtDriver1Address1")
            address.clear()
            address.send_keys(Address)
            city = driver.find_element_by_id("txtCity")
            city.clear()
            city.send_keys(City)
            zipcode = driver.find_element_by_id("txtZip")
            zipcode.clear()
            zipcode.send_keys(zipCode)
            time.sleep(1)
            driver.find_element_by_id("hprNext").click()
        except:
            pass
    empowerins(firstName, lastName, DOB, Gender, Address, City, zipCode, Product)
    print("Wait loading foragentsonly")
    time.sleep(5)
    
    # ***************************** 3 **********************************

    def falconinsgroup(firstName, lastName, DOB, Gender, Address, City, zipCode, Product, Year, Make, Model):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading falconinsgroup.com
        """)
        try:
            driver.execute_script("window.open('about:blank', 'tab3');")
            driver.switch_to.window("tab3")
            driver.get('https://agency.falconinsgroup.com/#!')
            time.sleep(5)
            agentCode = driver.find_element_by_id("UserName")
            agentCode.clear()
            agentCode.send_keys(cred.falconinsgroupUserName)
            password = driver.find_element_by_id("password")
            password.clear()
            password.send_keys(cred.foragentsonlyPassword)
            driver.find_element_by_id("SLLBBLogInButton").click()
            print("Wait Its loading Page :)")
            time.sleep(10)
            newQoute = driver.find_element_by_xpath('//*[contains(text(), "New Quote")]')
            newQoute.click()
            time.sleep(5)
            fName = driver.find_element_by_id("QIA0FirstNameTextbox")
            fName = fName.find_element_by_tag_name('input')
            fName.clear()
            fName.send_keys(firstName)
            lName = driver.find_element_by_id("QIA0LastNameTextbox")
            lName = lName.find_element_by_tag_name('input')
            lName.clear()
            lName.send_keys(lastName)
            dob = driver.find_element_by_xpath("(//input[@data-bind=\"value: Info.DateOfBirth.DateText, disable: Info.DateOfBirth.NoInput, falconTextBox: true, css: { 'ui-state-error': Info.DateOfBirth.IsInvalid() },attr: {'id': Info.DateOfBirth.Element}\"])[1]")
            dob.send_keys(DOB)
            zipcode = driver.find_element_by_id("QIA0ZipCodeTextbox")
            zipcode = zipcode.find_element_by_tag_name('input')
            zipcode.clear()
            zipcode.send_keys(zipCode)
            time.sleep(2)
            year = driver.find_element_by_xpath("//*[@data-bind=\"visible: Info.Year.DisplayOnly() == false, attr: {'id': Info.Year.Element,'data-location': Info.Year.Element}\"]")
            year.click()
            time.sleep(3)
            year = driver.find_element_by_id("s2id_autogen87_search")
            year.click()
            time.sleep(2)
            year.send_keys(Year)
            year.send_keys(Keys.ENTER)
            time.sleep(5)
            make = driver.find_element_by_xpath("//*[@data-bind=\"visible: true && Info.Make.IsVisible() == true, attr: {'class': 'falcInputControl falcImportant vehicle-make' + (Info.Make.DisplayOnly() ? ' falcDisplayOnly' : '') + (Info.Make.IsDisabled() ? ' falcIsDisabled' : '')} \"]")
            make.click()
            time.sleep(3)
            make = driver.find_element_by_id("s2id_autogen88_search")
            time.sleep(1)
            make.click()
            make.send_keys(Make)
            make.send_keys(Keys.ENTER)
            time.sleep(5)
            model = driver.find_element_by_xpath("//*[@data-bind=\"visible: true && Info.Model.IsVisible() == true, attr: {'class': 'falcInputControl falcImportant vehicle-model' + (Info.Model.DisplayOnly() ? ' falcDisplayOnly' : '') + (Info.Model.IsDisabled() ? ' falcIsDisabled' : '')} \"]")
            model.click()
            time.sleep(3)
            model = driver.find_element_by_id("s2id_autogen89_search")
            time.sleep(1)
            model.click()
            time.sleep(1)
            model.send_keys(Model)
            model.send_keys(Keys.ENTER)
            time.sleep(5)
            driver.find_element_by_xpath("//*[contains(text(),'Get Quote')]").click()
        except:
            pass
    falconinsgroup(firstName, lastName, DOB, Gender, Address, City, zipCode, Product, Year, Make, Model)

    # ***************************** 4 **********************************

    def foragentsonly(firstName, lastName, DOB, Gender, Address, City, zipCode , Product, livinDuration, yesno):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading foragentsonly.com
        """)
        try:  
            driver.execute_script("window.open('about:blank', 'tab4');")
            driver.switch_to.window("tab4")
            driver.get("https://www.foragentsonly.com/login/")
            time.sleep(2)
            agentCode = driver.find_element_by_id("user1")
            agentCode.clear()
            agentCode.send_keys(cred.foragentsonlyUserName)
            password = driver.find_element_by_id("password1")
            password.clear()
            password.send_keys(cred.foragentsonlyPassword)
            driver.find_element_by_class_name("loginButton").click()
            time.sleep(3)
            driver.find_element_by_id("selectProductButton").click()
            time.sleep(3)
            if(Product == 'auto'):
                driver.find_element_by_class_name("icon-AU").click()
            elif(Product == 'motorcycle' or Product == 'atv' or Product == 'motorcycle/atv'):
                driver.find_element_by_class_name("icon-MC").click()
            elif(Product == 'boat' or Product == 'pwc' or Product == 'boat/pwc'):
                driver.find_element_by_class_name("icon-BT").click()
            elif(Product == 'motor home'):
                driver.find_element_by_class_name("icon-MT").click()
            elif(Product == 'renters'):
                driver.find_element_by_class_name("icon-TT").click()
            elif(Product == 'commercial auto'):
                driver.find_element_by_class_name("icon-CV").click()
            elif(Product == 'renters'):
                driver.find_element_by_class_name("icon-RT").click() 
            elif(Product == 'epli' or Product == 'npdo' or Product == 'cyber' or Product == 'other'):
                driver.find_element_by_class_name("icon-PG").click()      
            time.sleep(2) 
            driver.find_element_by_id("quoteActionSelectButton").click()
            time.sleep(randint(20,30))
            driver.switch_to_window(driver.window_handles[4])
            fName = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_FirstName")
            fName.clear()
            fName.send_keys(firstName)
            lName = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_LastName")
            lName.clear()
            lName.send_keys(lastName)
            gender = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_Gender")
            gender.send_keys(Keys.ENTER)
            if(Gender == 'male'):
                gender.send_keys(Keys.DOWN)
                time.sleep(0.5)
                gender.send_keys(Keys.DOWN)
                time.sleep(2)
                gender.send_keys(Keys.ENTER)
            elif(Gender == 'female'):
                gender.send_keys(Keys.DOWN)
                time.sleep(2)
                gender.send_keys(Keys.ENTER)
            dob = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_DateOfBirth")
            dob.clear()
            dob.send_keys(DOB)
            address = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_MailingAddress")
            address.clear()
            address.send_keys(Address)
            city = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_City")
            city.clear()
            city.send_keys(City)
            zipcode = driver.find_element_by_id("NamedInsured_Embedded_Questions_List_ZipCode")
            zipcode.clear()
            zipcode.send_keys(zipCode)
            questions = driver.find_element_by_id('NamedInsured_Embedded_Questions_List_CurrentResidence')
            questions.click()
            for option in questions.find_elements_by_tag_name('option'):
                if option.text == livinDuration:
                    option.send_keys(Keys.ENTER)
                    break
                else:
                    questions.send_keys(Keys.DOWN)
            time.sleep(1)
            yesNo = driver.find_element_by_id('NamedInsured_Embedded_Questions_List_DisclosureProvided')
            yesNo.click()
            if yesno == 'yes':
                option.send_keys(Keys.DOWN)
                option.send_keys(Keys.ENTER)
            elif yesno == 'no':
                option.send_keys(Keys.DOWN)
                option.send_keys(Keys.DOWN)
                option.send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element_by_class_name("save-data").click()
        except:
            pass
    foragentsonly(firstName, lastName, DOB, Gender, Address, City, zipCode, Product, livinDuration, yesno)

    # ***************************** 5 **********************************

    def natlloydscorp(DFE):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading natlloydscorp.com
        """)
        try:  
            driver.execute_script("window.open('about:blank', 'tab6');")
            driver.switch_to.window("tab6")
            driver.get("https://www.agent.natlloydscorp.com/innovation?rq=COUserStartPage")
            time.sleep(2)
            agentCode = driver.find_element_by_id("j_username")
            agentCode.clear()
            agentCode.send_keys(cred.natlloydscorpUserName)
            password = driver.find_element_by_id("j_password")
            password.clear()
            password.send_keys(cred.natlloydscorpPassword)
            driver.find_element_by_id("SignIn").click()
            time.sleep(3)
            driver.find_element_by_id("NewQuote").click()
            time.sleep(2)
            dateEffective = driver.find_element_by_id("BasicPolicy.EffectiveDt")
            dateEffective.clear()
            dateEffective.send_keys(DFE)
            time.sleep(2)
            driver.find_element_by_id('Continue').click()
        except:
            pass
    natlloydscorp(DFE)

    # ***************************** 6 **********************************

    def thimble(zipCode, jobSearch):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading thimble.com
        """)
        try:
            driver.execute_script("window.open('about:blank', 'tab7');")
            driver.switch_to.window("tab7")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            driver.get("https://open-api.thimble.com/oauth/authorize?client_id=5727d306a5e24263b426be9ee5299a5c&client_secret=a0e7cdd61ca446b991167d54b5e7585c&redirect_uri=https%3A%2F%2Fbroker.thimble.com%2Flogin&role=broker&scope=basic&response_type=code")
            time.sleep(2)
            agentCode = driver.find_element_by_id("email")
            agentCode.clear()
            agentCode.send_keys(cred.thimbleUserName)
            password = driver.find_element_by_id("password")
            password.clear()
            password.send_keys(cred.thimblePassword)
            driver.find_element_by_id("log-in").click()
            time.sleep(20)
            driver.find_element_by_xpath('//*[contains(text(),"Start Selling")]').click()
            time.sleep(10)
            iframe = driver.find_elements_by_tag_name('iframe')[0]
            driver.switch_to.frame(iframe)
            time.sleep(10)
            zipcode = driver.find_element_by_id('zipcode')
            zipcode.clear()
            zipcode.send_keys(zipCode)
            time.sleep(10)
            jobsearch = driver.find_element_by_id('jobSearch')
            jobsearch.clear()
            jobsearch.send_keys(jobSearch)
            
        except:
            pass
    thimble(zipCode, jobSearch)
    
    # ***************************** 7 **********************************

    def superioraccess(quoteType, Business):
        print("""
        Please Be Patient depending on your network speed :)
        Its Loading adb4.superioraccess.com
        """)
        try:
            driver.execute_script("window.open('about:blank', 'tab8');")
            driver.switch_to.window("tab8")
            driver.get("https://www.superioraccess.com/login/")
            time.sleep(2)
            agentCode = driver.find_element_by_id("txtId_subMaster2")
            agentCode.clear()
            agentCode.send_keys(cred.superioraccessUserName)
            password = driver.find_element_by_id("txtPassword_subMaster2")
            password.clear()
            password.send_keys(cred.superioraccessPassword)
            time.sleep(2)
            driver.find_element_by_xpath("(//input[@type='submit'])[2]").click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[contains(text(),"Get Quote")]').click()
            time.sleep(3)
            if(quoteType == 'Personal'):
                driver.find_element_by_xpath('(//*[contains(text(),"Personal")])[1]').click()
                time.sleep(1)
                driver.find_element_by_id('NewQuotePer').click()
                time.sleep(1)
                driver.find_element_by_id('NewClientaPer').click()
            elif(quoteType == 'Commercial'):
                driver.find_element_by_xpath('(//*[contains(text(),"Commercial")])[1]').click()
                time.sleep(1)
                driver.find_element_by_id('NewQuoteCom').click()
                time.sleep(1)
                driver.find_element_by_id('NewClientCom').click()
                selState = driver.find_element_by_id('slctStates')
                selState.click()
                selState.send_keys(Keys.DOWN)
                selState.send_keys(Keys.ENTER)
            bussinesField = driver.find_element_by_id('slctLobs')
            bussinesField.click()
            for option in bussinesField.find_elements_by_tag_name('option'):
                if option.text == Business:
                    option.send_keys(Keys.ENTER)
                    break
                else:
                    bussinesField.send_keys(Keys.DOWN)
            time.sleep(1)
            driver.find_element_by_xpath('//*[contains(text(),"Create Application")]').click()
        except:
            pass
    superioraccess(quoteType, Business)
automateSite()