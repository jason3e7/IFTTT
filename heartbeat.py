# -*- encoding: utf8 -*-
import requests
import time
import socket
import urllib3
urllib3.disable_warnings()

def send_ifttt(text) :
  myData = {'value1': text}
  r = requests.post('https://maker.ifttt.com/trigger/[event]/with/key/[auth key]', data = myData)
  print(r.content)

def get_local_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 53))
  return s.getsockname()[0]

def get_public_ip() :
  r = requests.get("https://api.ipify.org/")
  return r.text

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

message = "online<br>"
message += "machine : [machine]<br>"
message += "time : " + now + "<br>"
message += "local ip : " + get_local_ip() + "<br>"
message += "public ip : " + get_public_ip() + "<br>"

send_ifttt(message)