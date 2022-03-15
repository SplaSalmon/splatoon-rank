#!/opt/anaconda3/bin/python

import os
import sys
import cgi
import cgitb

path = '/opt/upload/data/'
MEGA = 1048576


def print_header():
  print('Content-Type: text/html')
  print('')
  print('<!DOCTYPE html>')
  print('')
  print('<html lang="ja">')
  print('')
  print('<head>')
  print('  <meta charset="UTF-8">')
  print('  <meta name="description" content="file upload">')
  print('  <meta name="keywords" content="upload">')
  print('  <title>画像を選択</title>')
  print('</head>')
  print('')
  print('<body>')


def print_footer():    # HTMLフッタを出力しCGIを終了
  print('</body>')
  print('')
  print('</html>')
  sys.exit(0)


cgi.maxlen = 400000000
cgitb.enable()

print_header()

form_data = cgi.FieldStorage()

file_name = form_data['foobar'].filename
full_path = path + file_name
if os.path.exists(full_path):
  print(file_name + ' already exists.<br>')
  print_footer()    # 同名ファイルが存在する場合はアップロードせずに終了
  
uploaded_file = open(full_path, 'wb')    # アップロードされたデータを保存する新規ファイルを同名で作成
item = form_data['foobar']
while True:
  chunk = item.file.read(MEGA)
  if not chunk:
    break
  uploaded_file.write(chunk)
uploaded_file.close()
print(file_name + ' has just been uploaded.<br>')    # アップロードされたことを表示

print_footer()    # HTMLフッタを表示して終了
