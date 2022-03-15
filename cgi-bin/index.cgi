#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#上のpathは環境に合わせてください 
import cgi
import base64
print("Content-Type: text/html; charset=UTF-8")
print("")
form = cgi.FieldStorage()
img = form.getvalue("imagefile")
after_encode = base64.b64encode(img)
after_encode = str(after_encode)
after_encode = after_encode.replace("b'","")
after_encode = after_encode.replace("'","")
print("<img src='data:image/jpeg;base64,{0}'>".format(after_encode))
