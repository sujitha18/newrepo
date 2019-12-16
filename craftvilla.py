from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.craftsvilla.com/")
driver.find_element_by_xpath("//a[text()='KURTIS & DRESSES ']").click()
driver.find_element_by_xpath("//label[@title='2000-5000']").click()
list_of_prices=driver.find_elements_by_xpath("//span[@class='product-offer-price']")
x=0
for i in list_of_prices:
    t=i.text
    print(t)
    x=int(t[2:])

assert x>=2000 and x<=5000,"False"
"True"

driver.close()