import socket
import concurrent.futures

# Rango de puertos que quieres escanear
start_port = 1
end_port = 65535

# Función para escanear un puerto específico
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None

# Escaneando los puertos
print("Escaneando los puertos en el rango de {} a {}...".format(start_port, end_port))

with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
    future_to_port = {executor.submit(scan_port, port): port for port in range(start_port, end_port + 1)}
    for future in concurrent.futures.as_completed(future_to_port):
        port = future_to_port[future]
        if port is not None:
            try:
                open_port = future.result()
                if open_port is not None:
                    print("Puerto {} está abierto".format(open_port))
            except Exception as exc:
                print('%r generó una excepción: %s' % (port, exc))
