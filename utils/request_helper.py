import requests


class Http(object):
    def __init__(self, url):
        self.url = url

    def GET_info(self, uri, param, headers):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.get(http_url, param, headers=headers)
        return resp

    def POST_info(self, uri, datas):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.post(http_url, data=datas)
        return resp

    def PUT_info(self, uri, datas):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.put(http_url, data=datas)
        return resp

    def DELETE_info(self, uri, datas):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.delete(http_url, data=datas)
        return resp


