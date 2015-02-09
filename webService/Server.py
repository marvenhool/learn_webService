# This Python file uses the following encoding: utf-8
#システムのディフォルトコードセットをUTF-８に設定、
#でないとASCIIコード直接ファイルに書き込みできない可能性が高いですから、エラー出る
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.send_response(200)
        enc = 'UTF-8'
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        strs = 'My first Server! it Works!'
        self.send_header("Content-Length", str(len(strs)))
        self.end_headers()
        self.wfile.write(strs)


httpd = HTTPServer(('', 8080), MyHTTPHandler)
print("Server started port 8080.....")
httpd.serve_forever()  #サーバーを起動します
