# 此模块用来用xbee通信

from digi.xbee.devices import XBeeDevice
# pygame用于获取键盘按键信息，控制发射指令
import time
from bitarray import bitarray, bits2bytes
import struct
from digi.xbee.reader import DataReceived
import numpy as np
# 发送信息途中会出现错误，可能子板不存在（小车没开电）
from digi.xbee.exception import TransmitException
import sys
# xbee主板的com口
PORT = "COM7"
# 波特率，主板子板要一致，如果控制多辆小车，建议115200， 9600太小
BAUD_RATE = 115200
# xbee的ni，子板要配置，主板不用配置。使用的是1           86固件，升级过的。
REMOTE_NODE_ID = ["8"]
# REMOTE_NODE_ID = "2"

def main():
    print(" +--------------------------------------+")
    print(" | XBee Python Library Send Data Sample |")
    print(" +--------------------------------------+\n")


    # 创建一个主板对象
    device = XBeeDevice(PORT, BAUD_RATE)
    # 用于存储已经连接上的子板
    end_device = []
    try:
        device.open()   
        xbee_network = device.get_network()
        # remote_device1 = xbee_network.discover_device("2")
        for i in range(1):
            try:
                # 用于链接子板
                tmp = xbee_network.discover_device(REMOTE_NODE_ID[i])
            except ValueError:
                tmp = 0
            end_device.append(tmp)
            print(end_device)

        DATA_TO_SEND_1 = '155'

        #print(sys.getsizeof(211))
        for i in range(1):
            try:
                if end_device[i]:
                        # 如果连接上就发送信息
                    device.send_data(end_device[i], DATA_TO_SEND_1)
                    # else:
                    #     # 如果没连接上尝试重连结
                    #     end_device[i] = xbee_network.discover_device(REMOTE_NODE_ID[i])
            except TransmitException:
                    # end_device[i] = xbee_network.discover_device(REMOTE_NODE_ID[i])
                print(REMOTE_NODE_ID[i])
            # device.send_data(remote_device1, DATA_TO_SEND)
            # device.send_data(remote_device2, DATA_TO_SEND)
            time.sleep(0.01)
            print("Success")
            # device.add_data_received_callback(data_receive_callback)

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()

    
        # remote_device1 = xbee_network.discover_device(REMOTE_NODE_ID)
        # remote_device2 = xbee_network.discover_device(REMOTE_NODE_ID2)
        # if remote_device1 is None or remote_device2 is None:
        #     print("Could not find the remote device")
        #     exit(1)

        # derta = 10
        # angle = 90 + derta

        # if abs(angle-90) >= 0 and abs(angle-90) <= 22:
        #     output_2 = angle - 58
        # elif abs(angle-90) >= 23 and abs(angle-90) <= 36:
        #     output_2 = angle/2-2
        # elif abs(angle-90) >= 37 and abs(angle-90) <= 45:
        #     output_2 = angle/3+19
        # angle_2 = bin(angle)
    
        # if stright:
        #     tmp = 0b01000000
        # if stop:
        #     tmp = 0b00000000
        # if back:
        #     tmp = 0b10000000
        # fin = tmp|angle_2
        # print (fin)
        # def get_bit_val(byte, index):
        #     """
        #     得到某个字节中某一位（Bit）的值

        #     :param byte: 待取值的字节值
        #     :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
        #     :returns: 返回读取该位的值，0或1
        #     """
        #     if byte & (1 << index):
        #         return 1
        #     else:
        #         return 0


        # def set_bit_val(byte, index, val):
        #     """
        #     更改某个字节中某一位（Bit）的值

        #     :param byte: 准备更改的字节原值
        #     :param index: 待更改位的序号，从右向左0开始，0-7为一个完整字节的8个位
        #     :param val: 目标位预更改的值，0或1
        #     :returns: 返回更改后字节的值
        #     """
        #     if val:
        #         return byte | (1 << index)
        #     else:
        #         return byte & ~(1 << index)


        # DATA_TO_SEND = bitarray(8)
        # DATA_TO_SEND[0] = get_bit_val(1,1)
        # DATA_TO_SEND[1] = get_bit_val(1,0)
        # DATA_TO_SEND[2] = get_bit_val(44,5)
        # DATA_TO_SEND[3] = get_bit_val(44,4)
        # DATA_TO_SEND[4] = get_bit_val(44,3)
        # DATA_TO_SEND[5] = get_bit_val(44,2)
        # DATA_TO_SEND[6] = get_bit_val(44,1)
        # DATA_TO_SEND[7] = get_bit_val(44,0) 
        # datab=DATA_TO_SEND.tobytes()

        # i = 0 
        # for bit in DATA_TO_SEND: 
        #     i = (i << 1) | bit 
        # print(DATA_TO_SEND)
        # print(datab)
        # print(i)