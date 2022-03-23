from telnetlib import Telnet as T

host = "na-robot.ddns.net"
port = 8017

def cell_stats():
    data = "cell_stats"
    conn = T(host, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

def attach(ue, cell):
    data = "attach  ue={} cell={}".format(ue, cell)
    conn = T(host, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

def detach(ue):
    data = "detach  ue={}".format(ue)
    conn = T(host, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

def start_traffic(ue, mbps, bearer):
    data = 'trf_data_start  ue={} mbps={} bearer={}'.format(ue, mbps, bearer)
    conn = T(host, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

def show_traffic(ue):
    data = 'show_traffic  ue={} '.format(ue)
    conn = T(host, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

def stop_traffic(ue, bearer):
    data = 'trf_data_stop   ue={} bearer={} '.format(ue, bearer)
    conn = T(host, port)
    conn.write(data.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()
    return response

def ask(command):
    conn = T(host, port)
    conn.write(command.encode())
    response = conn.read_all().decode()
    print(response)
    conn.close()

#ask("cell_stats")
#attach(1, 1)
cell_stats()
#start_traffic(1, 1, 5)
#stop_traffic(1, 5)
#detach(1)


