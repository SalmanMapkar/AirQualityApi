#Import Libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from ..models import AirReport


def ScrapeData():
    #Download Drivers
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install() ,options=options)



    #Scrape Data
    url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"
    driver.get(url)

    air_quality =  driver.find_element_by_class_name('value-text').text
    pm_2point5 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[1]/div[3]').text
    pm_10 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[2]/div[3]').text
    no_2 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[3]/div[3]').text
    o_3 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[4]/div[3]').text
    co = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[5]/div[3]').text
    so_2 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/div[2]/div[6]/div[3]').text
    temperature = str(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[5]/div[3]/div[1]/div[2]').text).split('℃')[0]
    humidity = str(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[5]/div[3]/div[2]/div[2]').text).split('%')[0]
    wind_speed = str(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[5]/div[3]/div[3]/div[2]').text).split(' kph')[0]
    uv = str(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[5]/div[3]/div[4]/div[2]').text).split(' of ')

    print("Air Quality = {}\nPM 2.5 = {}\n".format(air_quality, pm_2point5))

    #Appending into Model
    ar = AirReport(
        air_quality=air_quality,
        pm_2point5=pm_2point5,
        pm_10=pm_10,
        no_2=no_2,
        o_3=o_3,
        co=co,
        so_2=so_2,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        uv=uv)
    ar.save()

    return ar