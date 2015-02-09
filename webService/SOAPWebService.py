# This Python file uses the following encoding: utf-8
#システムのディフォルトコードセットをUTF-８に設定、
#でないとASCIIコード直接ファイルに書き込みできない可能性が高いですから、エラー出る
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import soaplib
from soaplib.core.server import wsgi
from soaplib.core.service import DefinitionBase  # All the Service Class should be extends from this Class
from soaplib.core.service import soap
from soaplib.core.model.clazz import Array
from soaplib.core.model.clazz import ClassModel  #if return class ,the class should be extends from ClassModel
from soaplib.core.model.primitive import Integer, String

# the returned Class from this WebService
class C_ProbeCdrModel(ClassModel):
        __namespace__ = "C_ProbeCdrModel"
        Name=String
        Id=Integer

#this is a web service
class AdditionService(DefinitionBase):
    @soap(Integer, Integer, _returns=String)  #関数を定義する前に、必ずこの様なパラメータ値のタイプを指定しなければならない
    def addition(self, a, b):
        return str(a) + '+' + str(b) + '=' + str(a+b)

    #ブロックがインデントで別けます
    @soap(_returns=Array(String))
    def GetCdrArray(self):
        L_Result = ["1", "2", "3"]
        return L_Result

    @soap(_returns=C_ProbeCdrModel)
    def GetCdr(self):
        L_Model = C_ProbeCdrModel()
        L_Model.Name = L_Model.Name
        L_Model.Id = L_Model.Id
        return L_Model

if __name__ == '__main__':
    try:
                print 'This service has started!'
                from wsgiref.simple_server import make_server
                soap_application = soaplib.core.Application([AdditionService], 'tns')
                wsgi_application = wsgi.Application(soap_application)
                server = make_server('localhost', 7789, wsgi_application)
                server.serve_forever()

    except ImportError:
                print 'error'