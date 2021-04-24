import re

import requests
from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json

import pan

app = Flask(__name__, static_url_path='')

db_name = 'mydb'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'],
                      connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@app.route('/')
def root():
    return app.send_static_file('index1.html')
    # return render_template('index1.html')


@app.route('/api/month_list/')
def month_list():
    print(request)
    download_ = get_duty_data()
    re_compile = re.compile(r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d")
    loads = json.loads(download_)
    last_change = "0"
    file_info = pan.Pan().pan_getlist("advs.txt")
    # print(1, last_update)
    res_month = set()
    for i in loads:
        # i_schedule_name_ = {"date": i["UserName"], "name": i["ScheduleDay"], "ScheduleName": i["ScheduleName"]}
        # res.append(i_schedule_name_)
        # print(i)
        schedule_day_: str = i["ScheduleDay"]
        res_month.add(schedule_day_[:6])

        time_ = i["AddTime"]
        if re_compile.match(time_):
            if last_change < time_:
                format_time = time_[:16]
                format_time = format_time.replace("T", " ").replace("-", "/")
                last_change = format_time
                # print(format_time)

    res = sorted(list(res_month))
    # return HttpResponse(json.dumps({'month_list': res, 'last_change': last_change, 'file_info': file_info}),
    #                     content_type="application/json,charset=utf-8")
    json_dumps = json.dumps({'month_list': res, 'last_change': last_change, 'file_info': file_info})
    print(json_dumps)
    return json_dumps


def get_duty_data(month=""):
    Pan = pan.Pan()
    link_ = 'hur5uk7ct706pbkrinw3kgex3sf68c02'
    password_ = '1'
    link_to_password = Pan.pan_link_to_password(link_, password_)
    # path = '班表1'
    # filename = 'advs.txt'
    # Pan.pan_upload_for_pwd(link_, password_, path, filename, file_data)
    if len(month) > 0:
        file_name_ = "班表1/duty_{month}".format(month=month)
    else:
        file_name_ = "班表1/advs.txt"

    getlist_ = Pan.pan_getlist_for_pwd(link_, link_to_password, file_name_)
    download_ = Pan.pan_download_for_pwd(getlist_)
    return download_


def get_holidays_data(yeah):
    # requests_get = requests.get(
    #     "https://natescarlet.coding.net/p/github/d/holiday-cn/git/raw/master/{}.json".format(yeah))
    requests_get = requests.get(
        "https://natescarlet.coding.net/p/github/d/holiday-cn/git/raw/master/{}.json".format(yeah))

    return requests_get.text


@app.route('/api/holidays_list/')
def holidays_list():
    get_yeah = request.args.get("yeah")
    download_ = get_holidays_data(get_yeah)
    # loads = json.loads(download_, encoding='GB2312')
    # return HttpResponse(download_)
    # print(json.dumps(download,_ensure_ascii=False, encoding='utf-8'))
    # download_ = json.dumps(loads, encoding='utf-8')
    # print(download_)
    return download_
    # return render(request, "index.html")


@app.route('/api/duty_table/')
def duty_table():
    get_month = request.args.get("month")

    download_ = get_duty_data(month=get_month)
    # print(download_)
    return download_
    loads = json.loads(download_)
    res = {}
    res_date = set()
    for i in loads:
        # i_schedule_name_ = {"date": i["UserName"], "name": i["ScheduleDay"], "ScheduleName": i["ScheduleName"]}
        # res.append(i_schedule_name_)
        # print(i)
        schedule_day_ = i["ScheduleDay"]
        if get_month and schedule_day_[:6] == get_month:
            res_date.add(schedule_day_)

            # UserCode 可能会丢失或错误
            # res_get = res.setdefault(i['UserCode'], {'UserName': i["UserName"]})
            # UserID 可能会丢失或错误
            # res_get = res.setdefault(i['UserID'], {'UserName': i["UserName"]})

            res_get = res.setdefault(i['UserName'], {'UserName': i["UserName"]})
            res_get[schedule_day_] = i["ScheduleName"]
            # if i["UserName"] == "黄文焰":
            #     print(i)

    # res_name = sorted(list(res_name))
    # print(res_name)
    # res_date = [{'key': 'UserName', 'label': get_month}] + sorted(list(res_date))

    # print(res.values())
    res = list(res.values())
    return json.dumps(res)
    # return render(request, "duty_table1.html", {'List': json.dumps(res)})


# /* Endpoint to greet and add a new visitor to database.
# * Send a POST request to localhost:8000/api/visitors with body
# * {
# *     "name": "Bob"
# * }
# */
@app.route('/api/visitors', methods=['GET'])
def get_visitor():
    if client:
        return jsonify(list(map(lambda doc: doc['name'], db)))
    else:
        print('No database')
        return jsonify([])


# /**
#  * Endpoint to get a JSON array of all the visitors in the database
#  * REST API example:
#  * <code>
#  * GET http://localhost:8000/api/visitors
#  * </code>
#  *
#  * Response:
#  * [ "Bob", "Jane" ]
#  * @return An array of all the visitor names
#  */
@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    user = request.json['name']
    data = {'name': user}
    if client:
        my_document = db.create_document(data)
        data['_id'] = my_document['_id']
        return jsonify(data)
    else:
        print('No database')
        return jsonify(data)


@atexit.register
def shutdown():
    if client:
        client.disconnect()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
