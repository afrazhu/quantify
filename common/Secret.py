from sqlalchemy import create_engine


class Secret(object):
    class SecretError(TypeError):
        pass

    class SecretCaseError(SecretError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.SecretError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.SecretCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value


secret = Secret()

secret.TOKEN = "0b8f33e64a5558e84bd5b7499d0d0d6417d11d7db5d7ae960889f00e"
secret.DB_HOST = '127.0.0.1'
secret.DB_PORT = 3307
secret.DB_USER = 'root'
secret.DB_PWD = '123456'
secret.DB_NAME = 'quantify'
secret.ENGINE = create_engine('mysql+pymysql://root:123456@127.0.0.1:3307/quantify?charset=utf8')