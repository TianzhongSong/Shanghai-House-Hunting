一个上海租房选择程序 (Python爬虫+高德API)

参考[实验楼Python爬虫+高德api解决租房问题](https://www.shiyanlou.com/courses/599)

抓取了链家、安居客、58同城、赶集网、房天下五个网站上海所有租房信息。

下载：

git clone git://github.com/TianzhongSong/Shanghai-House-Hunting.git && cd Shanghai-House-Hunting

pip install -r requirements.txt

运行：
python crawl.py

等待数据抓取完毕

python -m http.server 3000

然后打开浏览器，在地址栏输入：localhost:3000 打开网页。

先选择工作地点，然后选择交通方式，接着加载下载好的房源文件（.csv），最后选择地图上的一个房源，点击房源会跳转到对应的链接。

![](https://github.com/TianzhongSong/Shanghai-House-Hunting/blob/master/0.png)

![](https://github.com/TianzhongSong/Shanghai-House-Hunting/blob/master/1.png)

![](https://github.com/TianzhongSong/Shanghai-House-Hunting/blob/master/2.png)



