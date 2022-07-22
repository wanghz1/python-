from urllib.request import urlopen  # 从urllib.request模块中导入urlopen模块


url = "http://www.baidu.com"
resp = urlopen(url)

with open("baidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))  # 读取网页的页面源代码
