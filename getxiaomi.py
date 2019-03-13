from selenium import webdriver
import time


class xiaomi():
    lurl = 'https://account.xiaomi.com/'
    burl = 'https://item.mi.com/product/10000134.html'
    atime = 'Wed Mar 19 10:00:00 2019'

    def __init__(self, usernme, pwd):
        self.username = usernme
        self.pwd = pwd
        self.b = webdriver.Firefox(executable_path='geckodriver.exe')

    def login(self):
        print('正在登陆...\n')
        self.b.get(self.lurl)
        self.b.find_element_by_id('username').send_keys(self.username)
        self.b.find_element_by_id('pwd').send_keys(self.pwd)
        self.b.find_element_by_id('login-button').click()

    def buy(self):
        print('进入米9秒杀页面...\n')
        self.b.get(self.burl)
        print('正在选择型号配件...\n')
        self.b.find_element_by_xpath('//*[@id="J_list"]/div[2]/ul/li[3]').click()
        self.b.find_element_by_xpath('//*[@id="J_list"]/div[3]/ul/li[5]').click()
        while True:
            if time.asctime() == self.atime:
                try:
                    self.b.find_element_by_xpath('//*[@id="J_buyBtnBox"]/li[1]').click()
                    print('开始抢购...\n')
                except:
                    print('异常，退出抢购')
                    break
            else:
                print('\n\n', '还未到达抢购时间\n', '当前时间是：', time.asctime(), '\n', '抢购时间是：', self.atime, '\n\n')


if __name__ == '__main__':
    username = input('username：\n')
    pwd = input('pwd：\n')
    a = xiaomi(usernme=username, pwd=pwd)
    a.login()
    a.buy()