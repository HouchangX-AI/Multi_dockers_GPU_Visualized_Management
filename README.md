# Multi_dockers_GPU_Visualized_Management
Make some work for managing GPU server in order to save time.
### linux常用查看磁盘空间大小的命令
- ls -lh查看当前目录下文件大小

- df -lh 使用这个命令会更清楚磁盘使用情况

- df-a 查看全部文件大小

- du -h --max-depth=1 查看各文件夹大小

> 首页显示服务器的磁盘使用情况，方便观测相关的数据

### docker stats监控容器资源消耗

- docker stats 命令用来显示容器使用的系统资源。
- 默认情况下，stats 命令会每隔 1 秒钟刷新一次输出的内容直到你按下 ctrl + c。下面是输出的主要内容：

> - [CONTAINER]：以短格式显示容器的 ID。
> - [CPU %]：CPU 的使用情况。
> - [MEM USAGE / LIMIT]：当前使用的内存和最大可以使用的内存。
> - [MEM %]：以百分比的形式显示内存使用情况。
> - [NET I/O]：网络 I/O 数据。
> - [BLOCK I/O]：磁盘 I/O 数据。 
> - [PIDS]：PID 号。


只返回当前的状态:如果不想持续的监控容器使用资源的情况，可以通过 --no-stream 选项只输出当前的状态：
> docker stats --no-stream

