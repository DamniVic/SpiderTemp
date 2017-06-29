# user/bin/env python3
# -*- coding:utf-8 -*-
import os
import traceback
import requests
import sys
from selenium import webdriver
CURRENTPATH = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取该文件的绝对路径
# 根据提供的网址下载文件
def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]  # 读取文件的名字
    print("Download Image File=", local_filename)
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    os.makedirs(CURRENTPATH+'\\tuchong', exist_ok=True)  # 创建一个新的文件夹
    with open(CURRENTPATH+'\\tuchong\\'+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename

class Spider:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 初始化这个类，这里仅仅指明了用哪个浏览器
    def execute(self):
        self.login()  # 登录图虫
        self.album('3')  # 去到编号为3这个人的相册
    def login(self):
        self.driver.get('https://tuchong.com/')  # 打开图虫网页
        print(self.driver.title)
        # login = self.driver.find_element_by_link_text('登录')
        login = self.driver.find_element_by_xpath('/html/body/header/nav/div[2]/a[1]')  # 找到图虫首页上面的登录按钮，这里采用的是xpath方式
        print(login)
        if not login is None:  # 判断找到的登录按钮是否为空
            login.click()  # 点击登录按钮
            self.driver.switch_to.alert  # 将当前driver的焦点转移到弹出的对话框
            account = self.driver.find_element_by_xpath('//*[@id="login-dialog"]/div/div/div/div[1]/form/div[2]/input')  # 找到输入账号的输入框
            password = self.driver.find_element_by_xpath('//*[@id="login-dialog"]/div/div/div/div[1]/form/div[3]/input')  # 找到输入密码的输入框
            loginbtn = self.driver.find_element_by_xpath('//*[@id="login-dialog"]/div/div/div/div[1]/form/div[6]/button')  # 找到登录的按钮
            account.send_keys('你的图虫账号')  # 输入账号
            password.send_keys('你的图虫密码')  # 输入密码
            loginbtn.click()  # 点击登录
            self.driver.refresh()  # 刷新driver，让网页本身获取焦点
            print(self.driver.title)  # 打印标题
    def album(self, num):
        url = 'https://tuchong.com/%s/albums' % (str(num),)  # 输入ID为num的账户的相册URL（因为上面已经登录了，所以这里不会要求重新登录）
        self.driver.get(url)
        self.driver.refresh()  # 刷新driver获取当前网页的焦点
        print(self.driver.title)  # 打印当前网页的标题
        albums = self.driver.find_elements_by_class_name('picture-wrap')  # 找到用户的相册元素的集合（多个相册就有多个元素）
        if True:
            try:
                albums[2].click()  # 这里点击第三个相册
                self.driver.refresh()  # 获取当前页面的driver
                images = self.driver.find_elements_by_class_name('post-cover')  # 获取相册里面的图片集合
                for image in images:  # 挨个打开，图片大图（会在新的标签页打开大图）
                    image.click()
                curhandle = self.driver.current_window_handle  # 获取当前网页的把柄handle（网页）
                print('main handle:', curhandle)
                for handle in self.driver.window_handles:  # 遍历当前浏览器打开的所有handle（网页）
                    print('handle:', handle)
                    if not handle == curhandle:  # 遍历的handle（网页）与相册的网页handle作比较
                        self.driver.switch_to.window(handle)  # 将driver的焦点转移到该大图网页
                        image = self.driver.find_element_by_class_name('copyright-contextmenu')  # 找到图片所在的节点
                        src = image.get_attribute('src')  # 从该节点里面取出图片的原地址链接
                        downloadImageFile(src)  # 下载该图片
                        self.driver.close()  # 关闭该网页，
                        print(src)
            except:
                traceback.print_exc()
                self.driver.back()
                self.driver.refresh()
        self.driver.quit()  # 所有的代码执行完，就退出这次程序



if __name__ == '__main__':
    spider = Spider()
    spider.execute()
