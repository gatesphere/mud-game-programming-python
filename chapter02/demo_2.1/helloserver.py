#!/usr/bin/python
import socket

if __name__ == "__main__":
  ## code block 2.3 - create a listening socket on port 4000
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # bind the socket
  serversocket.bind(('0.0.0.0', 4000))
  serversocket.listen(16)
  ## end code block 2.3
  
  # wait for an incoming connection now
  (clientsocket, address) = serversocket.accept()
  
  # recieve data
  buff = clientsocket.recv(128, 0)
  
  print "Data received:"
  print buff
  
  clientsocket.shutdown(socket.SHUT_RDWR)
  clientsocket.close()
  
  serversocket.shutdown(socket.SHUT_RDWR)
  serversocket.close()


