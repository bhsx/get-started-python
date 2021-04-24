import datetime
import re

import json
import requests


class Pan:
    def __init__(self):
        self.session = requests.session()
        self.token = ""

    def pan_login(self):
        cookies = {
            'think_language': 'zh-cn',
            'gksource': '%5B%22deploy%22%5D',
            'cookie_dispatch': '%2Fweb%2Findex',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://pan.gzmtr.cc',
            'Referer': 'http://pan.gzmtr.cc/login?code=40106',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        data = {
            'account': 'deploy\\zengqinglin2',
            'password': 'QngxMDY0Mjk=',
            'remember': '0',
            'verify_code': ''
        }

        response = self.session.post('http://pan.gzmtr.cc/account/login_submit', headers=headers, cookies=cookies,
                                     data=data, verify=False)
        print(response.text)
        print(response.status_code)

        if response.status_code == 200:
            return True
        else:
            return False

    def pan_gettoken(self):

        cookies = {
            'think_language': 'zh-cn',
            'account': '25641',
            'gksource': '%7B%220%22%3A%22deploy%22%2C%2225641%22%3A%22deploy%22%7D',
            'io': 'yhicfecaTkcTrwLTAB1p',
            'remember': '1612082192',
            'gkorguinfo': '6ab0QF6BMonWYJkT1wYyZD8uPgXVudnoNfXslIT79Pi4uF7x3enjzByNgvVpgMJfYDyyksugAiBdOuaZLU7TiX2pmfSOzQyVFvG3FquHiKuHSiXibyRieAgTx%2B5LtVl%2Bg0nfAvZy',
        }

        headers = {
            'Proxy-Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://pan.gzmtr.cc/login?code=40106',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        response = self.session.get('http://pan.gzmtr.cc/web/index', headers=headers, cookies=cookies, verify=False)
        # print(response.text)
        for i in re.finditer('token":"([^"]+)"', response.text):
            self.token = (i.group(1))
            print(self.token)
            break

    def pan_download(self, hash_=''):
        # import requests

        cookies = {
            'think_language': 'zh-cn',
            'account': '25641',
            'gksource': '%7B%220%22%3A%22deploy%22%2C%2225641%22%3A%22deploy%22%7D',
            'gkorguinfo': 'c15cMECDZO7LwxKr4VaZpT1u6WDWH67DqqO%2BIRv%2FGJKcgRLqyevsUTkD0x9Q9VPJ8tS6dIjQ7RBNq4fcXvxXLcjOv6hVCInT5RBpB%2FyAOxlCAA2qYEfRVgvetNmCmbkRN4NePNWA',
            'remember': '1612080755',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://pan.gzmtr.cc/web/index',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        if len(hash_) == 0:
            hash_ = 'd2b84b605606bbfca7ebf0e5a07de194267000a8'
        params = (
            ('mount_id', '15027'),
            ('hash', hash_),
        )

        # params = (
        #     ('mount_id', '15027'),
        #     ('hash', '08b5c9e50814f4c09a64680bc8263e217a75123c'),
        # )

        response = self.session.get('http://pan.gzmtr.cc/down', headers=headers, params=params, cookies=cookies,
                                    verify=False)

        print(response.status_code)
        print(response.text)

    def pan_getlist(self, file=""):

        cookies = {
            'gksource': '%7B%220%22%3A%22deploy%22%2C%2225641%22%3A%22deploy%22%7D',
            'think_language': 'zh-cn',
            'account': '25641',
            'gkorguinfo': '8895vw6esOUJoZ1HNRdO3tpngEMNzgbWDGlrBO80U3lbtEEvrIF0P%2F6Jjuk8N1Ra7tfVduKWlM7u3uVnvMn8XJqyMP037ZLkIz0VtOHUqn6Xi3xg319EGu44MEB7M7EYBcwSeqY',
            'io': '_nMI_Wh08Wmxmmr1ABnk',
        }
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://pan.gzmtr.cc/file/hur5uk7ct706pbkrinw3kgex3sf68c02',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        params = (
            ('start', '0'),
            ('fullpath', ''),
            ('order', 'filename asc'),
            ('show_del', ''),
            ('display', 'list'),
            ('mount_id', '0'),
            ('code', 'hur5uk7ct706pbkrinw3kgex3sf68c02'),
            ('file', file),
            ('keyword', ''),
        )

        response = self.session.get('http://pan.gzmtr.cc/index/link_file_list', headers=headers, params=params,
                                    cookies=cookies, verify=False)
        print(response.text)
        findall1 = re.findall("\?hash=([^&]+)&", response.text)
        # print(findall1)
        findall2 = re.findall("data-fullpath=\\\\\"([^\"]+)\\\\\"", response.text)
        # print(findall2)
        findall3 = re.findall("<td>(\d\d\d\d/\d\d/\d\d \d\d:\d\d)</td>", response.text)
        # print(findall3)
        res_t = list(zip(findall1, findall2, findall3))
        res = []
        for i in res_t:
            res.append({"hash": i[0], "file": i[1], "time": i[2]})

        for i in res:
            print(i)
        return res

    @staticmethod
    def pan_link_to_password(link_='hur5uk7ct706pbkrinw3kgex3sf68c02', password_='1'):

        cookies = {
            'gksource': '%7B%220%22%3A%22deploy%22%2C%2225641%22%3A%22deploy%22%7D',
            'account': '25641',
            'think_language': 'zh-cn',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://pan.gzmtr.cc',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://pan.gzmtr.cc/file/hur5uk7ct706pbkrinw3kgex3sf68c02',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        data = {
            'password': password_
        }

        response = requests.post('http://pan.gzmtr.cc/file/' + link_, headers=headers,
                                 cookies=cookies, data=data, verify=False)
        text = response.text
        # print(text)
        re_findall = re.findall("gkFiles.link.outer.init\({([^}]+)}\)", text)
        i: str
        dict_: dict = {}
        for i in re_findall:
            findall__ = re.findall("(\S+): \"(\S+)\",", i)
            for j, k in findall__:
                dict_[j] = k
        # n__replace = eval(n__replace)
        # print((n__replace))
        return dict_

    @staticmethod
    def pan_getlist_for_pwd(link_, dict_, file_name_):

        cookies = {
            'gksource': '%7B%220%22%3A%22deploy%22%2C%2225641%22%3A%22deploy%22%7D',
            'think_language': 'zh-cn',
            'account': '25641',
            'gkorguinfo': '9eb5KPVjU6OdDPyIDLwk9mcLEmg9Fsc7qN0GRa9glr%2BzZ7j%2B3faTCPf4Rcld5w8wcm6Dn3JJrQLZ62i7%2BmPPu8MJ9rXjvUzDb7o1a5EnE1p5zYjq3SWX2N3MScOVKTAyPC4',
        }

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'http://pan.gzmtr.cc',
            'Referer': 'http://pan.gzmtr.cc/file/hur5uk7ct706pbkrinw3kgex3sf68c02',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        params = (
            ('code', 'hur5uk7ct706pbkrinw3kgex3sf68c02'),
            ('t', '1611649849'),
            ('s', 'FltAtMI1ojVAAvTDkysrtODeoiA='),
        )
        params = (
            ('code', link_),
            ('t', dict_['dateline']),
            ('s', dict_['sign']),
        )

        response = requests.post('http://pan.gzmtr.cc/index/open_link_download', headers=headers, params=params,
                                 cookies=cookies, verify=False)
        text = json.loads(response.text)
        print(text)
        list_ = json.loads(text['list'])
        # for i in list_:
        #     print(i)
        list1 = [i for i in list_ if i['filename'] == file_name_]
        print(list1)
        text['list'] = list1
        print(json.dumps(text))
        return list1

    @staticmethod
    def pan_upload_for_pwd(link_, password, path='班表1', filename='advs.txt', data_=''):

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryZkFJIyxiTW8rZON2',
            'Accept': '*/*',
            'Origin': 'http://pan.gzmtr.cc',
            'Referer': 'http://pan.gzmtr.cc/index/open_link_upload?uploadParams=%257B%2522path%2522%253A%2522%2522%252C%2522code%2522%253A%2522hur5uk7ct706pbkrinw3kgex3sf68c02%2522%252C%2522filefield%2522%253A%2522file%2522%257D&stopCallback=gkFiles.afterUpload&fullpath=&code=hur5uk7ct706pbkrinw3kgex3sf68c02',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        data = '$------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="path"\\r\\n\\r\\n\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="code"\\r\\n\\r\\nhur5uk7ct706pbkrinw3kgex3sf68c02\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="filefield"\\r\\n\\r\\nfile\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="op_id"\\r\\n\\r\\n0\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="id"\\r\\n\\r\\nWU_FILE_0\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="name"\\r\\n\\r\\ngzmtr_edu_main.py\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="type"\\r\\n\\r\\ntext/plain\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="lastModifiedDate"\\r\\n\\r\\nMon Feb 01 2021 12:51:44 GMT+0800 (\u4E2D\u56FD\u6807\u51C6\u65F6\u95F4)\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="size"\\r\\n\\r\\n3263\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="overwrite"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="file"; filename="gzmtr_edu_main.py"\\r\\nContent-Type: text/plain\\r\\n\\r\\n\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2--\\r\\n'
        data = '$------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="path"\\r\\n\\r\\n\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="code"\\r\\n\\r\\n{link}\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="filefield"\\r\\n\\r\\nfile\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="op_id"\\r\\n\\r\\n0\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="id"\\r\\n\\r\\nWU_FILE_0\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="name"\\r\\n\\r\\n{filename}\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="type"\\r\\n\\r\\ntext/plain\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="lastModifiedDate"\\r\\n\\r\\nMon Feb 01 2021 12:51:44 GMT+0800 (\u4E2D\u56FD\u6807\u51C6\u65F6\u95F4)\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="size"\\r\\n\\r\\n3263\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="overwrite"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2\\r\\nContent-Disposition: form-data; name="file"; filename="{filename}"\\r\\nContent-Type: text/plain\\r\\n\\r\\n{file_data}\\r\\n------WebKitFormBoundaryZkFJIyxiTW8rZON2--\\r\\n'.format(
            path=path, filename=filename, file_data=data_, link=link_)
        # print(data)
        data = re.sub(r'\\r\\n', r'\r\n', data)

        # data = '$------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="member_id"\r\n\r\n25641\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="path"\r\n\r\n{path}\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="mount_id"\r\n\r\n15027\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="filefield"\r\n\r\nfile\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="token"\r\n\r\n{token}\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="id"\r\n\r\nWU_FILE_1\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="name"\r\n\r\nadvs.txt\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="type"\r\n\r\ntext/plain\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="lastModifiedDate"\r\n\r\nSun Jan 24 2021 16:19:33 GMT+0800 (\u4E2D\u56FD\u6807\u51C6\u65F6\u95F4)\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="size"\r\n\r\n2\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="overwrite"\r\n\r\n1\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: text/plain\r\n\r\n{file_data}\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN--\r\n'.format(
        #     path='班表1', token=self.token, filename='advs.txt', file_data=data_)

        response = requests.post('http://panstorage.gzmtr.cc:8092/web_upload', headers=headers, data=data.encode(),
                                 verify=False)
        print(response.text)
        pass

    @staticmethod
    def pan_download_for_pwd(list_):

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://pan.gzmtr.cc',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://pan.gzmtr.cc/file/hur5uk7ct706pbkrinw3kgex3sf68c02',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        data = {
            'list': json.dumps(list_)
        }

        response = requests.post('http://panstorage.gzmtr.cc:8092/file/download_zip/%E7%8F%AD%E8%A1%A81.zip',
                                 headers=headers, data=data, verify=False)
        download_ = response.content

        import zipfile
        import io
        buff_file = zipfile.ZipFile(io.BytesIO(download_))
        for i in buff_file.filelist:
            print(i)
            # print(buff_file.read(i))
            return buff_file.read(i)
        return None

    def pan_upload(self, file_data):

        headers = {
            'Proxy-Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJ3pFR3AlykeqrrDN',
            'Accept': '*/*',
            'Origin': 'http://pan.gzmtr.cc',
            'Referer': 'http://pan.gzmtr.cc/mount/upload?uploadParams=%257B%2522member_id%2522%253A25641%252C%2522path%2522%253A%2522%2522%252C%2522mount_id%2522%253A15027%252C%2522filefield%2522%253A%2522file%2522%257D&stopCallback=gkSiteCallback.UpdateFileList&redirectURL=http%3A%2F%2Fpan.gzmtr.cc%2Findex%2Fupload_cb%3F&fullpath=&mount_id=15027&from=web_fengcloud',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        data = '$------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="member_id"\r\n\r\n25641\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="path"\r\n\r\n{path}\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="mount_id"\r\n\r\n15027\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="filefield"\r\n\r\nfile\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="token"\r\n\r\n{token}\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="id"\r\n\r\nWU_FILE_1\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="name"\r\n\r\nadvs.txt\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="type"\r\n\r\ntext/plain\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="lastModifiedDate"\r\n\r\nSun Jan 24 2021 16:19:33 GMT+0800 (\u4E2D\u56FD\u6807\u51C6\u65F6\u95F4)\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="size"\r\n\r\n2\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="overwrite"\r\n\r\n1\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: text/plain\r\n\r\n{file_data}\r\n------WebKitFormBoundaryJ3pFR3AlykeqrrDN--\r\n'.format(
            path='班表1', token=self.token, filename='advs.txt', file_data=file_data)
        # data = data.replace('\\', '\\')
        # print(data)

        response = self.session.post('http://panstorage.gzmtr.cc:8092/web_upload', headers=headers, data=data.encode(),
                                     verify=False)
        print(response.text)
        print(response.status_code)

    @staticmethod
    def pan_download_duty_list():
        link_ = 'hur5uk7ct706pbkrinw3kgex3sf68c02'
        password_ = '1'
        link_to_password = Pan.pan_link_to_password(link_, password_)
        # print(link_to_password)
        file_name_ = "班表1/advs.txt"
        getlist_ = Pan.pan_getlist_for_pwd(link_, link_to_password, file_name_)
        download_ = Pan.pan_download_for_pwd(getlist_)
        get_data_of_dates = json.loads(download_)
        return get_data_of_dates


def main_handle():
    import sys
    sys.path.append("..\..")
    from gzmtr_edu.handle_core import gzmtr_edu_pc_handle
    # pan = Pan()
    # proxies = {"http": "http://127.0.0.1:6000"}
    # pan.session.proxies = proxies

    # sys.path.append("..\..\..")
    # from edu_phone.bb import bb
    # file_data = bb

    handle = gzmtr_edu_pc_handle.edu_handle(None, None)
    pp = {'1': 1}
    _date = datetime.date.today().strftime("%Y-%m-%d")
    # print(_date)
    pp = handle.get_class_for_input3(_date)
    # handle.get_class_for_input2(_date, pp, '夜班')
    # # print(pp)
    file_data = json.dumps(pp)

    # return
    # pan.pan_login()
    # pan.pan_gettoken()
    # pan.pan_upload(file_data)

    link_ = 'hur5uk7ct706pbkrinw3kgex3sf68c02'
    password_ = '1'
    link_to_password = Pan.pan_link_to_password(link_, password_)

    path = '班表1'
    filename = 'advs.txt'
    Pan.pan_upload_for_pwd(link_, password_, path, filename, file_data)
    print(file_data)
    print(type(file_data))


if __name__ == '__main__':
    main_handle()
