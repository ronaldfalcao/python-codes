import pyqrcode

url = "http://www.ronaldfalcao.com.br"
qrcode = pyqrcode.create(url)

qrcode.svg('qrcode.svg', scale=12)  # Cria arquivo .svg
print(qrcode.terminal(quiet_zone=1))  # Exibe no terminal
