class SockStart:
    adr = ""
    port = 80
    sock = ""
    buffer = 4096
    acceptedFile = "application/json"

    def __init__(self, adr = "coronavirus-tracker-api.herokuapp.com" ,  ):
        import socket


        self.adr = adr
        self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        self.sock.connect((self.adr , self.port ))


    def setBuffer(self ,intt):
        if( intt is int):
            self.buffer = intt

    def getVari(self ,  string ):
        vari = ""
        tmp = "" 

        if( isinstance(string , str) ):
            self.sock.sendall(("GET " + string + " HTTP/1.1\r\nHost: " + self.adr + "\r\nAccept: " + self.acceptedFile + "\r\n\r\n").encode())
            while(True):
                tmp = self.sock.recv(self.buffer)
                vari += tmp.decode()
                if(tmp == b""):
                    break
                tmp = ""

            return vari

    def closeSocket(self):
        self.sock.close()
