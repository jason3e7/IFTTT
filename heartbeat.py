# -*- encoding: utf8 -*-
import requests
import time
import socket
import fcntl
import struct

import urllib3
urllib3.disable_warnings()
import os

# config 
event = "event"
authKey = "auth key"
machine = "machine"
ni = [] # 'eth0'
###

def send_ifttt(text) :
  myData = {'value1': text}
  r = requests.post("https://maker.ifttt.com/trigger/" + event + "/with/key/" + authKey, data = myData)
  print(r.content)

def get_local_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 53))
  return s.getsockname()[0]

def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  return socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915,  # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
  )[20:24])

def get_public_ip() :
  r = requests.get("https://api.ipify.org/")
  return r.text

def get_pppoe_ip() :
  temp = os.popen("ifconfig ppp0 | grep 'inet' | awk '{print $2}'")
  data = temp.read()
  temp.close()
  return data

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

message = "online<br>"
message += "machine : " + machine + "<br>"
message += "time : " + now + "<br>"
message += "local ip : " + get_local_ip() + "<br>"
message += "public ip : " + get_public_ip() + "<br>"

if ni :
  for iface in ni :
    message += iface + " : " + get_ip_address(iface) + "<br>"

send_ifttt(message)
