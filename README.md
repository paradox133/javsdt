# jav-standard-tool 简称javsdt
# 作者为生活所迫，已经跑路...
简介：收集jav元数据，并规范本地文件（夹）的格式，收集女优头像，为emby、kodi、jellyfin、极影派等影片管理软件铺路。  

  
## 1、【一般用户】下载及群链接：  
目前2020年5月30日更新的1.1.1版本  推荐使用环境win10 64位  
[从蓝奏云下载](https://junerain.lanzous.com/id6ilbe) 或者 [从github下载](https://github.com/javsdt/javsdt/releases/tag/V1.1.1)
  
[前往下载演员头像](https://github.com/javsdt/javsdt/releases/tag/女优头像)   
  
[电报群](https://t.me/joinchat/PaHhgBaleu_qEgFy_NJlIA)  
[企鹅群](https://jq.qq.com/?_wv=1027&k=5CbWOpV)（需要付费1人民币扩群）  
  
## 2、[使用说明(还没写完)](https://github.com/javsdt/javsdt/wiki)  
[旧版的使用说明从蓝奏云下载](https://www.lanzous.com/ib0qozg)  

## 3、【其他开发者】运行环境：  
  python3.7.6 发行版是pyinstaller打包的exe  
    pip install requests  
    pip install Pillow  
    pip install baidu-aip  
    pip install pysocks  
    pip install [cloudscraper](https://github.com/VeNoMouS/cloudscraper)  
   几个jav的py都是独立执行的，加了很多很多注释，希望能理解其中踩过的坑。  
   
## 4、工作流程：  
    （1）用户选择文件夹，遍历路径下的所有文件。  
    （2）文件是jav，取车牌号，到javXXX网站搜索影片找到对应网页。  
    （3）获取网页源码找出“标题”“导演”“发行日期”等信息和DVD封面url。  
    （4）重命名影片文件。  
    （5）重命名文件夹或建立独立文件夹。  
    （6）保存信息写入nfo。   
    （7）下载封面url作fanart.jpg，裁剪右半边作poster.jpg。   
    （8）移动文件夹，完成归类。  
  
## 5、目标效果：  
...
  
## 6、ini中的用户设置：  
![image](https://github.com/javsdt/images/blob/master/jav/javsdt/readme/ini%E8%AE%BE%E7%BD%AE.PNG?raw=false)  
  
## 7、其他说明：  
（1）不需要赞助；  
（2）允许对软件进行任何形式的转载；  
（3）代码及软件使用“MIT许可证”，他人可以修改代码、发布分支，允许闭源、商业化，但造成后果与本作者无关。  
