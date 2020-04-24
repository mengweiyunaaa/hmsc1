import hashlib,base64
class UserService():
    # salt+md5 加密
    @staticmethod
    def generatePwd(pwd,salt):
        m = hashlib.md5()
        str='%s-%s'%(base64.encodebytes(pwd.encode('utf-8')),salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()
    # cooki中信息加密
    @staticmethod
    def genearteAuthCode(user_info=None):
        m = hashlib.md5()
        str = '%s-%s-%s-%s'%(user_info.uid,user_info.login_name,user_info.login_pwd,user_info.login_salt)
        m.update(str.encode('utf-8'))
        return m.hexdigest()


