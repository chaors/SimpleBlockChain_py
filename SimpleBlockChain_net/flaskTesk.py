from flask import Flask

app = Flask(__name__)

@app.route('/')  #映射根目录
def hello_world():
    return 'this is a chainNode!'  #返回网页信息

@app.route('/zhangsan')  #映射根目录
def node_zhangsan():
    return '张三的区块链节点'  #返回网页信息

@app.route('/lisi')  #映射根目录
def node_lisi():
    return '李四的区块链节点'  #返回网页信息

@app.route('/wangwu')  #映射根目录
def node_wangwu():
    return '王五的区块链节点'  #返回网页信息

if __name__ == '__main__':
    app.run()
