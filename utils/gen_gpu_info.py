import datetime
import os, time


def gen_gpu_list():
    gpu_ter = 'gpustat -cp'
    gpu_res = os.popen(gpu_ter).read().strip()
    my_list = gpu_res.split('\n')
    tmp_list = []
    for i in my_list:
        p_list = i.split('|')
        tmp_list.append(p_list)

    gpu_list = []
    pid_list = []
    mem_in_use = 0
    mem_all = 8 * 15079
    mem_dict = {}

    with open('/home/dc2-user/Multi_dockers_GPU_Visualized_Management/utils/rate.txt', 'r') as f:
        dict_str = f.read()
        res_dict = eval(dict_str)

    for i in range(1, len(tmp_list)):
        p = tmp_list[i]
        mem_info = p[2].split('/')
        mem_size = int(mem_info[1].strip()[:-3])
        mem_used = int(mem_info[0].strip())
        mem_in_use += mem_used
        mem_use_rate = int(round(mem_used / mem_size, 2) * 100)

        mem_dict['rate_' + str(i)] = mem_use_rate

    all_mem_used_rate = int(round(mem_in_use / mem_all, 2) * 100)

    mem_dict['all_mem_used_rate'] = all_mem_used_rate

    now_time = str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))

    res_dict[now_time] = mem_dict

    # print(res_dict)

    with open('/home/dc2-user/Multi_dockers_GPU_Visualized_Management/utils/rate.txt', 'w') as f:
        f.write(str(res_dict))

    return res_dict

