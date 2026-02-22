# Linux 服务器监控面板 (Linux_Panel)

极简的 Linux 服务器资源监控 Web 面板，使用 Python Flask + psutil 采集系统数据，前端纯 HTML/JavaScript 展示，无需数据库，开箱即用。

## 功能特性

- 💻 **CPU 实时监控**：显示当前 CPU 使用率及 1/5/15 分钟负载平均值。
- 🧠 **内存监控**：显示内存总量、已用、可用、空闲及使用率。
- 💾 **交换分区监控**：显示交换分区使用情况（如启用）。
- 📁 **磁盘分区监控**：列出所有真实磁盘分区（自动过滤虚拟文件系统），显示容量、已用、使用率。
- 🌐 **网络流量监控**：显示累计上传/下载流量，并实时计算上传/下载速度。
- ⏱️ **系统运行时间**：显示系统启动时间及已运行时长。
- 🔄 **自动刷新**：数据每秒动态更新（可自行配置）。

## 技术栈

- **后端**：Python 3 + Flask + psutil
- **前端**：原生 HTML + CSS + JavaScript (ES6)
- **通信**：RESTful API (JSON)

## 安装与使用

### 1. 克隆仓库
```bash
git clone https://github.com/qianxiao1234/Linux_Panel.git
cd Linux_Panel
```

### 2. 安装依赖

请先安装 python3 和其依赖

- Debian / Ubuntu
```bash
apt install python3
pip install flask psutil
```
- Arch Linux
```bash
sudo pacman -S python3 python-flask python-psutil
```

### 3. 启动服务
```bash
python app.py
```
默认监听 0.0.0.0:5000，启动后可通过 http://服务器IP:5000 访问。

### 4. 停止服务

在终端按 Ctrl + C 即可终止。