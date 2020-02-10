import requests
from utils.responses import HttpJsonResponse


class Http(object):
    def __init__(self, url):
        self.url = url

    def get(self, uri, param, headers):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.get(http_url, param, headers=headers)
        return resp

    def post(self, uri, datas):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.post(http_url, data=datas)
        return resp

    def put(self, uri, datas):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.put(http_url, data=datas)
        return resp

    def delete(self, uri, datas):
        http_url = '%s%s' % (self.url, uri)
        resp = requests.delete(http_url, data=datas)
        return resp


class Request(object):
    def __init__(self):
        self.headers = {}

    def wx_get(self, url, params=None):
        return requests.get(
            url=url,
            params=params,
            headers=self.headers
        )

    def get(self, url, params=None):
        return self.deal_resp(requests.get(
            url=url,
            params=params,
            headers=self.headers)
        )

    def head(self, url):
        return self.deal_resp(requests.head(
            url=url,
            headers=self.headers)
        )

    # data为字典类型
    def post(self, url, data=None):
        return self.deal_resp(requests.post(
            url=url,
            json=data,
            headers=self.headers)
        )

    def put(self, url, data=None):
        return self.deal_resp(requests.put(
            url=url,
            json=data,
            headers=self.headers)
        )

    def patch(self, url, data=None):
        return self.deal_resp(requests.patch(
            url=url,
            json=data,
            headers=self.headers)
        )

    def delete(self, url, **kwargs):
        return self.deal_resp(requests.delete(
            url=url,
            headers=self.headers)
        )

    def deal_resp(self, resp):
        # return resp
        data = None
        if resp.content:
            try:
                data = resp.json()
            except:
                data = resp.content.decode()
        link = resp.headers.get('Link', None)
        r = HttpJsonResponse(data, status=resp.status_code)
        if link:
            r['Link'] = link
        return r

        # def data_get(self, url, params=None):
        #     return self.deal_data_resp(requests.get(
        #         url=url,
        #         params=params,
        #         headers=self.headers)
        #     )
        #
        # def deal_data_resp(self, resp):
        #     # return resp
        #     data = None
        #     if resp.content:
        #         try:
        #             data = resp.json()
        #         except:
        #             data = resp.content.decode()
        #     return data


new_req = Request()
