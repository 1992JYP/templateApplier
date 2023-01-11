from selenium import webdriver

edge_options = webdriver.EdgeOptions()
driver = webdriver.ChromiumEdge("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", options=edge_options)

driver.get("www.google.com")
driver.close()
quit()