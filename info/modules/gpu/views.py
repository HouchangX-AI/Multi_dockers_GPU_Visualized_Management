from flask import render_template

from info.modules.gpu import gpu_blu


@gpu_blu.route('/rate')
def rate():

    with open('/home/dc2-user/Multi_dockers_GPU_Visualized_Management/utils/rate.txt', 'r') as f:
        rate_dict = eval(f.read())

    x_list = []
    y_list_1, y_list_2, y_list_3, y_list_4, y_list_5, y_list_6, y_list_7, y_list_8, y_list_all = [], [], [], [], [], [], [], [], []
    for k, v in rate_dict.items():
        x_list.append(k)
        y_list_1.append(v.get('rate_1'))
        y_list_2.append(v.get('rate_2'))
        y_list_3.append(v.get('rate_3'))
        y_list_4.append(v.get('rate_4'))
        y_list_5.append(v.get('rate_5'))
        y_list_6.append(v.get('rate_6'))
        y_list_7.append(v.get('rate_7'))
        y_list_8.append(v.get('rate_8'))
        y_list_all.append(v.get('all_mem_used_rate'))
    data = {
        'x_list': x_list,
        'y_list_1': y_list_1,
        'y_list_2': y_list_2,
        'y_list_3': y_list_3,
        'y_list_4': y_list_4,
        'y_list_5': y_list_5,
        'y_list_6': y_list_6,
        'y_list_7': y_list_7,
        'y_list_8': y_list_8,
        'y_list_all': y_list_all,
    }

    return render_template('gpu_rate.html', data=data)
