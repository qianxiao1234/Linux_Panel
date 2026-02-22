from flask import Flask, jsonify, render_template
import psutil
import time

app = Flask(__name__)

def get_stats():
    # CPU 使用率（阻塞 0.1 秒获得较准确值）
    cpu_percent = psutil.cpu_percent(interval=0.1)
    load_avg = psutil.getloadavg()

    # 内存信息
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    # 磁盘分区（过滤掉常见的虚拟文件系统）
    partitions = []
    for part in psutil.disk_partitions(all=False):
        # 跳过虚拟文件系统类型
        if part.fstype in ('proc', 'sysfs', 'devtmpfs', 'tmpfs', 'fusectl',
                           'cgroup', 'cgroup2', 'nsfs', 'overlay', 'autofs'):
            continue
        try:
            usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue
        partitions.append({
            'device': part.device,
            'mountpoint': part.mountpoint,
            'fstype': part.fstype,
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent
        })

    # 网络累计流量（所有接口总和）
    net = psutil.net_io_counters()

    # 启动时间与运行时长
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time

    return {
        'cpu_percent': cpu_percent,
        'load_avg': list(load_avg),
        'memory': {
            'total': mem.total,
            'available': mem.available,
            'percent': mem.percent,
            'used': mem.used,
            'free': mem.free
        },
        'swap': {
            'total': swap.total,
            'used': swap.used,
            'free': swap.free,
            'percent': swap.percent
        },
        'disk_partitions': partitions,
        'network': {
            'bytes_sent': net.bytes_sent,
            'bytes_recv': net.bytes_recv
        },
        'boot_time': boot_time,
        'uptime_seconds': uptime_seconds
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    return jsonify(get_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)