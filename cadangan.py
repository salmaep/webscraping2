from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request

s = Service("E:\DATA DOKUMEN\POLBAN\semester 2\Proyek 1  Pengembangan Perangkat Lunak Desktop\Tugas\P-Minggu 6\Tugas 6.3 web scraping\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get("https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=3Q3DFG6PKPAAJW8DW42G&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_6")

i = 1

for tvshowlist in driver.find_elements(By.CLASS_NAME, "lister-list"):
    print(tvshowlist.text)
    for img in tvshowlist.find_elements(By.TAG_NAME, "img"):
        print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
        i = i+1

driver.quit()
