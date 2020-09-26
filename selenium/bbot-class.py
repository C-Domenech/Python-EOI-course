from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time


# wait until class time
def class_time():
    it_is_time = False
    start_time = "10:57:00" # set time
    while not it_is_time:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Hora actual =", current_time)
        if current_time == start_time:
            print("¡Es hora de ir a clase!")
            it_is_time = True
        else:
            continue
    set_driver()


# driver creation, set microphone and webcam permissions
def set_driver():
    opt = Options()
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1
    })
    driver = webdriver.Chrome(options=opt, executable_path="/SeleniumBrowserDrivers/chromedriver.exe") # PATH to your chromedriver.exe
    open_browser(driver)


# open browser and start session
def open_browser(driver):
    CLASS_LINK = 'your-url' # add your url
    driver.get(CLASS_LINK)
    print("> Navegador abierto")
    print("> Sesión iniciada")
    skip(driver)


# skip tutorial
def skip(driver):
    time.sleep(10)
    close_bt1 = driver.find_element_by_xpath('//*[@id="techcheck-modal"]/button')
    close_bt1.click()
    print("> Primera ventana cerrada")

    time.sleep(5)
    close_bt2 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/button')
    close_bt2.click()
    print("> Segunda ventana cerrada")

    time.sleep(5)
    open_side_panel(driver)

    time.sleep(5)
    # choose chat 'Todos'
    chat_all = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/main/div[3]/section/div/div/ul/li/ul/li/bb-channel-list-item/button')
    chat_all.click()
    print("> Chat seleccionado")
    greet(driver)


# open side panel
def open_side_panel(driver):
    side_panel = driver.find_element_by_id("side-panel-open")
    side_panel.click()
    print("> Panel lateral abierto")


# write greeting in the text area
def greet(driver):
    time.sleep(5)
    text_area = driver.find_element_by_id("message-input")
    text_area.clear()
    text_area.send_keys("Buenas!")
    text_area.send_keys(Keys.RETURN)
    print("> Saludo realizado")
    end_class_time(driver)


# wait until the end of the class
def end_class_time(driver):
    end_time = False
    start_time = "14:05:00" # set time
    while not end_time:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Hora actual =", current_time)
        if current_time == start_time:
            print("¡Es hora de terminar!")
            end_time = True
        else:
            continue
    goodbye(driver)


# write farewell in the text area
def goodbye(driver):
    text_area = driver.find_element_by_id("message-input")
    text_area.clear()
    # text_area.send_keys("Hasta mañana!")
    # print("> Despedida realizada: Hasta mañana!")

    text_area.send_keys("Hasta el lunes!")
    print("> Despedida realizada: Hasta el lunes!")
    text_area.send_keys(Keys.RETURN)

    # TODO A good thing -> right now doesn't work
    '''
    it_is_time = False
    start_tomorrow = "hasta mañana"
    start_monday = "hasta el lunes"
    while not it_is_time:
        chat_message = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div[3]/section/section/section/div[2]/ul/li/div/div/div[2]/p[2]")
        message = chat_message.text
        if message.lower().startwith(start_tomorrow):
            text_area = driver.find_element_by_id("message-input")
            text_area.clear()
            text_area.send_keys("Hasta mañana!")
            text_area.send_keys(Keys.RETURN)
            print("> Despedida realizada: Hasta mañana!")
            it_is_time = True
        elif message.lower().startwith(start_monday):
            text_area = driver.find_element_by_id("message-input")
            text_area.clear()
            text_area.send_keys("Hasta el lunes!")
            text_area.send_keys(Keys.RETURN)
            print("> Despedida realizada: Hasta el lunes!")
            it_is_time = True
        '''
    close_session(driver)


# open session menu and logout
def close_session(driver):
    side_panel = driver.find_element_by_id("session-menu-open")
    side_panel.click()
    print("> Panel de sesión abierto")
    time.sleep(5)
    logout_button = driver.find_element_by_id("leave-session")
    logout_button.click()
    time.sleep(5)
    close = driver.find_element_by_id("session-survey-skip")
    close.click()
    print("> Sesión cerrada")


def main():
    class_time()


if __name__ == '__main__':
    main()
