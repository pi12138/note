"""
tftp上传文件
地址：('127.0.01', 69)
"""

import socket 
import struct
import sys


ip = ""
filename = ""
s = None


def handle_argv():
    """处理输入参数"""
    global ip
    global filename

    if len(sys.argv) != 3:
        print("-"*30)
        print("请输入正确格式：python xxx.py ip filename")
        print("例如：python xxx.py 127.0.0.1, test.txt")
        print("-"*30)
    else:
        ip = sys.argv[1]
        filename = sys.argv[2]


def upload_file():
    """上传文件"""
    code = 0
    block_number = 0
    current_number = 1

    while True:
        data, addr = s.recvfrom(1024)

        code, block_number = struct.unpack("!HH", data[:4])

        if code == 4:
            if block_number == 0:
                f = open(filename, 'rb')

            if block_number+1 == current_number:
                file_data = f.read(512)
                send_data = struct.pack('!HH', 3, current_number) + file_data
                s.sendto(send_data, addr)
                print("第{}次传输数据！".format(current_number))
                
                block_number += 1
                current_number += 1

            if len(send_data) < 516:
                f.close()
                print("文件上传完成！")
                break

        elif code == 5:
            f.close()
            print("上传文件失败！error info: {}".format(data[4:].decode()))
            break


def main():
    global s

    handle_argv()

    upload_args = struct.pack("!H{}sb5sb".format(len(filename)), 2, filename.encode(), 0, "octet".encode(), 0)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 6666))

    s.sendto(upload_args, ("127.0.0.1", 69))

    upload_file()

    s.close()

if __name__ == "__main__":
    main()