import jwt

class Token(object):
    '''
    python jwt common class
    '''
    secret_key = None
    algorithm = 'HS256'

    def __init__(self, secret_key=None, algorithm=None):
        self.secret_key = secret_key
        self.algorithm = algorithm or self.algorithm

    def get(self, payload=None):
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def decode(self, token=None):
        payload = jwt.decode(token, key=self.secret_key, algorithms=[self.algorithm])
        return payload


if __name__ == '__main__':
    jwt_parser = Token(secret_key='12321312eqwasd12312121')
    token = (jwt_parser.get(payload={'a': 'b'}))
    payload = jwt_parser.decode(token=token)
    print (token)
    print (payload)