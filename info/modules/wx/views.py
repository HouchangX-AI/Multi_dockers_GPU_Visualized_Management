import os

from flask import render_template, jsonify

from info.modules.wx import wx_blu


@wx_blu.route('/source_data')
def source_data():
    # 获取服务器上面的数据
    terminal = 'docker stats --no-stream --format "{\\"container\\":\\"{{ .Container }}\\",\\"name\\":\\"{{ .Name }}\\",\\"memory\\":{\\"raw\\":\\"{{ .MemUsage }}\\",\\"percent\\":\\"{{ .MemPerc }}\\"},\\"cpu\\":\\"{{ .CPUPerc }}\\",\\"pid\\":\\"{{ .PIDs }}\\",\\"diskio\\":\\"{{ .BlockIO }}\\"}"'
    # print(terminal)
    result = os.popen(terminal).read().strip()
    # print(result)
    my_list = result.split('\n')
    # print(my_list)
    source_list = []
    for i in my_list:
        i = eval(i)
        p_source = {
            'container': i.get('container'),
            'name': i.get('name'),
            'memory_use': i.get('memory')['raw'],
            'memory_per': i.get('memory')['percent'],
            'cpu': i.get('cpu'),
            'pid': i.get('pid'),
            'diskio': i.get('diskio'),
        }
        source_list.append(p_source)
    data = {
        'code': 0,
        'count': len(source_list),
        "data": source_list,
    }
    return jsonify(data)


@wx_blu.route('/source_ctrl')
def source_ctrl():
    return render_template('source_ctrl.html')
