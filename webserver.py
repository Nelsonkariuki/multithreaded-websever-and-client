from socket import *
 #import the python socket module
import sys
# for commandline arguments handling
import datetime 
# for timestamp log
ServerSocket= socket(AF_INET, SOCK_STREAM) # IPV4 address, TCP stream
#print "The no of Args is:",len(sys.argv)
# #for debugging
ServerPort=8080 # default port if port not provided in terminal
if (len(sys.argv)==2):
    ServerPort=int(sys.argv[1])
Host = gethostname()# get the IPaddress computer 
#ServerSocket.bind((Host,ServerPort)) # debugging# for other machines in Network
ServerSocket.bind(('',ServerPort)) # Bind to this m/c IP address to this port
ServerSocket.listen(5) #listen to 5 connections at a time[Multithreaded]
print('Web server ready to serve on port'),ServerPort,"..."
filename=""
while True: # infinite loop accepting connections
    connectionSocket, addr =ServerSocket.accept() # Client conn setup
    print ('\n')
    print ('--------------------------------------------------------------------------')
    #timestamp with host name & IP address
    print('TimeStamp'),datetime.datetime.now(),"Request from", (gethostbyaddr(connectionSocket.getpeername()[0]))[0],(gethostbyaddr(connectionSocket.getpeername()[0]))[2]
    print('Client Host Name:'),(gethostbyaddr(connectionSocket.getpeername()[0]))[0] #find the host name obtaining the peer IP address
    print('Client Socket Family:'),connectionSocket.family
    print('Client Socket Type:'),connectionSocket.type
    print('Client Protocol:'), connectionSocket.proto
    print('Client Socket- get Peer Name:'), connectionSocket.getpeername()
    print('Client Timeout:'),connectionSocket.gettimeout()
    #print "The number of Args as:",len(sys.argv)
    try:
        clientmessage=connectionSocket.recv(1024) # receive the requests from client
        if (clientmessage!=''):
            print('Request details:'), clientmessage #request from the client
            filename = clientmessage.split()[1] # get the /filename from the string
            #print "The file recd is..." + filename # for debugging
            file = open(filename[1:]) # ignore "/" the 1st char in received filename
            outputdata =file.read()
            connectionSocket.send("\nHTTP/1.1 200 OK\n")
            for c in range(0,len(outputdata)): # 0 to eof
                connectionSocket.sendall(outputdata[c]) # send response to client
            print('Response:File Sent to client....')
            print('-----------------------------')
            connectionSocket.close() # close client socket
    except IOError: # file not found exception
        print('clientmessage'),clientmessage
        if filename!="/favicon.ico":
            print('IOError')
            print('Response:404 Not Found sent to client.......') # printed 404
            print("--------------------------------------------------------------------------")
        else:
            print("Additional ""Get favicon.ico"" request sent by Browser..")
            print("--------------------------------------------------------------------------")
        connectionSocket.send("\n404 Not Found\n")# 404, send to client
        connectionSocket.close() 
ServerSocket.close()# close the serverside socket outside the infinite loop, executes when program termintes
       
                            

    
          
       


