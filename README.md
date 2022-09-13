# 本文档持续完善中... 2022.09.13

# 说明
- 本项目为小红书个人定制网页版，出发点是方便在网页端查看小红书数据
- 仅代表个人表示强烈谴责各大公司互不联网行为
- 根据用户及个人使用情况，不定期完善项目功能
- 本项目是我本人个人网站项目的子模块(redbook)，在线预览： [科学上网](https://web-zmqcherish.vercel.app/#/redbook) 或 [IP](http://121.5.254.139/#/redbook)

# 功能说明
- 网页端展示小红书个人主页帖子
- 半自动化抓取小红书帖子
- [TODO] 增加登录功能（非小红书登录）
- [TODO] 增加收藏列表（登录后可查看）
- [TODO] 抓取帖子详情

# 准备工作 - LeanCloud
## 本项目使用LeanCloud存储及获取数据，无需单独再部署后端服务
1. 注册一个 [LeanCloud](https://www.leancloud.cn/) 账户，进入 [控制台](https://console.leancloud.cn/apps) 创建一个应用
2. 在控制台 -> 数据存储 -> 结构化数据，创建Class，并设置相应权限。这里的class名称使用英文，后续需要使用
![alt 创建Class](https://raw.githubusercontent.com/zmqcherish/redbook-web/main/imgs/lc_1.jpg)
3. 在控制台 -> 设置 -> 应用凭证 -> Credentials，获取后续python脚本及web应用需要的AppID, AppKey, MasterKey
![alt 获取相关配置](https://raw.githubusercontent.com/zmqcherish/redbook-web/main/imgs/lc_2.jpg)
4. 在控制台 -> 设置 -> 应用凭证 -> 服务器地址，获取后续web应用需要的服务器地址serverURLs
![alt 获取服务器地址](https://raw.githubusercontent.com/zmqcherish/redbook-web/main/imgs/lc_3.jpg)

# 准备工作 - python
## 使用python + mitmproxy 对小红书半自动化抓包
1. 安装python及py目录下 [requirements.txt](https://raw.githubusercontent.com/zmqcherish/redbook-web/main/py/requirements.txt)文件中的包
```
pip install -r requirements.txt
```
2. 修改py目录下 [config.py](https://raw.githubusercontent.com/zmqcherish/redbook-web/main/py/config.py)文件中的配置，包括leancloud准备工作中的class名称、AppID、AppKey、 MasterKey，以及本机的IP地址和端口号，查看本机IP命令如下
```
ipconfig
```

# 准备工作 - 小红书数据
## 使用小红书手机APP代理抓包获取数据
1. 确保手机和电脑连接的是同一个wifi网络
2. 执行python脚本
```
python redbook.py
```
3. 将手机连接电脑代理，iPhone方法为：设置 -> 无线局域网 -> (点击编辑) -> 配置代理 -> 手动 -> 填写上一步中的IP和端口号，Android手机类似，可自行查阅
4. 用Safari 浏览器访问 mitm.it 进行证书安装和信任，参考连接 [apple官网](https://support.apple.com/zh-cn/HT204477) 、[mitmproxy docs](https://docs.mitmproxy.org/stable/concepts-certificates/)
5. 在手机浏览器访问：[https://httpbin.org/json](https://httpbin.org/json)，如果出现以下结果，说明配置成功
6. 打开小红书APP进入个人主页，按顺利浏览自己主页的帖子，直到结束

# 修改web项目配置
- 修改src目录下 [main.js](https://raw.githubusercontent.com/zmqcherish/redbook-web/main/src/main.js)文件中的配置，包括leancloud准备工作中的AppID、AppKey和服务器地址serverURLs
```
AV.init({
	serverURLs: '你的服务器地址',
	appId: '你的appId',
	appKey: '你的appKey'
});
```

# 本地运行
1. 安装[node](http://nodejs.cn/)
2. 安装相关依赖包
```
npm install
```
3. 编译启动项目
```
npm run serve
```
4. 打包部署
```
npm run build
```

# 高级使用

## vercel
## github action

# 相关技术栈
- [Vue.js](https://cn.vuejs.org/)
- [MDBootstrap](https://mdbootstrap.com/)
- [LeanCloud](https://www.leancloud.cn/)
- [mitmproxy](https://mitmproxy.org/)


# 免责声明
- 此项目仅用于学习研究，不保证其合法性、准确性、有效性，请根据情况自行判断，本人对此不承担任何保证责任。
- 请勿将此项目用于任何商业或非法目的，若违反规定请自行对此负责。
