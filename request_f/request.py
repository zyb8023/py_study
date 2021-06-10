import requests;
import json;
from PIL import Image
from requests.api import request;
from io import BytesIO;

def demo_get():
  """模仿浏览器，请求api信息"""
  url = 'http://www.weather.com.cn/data/sk/101010100.html';
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
  }
  request = requests.get(url, headers = headers);
  html_text = request.text;
  file = open('json.json', 'w', encoding='utf-8');
  json.dump(html_text, file, ensure_ascii=False);
  print(html_text);

def get_image():
  ulr = 'https://imusae-download.90sheji.com/imusae/download/2021/05/20/32b6462d6b9d611479e8b931f86f02c1.png!t125?sign=bca1105d1e6ff7b3a12f5206f1ebf519&t=61042200';
  request = requests.get(ulr);
  i = Image.open(BytesIO(request.content))
  i.save('demo.png');
  i.show();
  i.close();
  pass;

if __name__ == '__main__':
  #  demo_get();
   get_image();
   pass;
