import socket

target = "Target ip"  # Skan etmək istədiyiniz hədəf IP ünvanını buraya yazın
min_port = 1  # Skanın başlayacağı minimum port nömrəsi
max_port = 65535  # Skanın bitəcəyi maksimum port nömrəsi

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Porta qoşulma cəhdi üçün maksimum gözləmə müddəti (saniyə).
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {} açık".format(port))
        sock.close()
    except socket.error as e:
        print("Hata oluştu:", str(e))

# Müəyyən edilmiş port diapazonunu skan edin
for port in range(min_port, max_port+1):
    scan_port(port)
