#-*- coding: cp949 -*-
import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors

model_no = "42039"

connect = pymysql.connect(host = 'localhost',
                          user='root', 
                          password='apmsetup', 
                          database='python')

try:
    with connect.cursor() as cursor:
        sql = "select model_url, model_class, basket_class from lego_info where model_no = %s"
        cursor.execute(sql, (model_no))
        result = cursor.fetchone()
        #print(result)
finally:
    connect.close()
    
'''
#this_url = "http://shop.lego.com/ko-kr/product/?p=42039"
#this_url = "http://shop.lego.com/en-US/product/?p=42039"
#model_class = 'product-price test-unit-price-42039'
#basket_class = 'add-to-cart btn-big orange test-addToCart'
'''
this_url = result[0]
model_class = result[1]
basket_class = result[2]

try:
    html = urllib.request.urlopen(this_url)
    data = html.read()
    soup = BeautifulSoup(data, "html.parser")
    
    basket_article = soup.findAll('button',attrs={'class': basket_class})
    price_article = soup.findAll('span',attrs={'class': model_class})
    
    if not basket_article:
        print('sold out')
    else:
        print(basket_article[0].text)
    
    print(price_article[0].find('em').text)
    
except Exception as exception:
    print(exception)
    
finally:
    pass
