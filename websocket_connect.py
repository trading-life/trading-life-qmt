# encoding:gbk
'''
本策略事先设定好交易的股票篮子，然后根据指数的CCI指标来判断超买和超卖
当有超买和超卖发生时，交易事先设定好的股票篮子
'''
import pandas as pd
import numpy as np
import talib
import json
import websocket as wsc


class MessagePackage:
	def __init__(self, code, msg):
		self.code = code
		self.msg = msg


def to_json(msg: MessagePackage):
	if msg:
		# 将对象转换为字典
		msg = msg.__dict__

		# 将字典转换为 JSON 字符串
		json_string = json.dumps(msg)
		return json_string
	return None


def on_message(ws, message):
	print("-----start---------")
	print(message)

	ws.send("Hello, World")
	print("-----end---------")


def on_error(ws, error):
	print("-----error start---------")
	print(error)
	print("-----error end---------")


def on_close(ws, close_status_code, close_msg):
	print("-----on_close start---------")
	print("# closed #")
	print("-----on_close end---------")


def on_open(ws):
	print("-----on_close start---------")
	ws.send(to_json(MessagePackage("login", "你好")))
	print("# on_open #")
	print("-----on_close end---------")


def on_opennn(ContextInfo):
	print("on_opennn")


def init(ContextInfo):
	print("hello")
	ws = wsc.WebSocketApp("ws://127.0.0.1:10008/ws/message", on_message=on_message, on_error=on_error,
						  on_close=on_close, on_open=on_open, header={"CustomHeader1": "你好", "NewHeader2": "Test"})
	ws.run_forever()
	print("hwllo")
