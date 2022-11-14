import json


class Response:
    def __init__(self, code=0, msg='', content=[]):
        if type(code) == int:
            self.code = code

        if type(msg) == str:
            self.message = msg

        if type(content) == list:
            self.content = content

    def format(self):
        return json.dumps(
            {
                'code': self.code,
                'message': self.message,
                'content': self.content,
            }
        )
