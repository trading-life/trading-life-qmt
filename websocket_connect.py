# encoding:gbk
'''
�����������趨�ý��׵Ĺ�Ʊ���ӣ�Ȼ�����ָ����CCIָ�����жϳ���ͳ���
���г���ͳ�������ʱ�����������趨�õĹ�Ʊ����
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
		# ������ת��Ϊ�ֵ�
		msg = msg.__dict__

		# ���ֵ�ת��Ϊ JSON �ַ���
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
	ws.send(to_json(MessagePackage("login", "���")))
	print("# on_open #")
	print("-----on_close end---------")


def on_opennn(ContextInfo):
	print("on_opennn")


def init(ContextInfo):
	print("hello")
	ws = wsc.WebSocketApp("ws://127.0.0.1:10008/ws/message", on_message=on_message, on_error=on_error,
						  on_close=on_close, on_open=on_open, header={"CustomHeader1": "���", "NewHeader2": "Test"})
	ws.run_forever()
	print("hwllo")
