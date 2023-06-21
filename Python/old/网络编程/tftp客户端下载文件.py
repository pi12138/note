"""
tftp下载文件
地址:("127.0.0.1", 69)
"""
import struct
import socket 
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


def recv_data():
    """接收数据"""
    data_length = 0
    code = 0
    block_number = 0
    current_number = 0

    while True:
        data, addr = s.recvfrom(1024)

        # code_tuple = struct.unpack("!HH", data[:4])
        # print(code_tuple) # (3, 1)
        code, current_number = struct.unpack("!HH", data[:4])
        data_length = len(data)

        if code == 3: 
            
            if current_number == 1:
                f = open(filename, 'ab')
            
            if block_number+1 == current_number:
                f.write(data[4:])
                block_number += 1
                print("第{}次接收到数据!".format(current_number))

                reply_info = struct.pack('!HH', 4, block_number)
                s.sendto(reply_info, addr)
            
            if data_length < 516:
                f.close()
                print("下载完成！")
                break

        else:
            print("error info {}：", data.decode())
            break  


def main():
    global s

    handle_argv()

    read_args = struct.pack("!H{}sb5sb".format(len(filename)), 1, filename.encode(), 0, 'octet'.encode(), 0)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 6666))
    
    # IP可变, 端口固定
    # s.sendto(read_args, ("127.0.0.1", 69))
    s.sendto(read_args, (ip, 69))   

    recv_data()

    s.close()


if __name__ == "__main__":
    main()