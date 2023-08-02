import sys, notify

def main():
    
    if (len(sys.argv)<2):
        print("Notify error: wrong arguments.")
        exit(0)
        
    l = len(sys.argv)
    
    message = ""
        
    for i in range(1, l):
        message += sys.argv[i]+" "
        
    notify.send(message=message)