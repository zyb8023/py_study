#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json;
if __name__ == '__main__':
  """解读字符串拼装成json写入文件，方便其他语言解析数据"""
  file_path = 'json.txt';
  with open(file_path, 'r', encoding='utf-8') as file_obj:
    all_file = file_obj.readlines();
    data = [];
    for line in all_file:
      line_info = line.split(',');
      if line_info:
        info = {'name': line_info[0], 'url': line_info[1].replace('\n', '')};
        data.append(info);
    file_obj.close();
    print(data, '----data')
    file = open('json.json', 'w', encoding='utf-8');
    json.dump(data, file, ensure_ascii=False);