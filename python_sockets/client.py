messag = ['Hello, world', 'Test', 'anything goes here'] 

def client_to_server(messag,host,port,size): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host, port)) 
    countmsg = 0 
    restmsg = '' 
    for msg in messag: 
     strl = tmsg = msg 
     if len(restmsg): 
      tmsg = restmsg + ' ' + msg 
     countmsg = len(tmsg) 
     if countmsg <= size: 
      pass 
     else: 
      restmsg = tmsg[size:] 
      tmsg = tmsg[:size] 
      #s.close() 
      countmsg = len(tmsg) 
      #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
      #s.connect((host, port)) 
     print 'Sending to server msg {}'.format(tmsg) 
     s.send(tmsg) 
     # s.settimeout(1) 
     try: 
      data = s.recv(size) 
      print 'Received:', data 
      if strl == data: 
       print strl,data 
       countmsg = 0 
       restmsg = '' 
     except (socket.error), e: 
      print e.args,e.message 
      s.close() 
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
      s.connect((host, port)) 
    s.close() 
    if restmsg: 
     client_to_server([restmsg],host,port,size) 
    return 


client_to_server(messag,host,port,size) 
