import os
import re

from flask import jsonify, render_template

from info.modules.disk import disk_blu


@disk_blu.route('/detail')
def detail():
    # 获取服务器上面的磁盘数据 df -h
    terminal = 'docker system df -v'
    # print(terminal)
    result = os.popen(terminal).read().strip()
    # print(result)
    a = r'Containers space usage:([\w\W]*)Local Volumes space usage:'
    info = re.findall(a, result)
    info_list = info[0].split('\n')
    info_list = [i for i in info_list if i != '']
    # print(info_list)

    detail_list = []

    for i in range(1, len(info_list)):
        p = [i for i in info_list[i].split(' ') if i != '']
        # print(p)
        if p[1] == 'houchang:base':
            p_dict = {
                'container_id': p[0],
                'image': p[1],
                'command': p[2] + p[3],
                'local_volums': p[4],
                'sort_size': size2num(p[5]),
                'size': p[5],
                'created': p[6] + p[7] + p[8],
                'status': p[9] + p[10] + p[11],
                'names': p[12],
            }
            detail_list.append(p_dict)

    data = {
        'code': 0,
        'count': len(detail_list),
        "data": detail_list,
    }
    return jsonify(data)


@disk_blu.route('/detail_info')
def detail_info():
    return render_template('disk_detail.html')


def size2num(size):
    if 'kB' in size:
        return float(size[:-2])
    elif 'MB' in size:
        return float(size[:-2])*1024
    elif 'GB' in size:
        return float(size[:-2])*1024*1024
    else:
        return 0
