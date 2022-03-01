#coding=utf-8
'''
对象库层
    定位元素
'''
from Register51Test.until.read_ini import ReadIni
class FindElement(object):

    def __init__(self,driver,key_el):
        self.driver = driver
        self.key_el = key_el

    def get_element(self):
        data = ReadIni().read_ini(self.key_el)
        key = data.split('>')[0]
        value = data.split('>')[1]
        return key,value

    def locate_element(self):
        key,value = self.get_element()
        try:
            el = self.driver.find_element(key,value)
            return el
        except:
            return None



