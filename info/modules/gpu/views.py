from flask import render_template

from info.modules.gpu import gpu_blu
from utils.gen_gpu_info import gen_gpu_list


@gpu_blu.route('/rate')
def rate():
    rate_dict = gen_gpu_list()
    # with open('/home/dc2-user/Multi_dockers_GPU_Visualized_Management/utils/rate.txt', 'r') as f:
    #     rate_dict = eval(f.read())
    # 对取到的字典根据键的时间进行排序
    rate_list = sorted(rate_dict.items(), key=lambda x: x[0], reverse=False)
    # print(rate_list)
    # rate_dict = {i[0]: i[1] for i in rate_list}
    # print(rate_dict)
    x_list = []
    y_list_1, y_list_2, y_list_3, y_list_4, y_list_5, y_list_6, y_list_7, y_list_8, y_list_all = [], [], [], [], [], [], [], [], []
    for i in rate_list:
        x_list.append(i[0])
        y_list_1.append(i[1].get('rate_1'))
        y_list_2.append(i[1].get('rate_2'))
        y_list_3.append(i[1].get('rate_3'))
        y_list_4.append(i[1].get('rate_4'))
        y_list_5.append(i[1].get('rate_5'))
        y_list_6.append(i[1].get('rate_6'))
        y_list_7.append(i[1].get('rate_7'))
        y_list_8.append(i[1].get('rate_8'))
        y_list_all.append(i[1].get('all_mem_used_rate'))
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
