import psutil
import re  ## 标题
import os, sys


def processinfo(x):
    '''根据服务名找到PID'''
    procs = list(psutil.process_iter())  # 获取所有服务列表
    print(procs)
    for r in procs:
        aa = str(r)
        f = re.compile(x, re.I)
        if f.search(aa):
            print(aa.split('pid=')[1].split(',')[0])
            return aa.split('pid=')[1].split(',')[0]
            # print (aa.split('pid='))


def port(x):
    '''通过pid获取端口号'''
    PID = processinfo(x)
    cmd = 'netstat -ano | findstr' + ' ' + str(PID)
    print(cmd)
    a = os.popen(cmd)
    # 此时打开的a是一个对象，如果直接打印的话是对象内存地址
    text = a.read()
    # 要用read（）方法读取后才是文本对象
    first_line = text.split(':')
    ab = first_line[1]
    cd = ab.split(' ')
    por = cd[0]
    print(por)
    return por


if __name__ == '__main__':
    pid = sys.argv[1]
    port(pid)
