import os

from flask import render_template, jsonify, current_app

from info.modules.index import index_blu


@index_blu.route('/disk_data')
def disk_data():
    # 获取服务器上面的磁盘数据 df -h
    terminal = 'df -h'
    # print(terminal)
    result = os.popen(terminal).read().strip()
    # print(result)
    tmp_list = []
    my_list = result.split('\n')
    for i in my_list:
        p_list = [i for i in i.split(' ') if i != '']
        tmp_list.append(p_list)
    disk_list = []
    for i in range(1, len(tmp_list)):
        p = tmp_list[i]
        p_dict = {
            'filesystem': p[0],
            'size': p[1],
            'used': p[2],
            'avail': p[3],
            'use_rate': int(p[4][:-1]),
            'mounted_on': p[5],
        }
        disk_list.append(p_dict)
    # print(disk_list)
    data = {
        'code': 0,
        'count': len(disk_list),
        "data": disk_list,
    }
    return jsonify(data)


@index_blu.route('/gpu_data')
def gpu_data():
    gpu_ter = 'gpustat -cp'
    gpu_res = os.popen(gpu_ter).read().strip()
    # print(gpu_res)
    my_list = gpu_res.split('\n')
    # print(my_list)
    tmp_list = []
    for i in my_list:
        p_list = i.split('|')
        tmp_list.append(p_list)

    gpu_list = []

    for i in range(1, len(tmp_list)):
        p = tmp_list[i]
        mem_info = p[2].split('/')
        mem_size = int(mem_info[1].strip()[:-3])
        mem_used = int(mem_info[0].strip())
        mem_use_rate = int(round(mem_used / mem_size, 2) * 100)
        p_dict = {
            'gpu_id': i,
            'mem_size': mem_size,
            'mem_used': mem_used,
            'mem_use_rate': mem_use_rate,
            'use_info': p[3],
        }
        gpu_list.append(p_dict)
    data = {
        'code': 0,
        'count': len(gpu_list),
        "data": gpu_list,
    }
    return jsonify(data)


@index_blu.route('/')
def index():
    return render_template('index.html')


# 每个网站都会去设置/favicon.ico小logo图标
# 可以使用current_app.send_static_file(),自动加载static静态文件下面的内容
@index_blu.route('/favicon.ico')
def web_logo():
    return current_app.send_static_file("favicon.ico")
