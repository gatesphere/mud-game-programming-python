#!/usr/bin/python
import socket

if __name__ == "__main__":
  ## begin code block 2.4 - create a connecting data socket
  message = "Hello Internet!"
  
  ipaddr = raw_input("Enter the IP address to connect to: ")
  
  # create the socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # connect the socket
  sock.connect((ipaddr, 4000))
  ## end code block 2.4
  
  print "Sending message: %s..." % message
  
  # send data
  sock.send(message)
  
  sock.shutdown(socket.SHUT_RDWR)
  sock.close()