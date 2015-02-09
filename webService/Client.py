# This Python file uses the following encoding: utf-8
#システムのディフォルトコードセットをUTF-８に設定、
#でないとASCIIコード直接ファイルに書き込みできない可能性が高いですから、エラー出る
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import time
from suds.client import Client
print('Service Connect...Please Wait a moment')
test = Client('http://localhost:7789/SOAP/?wsdl')
print test.service.addition(52, 87)

time.sleep(300000)