import time
import socket
import struct
import string
import random
import threading

class QSBot:
    def __init__(self, IP, Port):
        self.NullByte = struct.pack('B', 0)
        self.BufSize = 4096
        self.ServerIP = IP
        self.ServerPort = Port

        self.connectToServer(self.ServerIP, self.ServerPort)

    def sendPacket(self, Socket, PacketData, Receive = False):
        Packet = bytes(PacketData, 'utf-8')

        if Socket:
            Socket.send(Packet + self.NullByte)

            if Receive:
                return Socket.recv(self.BufSize).decode('utf-8')

    def startKeepAlive(self, TimerSeconds = 10):
        if hasattr(self, 'SocketConn'):
            KeepAliveTimer = threading.Timer(TimerSeconds, self.startKeepAlive)
            KeepAliveTimer.daemon = True
            KeepAliveTimer.start()
            self.sendPacket(self.SocketConn, '0')
            #self.sendPacket(self.SocketConn, '9%%%%%%%%%%%%<><<>><//')
            #self.sendPacket(self.SocketConn, '0b100255000000')
            #self.sendPacket(self.SocketConn, '01')
            #self.sendPacket(self.SocketConn, '0b141255000000000000255')
            #self.sendPacket(self.SocketConn, '06Dick;rc')
            #self.sendPacket(self.SocketConn, '9ୱ୲୳୴୵୶୷୸୹୺୻୼୽୾୿ೳ೴೵೶೷೸೹೺೻೼೽೾೿')
            #self.sendPacket(self.SocketConn, 'A')
            #self.sendPacket(self.SocketConn, '0c')
            #self.sendPacket(self.SocketConn, 'INTERNAL SERVER ERROR')
            #self.sendPacket(self.SocketConn, '0b100255000000255000000')
            #self.sendPacket(self.SocketConn, '0b101001001001001001001')
            #self.sendPacket(self.SocketConn, '0b102-95-95-95-95-95-95')
            #self.sendPacket(self.SocketConn, '0b103255255255255255255')
            #self.sendPacket(self.SocketConn, '0b104001-95-95001-95-95')
            #self.sendPacket(self.SocketConn, '06')
            #self.sendPacket(self.SocketConn, '07')
            #self.sendPacket(self.SocketConn, '08')
            #self.sendPacket(self.SocketConn, '09')
            #self.sendPacket(self.SocketConn, '02')
            #self.sendPacket(self.SocketConn, '04penis')
            #self.sendPacket(self.SocketConn, '฀กขฃคฅฆงจฉชซฌญฎฏ0E10ฐฑฒณดตถทธนบปผฝพฟ')
            #self.sendPacket(self.SocketConn, 'System.out.println((char)27 + "[31mThis is an Error" + (char)27 + "[0m");')
            #self.sendPacket(self.SocketConn, 'System.exit();')
            #self.sendPacket(self.SocketConn, 'System.exit(0);')
            #self.sendPacket(self.SocketConn, 'exit()')
            #self.sendPacket(self.SocketConn, 'quit()')
            #self.sendPacket(self.SocketConn, 'sys.exit()')
            #self.sendPacket(self.SocketConn, 'os._exit()')
            #self.sendPacket(self.SocketConn, 'print("กขฃคฅฆงจฉชซฌญฎฏ0E10ฐฑฒณดตถทธนบปผฝพฟ")')
            #self.sendPacket(self.SocketConn, 'print "กขฃคฅฆงจฉชซฌญฎฏ0E10ฐฑฒณดตถทธนบปผฝพฟ"')

    def connectionHandler(self):
        Buffer = b''

        while hasattr(self, 'SocketConn'):
            try:
                Buffer += self.SocketConn.recv(self.BufSize)
            except OSError:
                if hasattr(self, 'SocketConn'):
                    try:
                        self.SocketConn.shutdown(socket.SHUT_RD)
                        self.SocketConn.close()
                    except:
                        pass

            if len(Buffer) == 0:
                print('Disconnected')
                break
            elif Buffer.endswith(self.NullByte):
                Receive = Buffer.split(self.NullByte)
                Buffer = b''

                for Data in Receive:
                    Data = Data.decode('utf-8')

                    if Data.startswith('0g') or Data.startswith('0j'):
                        print('{{Server}}: {}'.format(Data[2:]))
                    elif Data.startswith('0f') or Data.startswith('0e'):
                        Time, Reason = Data[2:].split(';')
                        print('This account has just been banned [Time: {} / Reason: {}]'.format(Time, Reason))

    def connectToServer(self, ServerIP, ServerPort):
        try:
            self.SocketConn = socket.create_connection((ServerIP, ServerPort))
        except Exception as Error:
            print(Error)
            return

        Handshake = self.sendPacket(self.SocketConn, '08HxO9TdCC62Nwln1P', True).strip(self.NullByte.decode('utf-8'))

        if Handshake == '08':
            #02B100!lol
            numberS = str(random.randint(1000, 99999))
            Packets = ['02A00!BIMBO{};F*GCEDBE'.format(numberS), '0k1']

            for Packet in Packets:
                self.sendPacket(self.SocketConn, Packet)

            self.startKeepAlive()
            ConnectionThread = threading.Thread(target=self.connectionHandler)
            ConnectionThread.start()

            print('Connected.')
        else:
            print('Server capacity check failed.')

if __name__ == '__main__':
    #QSBot('ballistick5.xgenstudios.com', 1138)
    #QSBot('ballistick4.xgenstudios.com', 1138)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    QSBot('ballistick1.xgenstudios.com', 1031)
    #QSBot('ballistick3.xgenstudios.com', 1138)
    #QSBot('ballistick2.xgenstudios.com', 1138)
    #QSBot('ballistick9.xgenstudios.com', 1138)
    #QSBot('ballistick1.xgenstudios.com', 1139)
