import psutil
import pickle
import cpuinfo
import socket, os, time
import netifaces


class Services:
    def __init__(self):
        self.service = "service"


    def freq_info(self,  conn, addr, msg):
        freq = psutil.cpu_freq()
        info = {'current': freq[0], 'total': freq[2]}
        conn.send(bytes(pickle.dumps(info)))
        print(addr, ": ", msg)

    # captures sys info
    def stats_info(self, conn, addr, msg):

        cpu_info = cpuinfo.get_cpu_info()
        freq = psutil.cpu_freq().current
        cpu_count = psutil.cpu_count()
        cpu_lol = psutil.cpu_count(logical=False)
        maxi = psutil.cpu_freq().max
        mini = psutil.cpu_freq().min
        vir_mem_total = psutil.virtual_memory().total

        infos = {"cpu_info": cpu_info, "freq": freq, "cpu_count": cpu_count, "cpu_lol": cpu_lol, "maxi": maxi, "mini": mini, "vir_mem": vir_mem_total}

        conn.send(bytes(pickle.dumps(infos)))
        print(addr, ": ", msg)

    def space_info(self, conn, addr, msg):
        disk = psutil.disk_partitions()
        mounted = []

        disk_parts = []
        for i in disk:
            mounted.append(i[0])

        for i in mounted:
            disk_parts.append({i: psutil.disk_usage(i)})

        conn.send(bytes(pickle.dumps(disk_parts)))
        print(addr, ": ", msg)

    #  captures cpu percentage
    def cpu_service(self, conn, addr, msg):
        cpu = psutil.cpu_percent()
        cpu_cores = psutil.cpu_percent(interval=None, percpu=True)

        c = 0
        obj = [{c: cpu}]
        for i in cpu_cores:
            c += 1
            obj.append({c: i})

        conn.send(bytes(pickle.dumps(obj)))

        # conn.send(str(obj).encode(FORMAT))  # this is without pickle - use it to debug

        print(addr, ": ", msg)


    #  captures virtual memory
    def msn_service(self, conn, addr, msg):
        mem_total = str(psutil.virtual_memory()[0] / (1024 * 1024 * 1000))
        mem_ava = str(psutil.virtual_memory()[1] / (1024 * 1024 * 1000))
        mem_used = str(psutil.virtual_memory()[3] / (1024 * 1024 * 1000))
        mem_per = str(psutil.virtual_memory()[2])

        infos = {"total": mem_total, "available": mem_ava, "used": mem_used, "percent": mem_per}

        conn.send(bytes(pickle.dumps(infos)))
        print(addr, ": ", msg)


    #  captures gateway
    def gateway_service(self, conn, addr, msg):
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        conn.send(bytes(pickle.dumps(default_gateway)))
        print(addr, ": ", msg)

    # determine net connections
    def active_connections(self, conn, addr, msg):
        st = psutil.net_if_stats()

        active_connections = []
        for k, v in st.items():
            if v[0] == True:
                if v[2] < 500:
                    active_connections.append(psutil.net_if_addrs()[k][1].address)

        conn.send(bytes(pickle.dumps(active_connections)))
        print(addr, ": ", msg)

    #  captures addresses
    def internet_service(self, conn, addr, msg):
        infos = []
        net = psutil.net_if_addrs()

        for key, value in net.items():
            infos.append({str(key): value[1][1], "submask": value[1][2], "mac addr": value[0][1]})

        conn.send(bytes(pickle.dumps(infos)))
        print(addr, ": ", msg)


    # captures processes
    def process_service(self, conn, addr, msg):
        try:
            pid = psutil.pids()
            listaPro = []
            for i in pid:
                p = psutil.Process(i)
                listaPro.append({'pid': p.pid,
                                 'nam': p.name(),
                                 'st': p.status(),
                                 'mem': '{:.2f}'.format(p.memory_percent()),
                                 'th': p.num_threads()})

            conn.send(bytes(pickle.dumps(listaPro)))
            print(addr, ": ", msg)
        except:
            print("Some finished process created an error. Reload it.")



    # captures directories
    def directory_service(self, conn, addr, msg):
        REBOOT = "c:\\Users"
        # os.chdir(REBOOT)

        arq = []
        lista = os.listdir(REBOOT)

        for i in lista:
            if os.path.isfile(i):
                arq.append({'name': os.path.splitext(i)[0],
                            'size': str(os.stat(i).st_size),
                            'ced_at': str(os.stat(i).st_atime),
                            'med_at': str(os.stat(i).st_mtime),
                            'type': os.path.splitext(i)[1]})
            else:
                arq.append({'name': i,
                            'size': str(os.stat(i).st_size),
                            'ced_at': str(os.stat(i).st_atime),
                            'med_at': str(os.stat(i).st_mtime),
                            'type': 'File'})

        conn.send(pickle.dumps(arq))
        print(addr, ": ", msg)
