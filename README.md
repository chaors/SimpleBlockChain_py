# SimpleBlockChain
用Python从零到一创建一个简单的区块链

#前言
比特币在2017可谓是十足地火爆了，那他背后依赖的区块链技术又是如何实现的呢？当下对区块链人才的需求更是迫切中的迫切，或许在2018将火爆各个行业。

本次系列文章将从实际代码出发，来构建你对区块链技术的认知。

#写代码之前
###基础技能要求
```
1.简单的Python基础
2.面向对象编程思维
4.区块链基本定义
```

###开发环境准备
#####1.Python3.6
Mac自带的Python为2.7，这里我们需要重新安装Python3.6
1.1确保电脑安装了套件管理工具 Homebrew，如果没有请在命令行执行以下命令安装：
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
1.2 验证是否安装成功,该命令也可以检验电脑是否安装了Homebrew
```
brew doctor
```
1.3安装Python3.6
```
brew install python3
```
1.4查看Python路径
```
// 系统自带的python2.7，目录为/usr/bin/python
which python
//brew安装的python3.4,目录为/usr/local/bin/python3
which python3
```
![1.4查看Python路径.png](http://upload-images.jianshu.io/upload_images/830585-610e86c3ec398a82.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1.5使用
```
// 系统自带的
python a.py
//brew安装的
python3 a.py
```
#####2.python包管理工具:Pip
一般我们安装python3时自带了Pip，如果没有在命令行用HomeBrew安装：
```
brew install pip
```
2.1 配置[pipenv](https://github.com/kennethreitz/pip):
```
//安装 pipenv
pip install pipenv 
```
```
//创建virtual env
pipenv --python=python3.6
```

```
//安装依赖
pipenv install
```
#####3.Python IDE
这一项不是必须的，我们可以在命令行vi或记事本里写python代码。当然习惯使用IDE的童鞋也可以选择使用IDE，笔者这里使用的Python IDE为[Pycharm专业版](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac)(自行百度PoJie教程）



