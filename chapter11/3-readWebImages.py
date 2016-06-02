import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# 创建新的 Selenium Driver
# driver = webdriver.PhantomJS(executable_path='/Users/ChowHungLou/phantomjs/bin/phantomjs')
# 有时我发现 PhantomJS 查找元素有问题, 但是 Firefox 没有
# 如果你运行程序时出现问题, 去掉下面这行注释,
# 用 Selenium 试试 Firefox 浏览器:
driver = webdriver.Firefox()

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# 单击图书预览按钮
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# 等待页面加载完成
time.sleep(5)

# 当向右箭头点击时, 开始翻页
print(driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"))
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已加载的新页面 (一次可以加载多个页面，但是重复的页面不能加载到集合中)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

# 用 Tesseract 处理我们收集的图片 URL 链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
