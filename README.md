# SpiderTemp
各种爬虫和PyQt的实例
-------------------
严格来说，除了煎蛋的那个demo外，其它的都算不上爬虫。

## Girls
[图片原地址](http://gank.io/)
这里下载图片会根据当前的路径，新建一个名为girls的文件夹，所有的下载图片都在这个文件夹里面
- Girls.py - 抓取gank.io的图片，事实上这里是gank.io提供的接口，根据接口去循环拉取里面的图片
- PackGirls.py - 用py2exe打包Girls.py的代码，事实上用pyinstaller打包会简单很多。
- 其它的都是一些无关紧要的。
## TBGirls
 [图片原地址](https://mm.taobao.com/json/request_top_list.htm?page=1)
 这里由于进一步抓取图片后，发现HTML里面关于相册的那一步里面使JS代码，所以这里暂时不打算研究脚本抓取执行JS获得的动态信息。
 - TBGirls.py 这里是抓取网站里面的数据，这里能抓取到相册所在界面去，但是相册部分是JS，所以就这样了，以后深入会回来修改的
 - Spider.py 这里是抓取[图虫](https://tuchong.com/3/albums)的图片，问题同上。
 ## WallHaven
 [图片原地址](https://alpha.wallhaven.cc/)
 这里是抓取著名图片网站[WallHaven](https://alpha.wallhaven.cc/)的图片，里面有很多小黄图。。
 - WallHaven.py 无限抓取WallHaven网站里面的图片，图片会放在新建的wallpapers文件夹下。
 - WallHavenPack.py 这里是打包上面的WallHaven.py文件，打包成EXE，这里用的是pyinstaller
 ## WeiChat
 这里是准备用Python玩一玩微信的网页登录的，但是同上面的TBGirls一样，卡在JS这里的，因为微信的登录二维码图片是用js动态获取的。
- weixin.py 微信登录的Python源码，
## jiandan
[图片原地址](http://jandan.net/ooxx)
煎蛋里面多是有一些黄黄的图片，但是这里是用爬虫的而技术，需要自己分析HTML源码。采用正则表达式去匹配，这里采用三方的html分析工具来爬取。
- jiandan_spider.py 爬取煎蛋的女孩儿图片，[代码原地址](https://github.com/kulovecc/jandan_spider)
## FaceClient.py
这个是采用百度AI开放平台的API，实现人脸识别的工具，里面的APPkey，secret我都没抹去，希望看到的伙伴不要乱用。
