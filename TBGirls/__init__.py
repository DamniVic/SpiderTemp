# user/bin/env python3
# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver

def test1():
    driver = webdriver.Chrome()
    driver.get('https://tuchong.com/explore/')
    print(driver.title)
    items = driver.find_elements_by_class_name('tag-square-base')
    print(items)
    items[0].click()
    print(driver.current_url)
    handles = driver.window_handles
    print(driver.current_window_handle)
    for handle in handles:
        print(handle)
        if not handle == driver.current_window_handle:
            driver.switch_to.window(handle)
            break
    sleep(5)
    print(driver.title)
    girls = driver.find_elements_by_class_name('post-item')
    print(girls)
    girls[0].click()

def test2():
    driver = webdriver.Chrome()
    driver.get('https://tuchong.com/')
    print(driver.title)
    # login = driver.find_element_by_link_text('登录')
    login = driver.find_element_by_xpath('/html/body/header/nav/div[2]/a[1]')
    print(login)
    if not login is None:
        login.click()
        driver.switch_to.alert
        account = driver.find_element_by_xpath('//*[@id="login-dialog"]/div/div/div/div[1]/form/div[2]/input')
        password = driver.find_element_by_xpath('//*[@id="login-dialog"]/div/div/div/div[1]/form/div[3]/input')
        loginbtn = driver.find_element_by_xpath('//*[@id="login-dialog"]/div/div/div/div[1]/form/div[6]/button')
        account.send_keys('lizelang19941208@126.com')
        password.send_keys('li55626437')
        loginbtn.click()
        driver.refresh()
        print(driver.title)
        girls = driver.find_element_by_link_text('人像')
        girls.click()
        driver.refresh()

if __name__ == '__main__':
    test2()
