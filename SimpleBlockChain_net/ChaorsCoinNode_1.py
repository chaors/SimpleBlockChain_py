# 节点的数据更新和网络公示

from uuid import uuid4  # 签名
import requests  # 网络请求
from flask import Flask, jsonify, request  # flask网络框架

from ChaorsCoinBlockChain import ChaorsCoinBlockChain

chaorsCoin = ChaorsCoinBlockChain()  # 创建一个网络节点
node_id = str(uuid4()).replace("-", "")  # 生成节点秘钥
print("当前节点钱包地址:", node_id)

app = Flask(__name__)  # 初始化flask框架


@app.route("/")
def index_page():
    return "welcome to ChaorsCoin..."


@app.route("/chain")  # 查看所有区块链
def index_chain():
    response = {
        "chain": chaorsCoin.chain,  # 区块链
        "length": len(chaorsCoin.chain)  # 区块链长度
    }
    return jsonify(response), 200


@app.route("/mine")  # 挖矿
def index_mine():
    last_block = chaorsCoin.last_block
    proof = chaorsCoin.proof_of_work(last_block)

    # 系统奖励比特币
    chaorsCoin.new_transaction(
        sender="0",  # 0代表系统奖励,即coinBaseTransaction
        recipient=node_id,
        amount=12.5
    )

    block = chaorsCoin.new_block(proof, chaorsCoin.hash(last_block))  # 新增区块

    response = {
        "message": "new block created...",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "hash": chaorsCoin.hash(block),
        "prev_hash": block["prev_hash"]
    }
    return jsonify(response), 200


@app.route("/new_transcations", methods=["POST"])  # 创建一个新的交易
def index_new_transcations():
    values = request.get_json()  # 抓取网络传输的信息
    required = ["sender", "recipient", "amount"]

    print(values, required)
    if not all(key in values for key in required):
        return "数据不完整", 400

    index = chaorsCoin.new_transaction(values["sender"],
                                       values["recipient"],
                                       values["amount"])  # 新增交易

    response = {
        "message": f"交易加入到区块{index}"
    }

    return jsonify(response), 200


@app.route("/new_node", methods=["POST"])  # 新增节点
def index_new_node():
    values = request.get_json()
    nodes = values.get("nodes")  # 获取所有节点

    if nodes is None:
        return "怎么是空节点"

    for node in nodes:
        chaorsCoin.register_node(node)

    response = {
        "message": "网络节点加入到区块",
        "nodes": list(chaorsCoin.nodes)
    }

    return jsonify(response), 200


@app.route("/node_refresh")  # 刷新节点
def index_node_refresh():
    replaced = chaorsCoin.resolve_conflicts()  # 一致性算法进行最长链选择

    if replaced:
        response = {
            "message": "区块链被替换为最长有效链",
            "new chain": chaorsCoin.chain
        }
    else:
        response = {
            "message": "当前区块链为最长无需替换",
            "chain": chaorsCoin.chain
        }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run("127.0.0.1", port=5006)


