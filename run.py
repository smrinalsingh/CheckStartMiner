from pypsexec.client import Client
import getpass

def WorkerStatus(psObject, exeName):
    stdout, stderr, rc = c.run_executable("cmd.exe",
                                                  arguments="/c tasklist")
    stdout = stdout.decode("utf-8")
    if (stdout.__contains__(exeName)):
        return True
    else:
        return False
    

with open("hosts.txt", "r") as file:
    hosts = file.readlines()
    hosts = [x.strip("\n") for x in hosts]

adminPass = getpass.getpass(prompt='Password: ',
                            stream=None)

for host in hosts:
    c = Client(host, username="Administrator", password=adminPass)
    print ("Object created. Trying to connect: %s"%host)
    try:
        c.connect()
        print ("Connected.")
        try:
            c.create_service()
            print ("Service created.")

            #code to start of stop the worker.
            #stdout, stderr, rc = c.run_executable("cmd.exe", arguments="/c ipconfig")
            stdout = WorkerStatus(c, "xmrig.exe")
            
            print ("Command Output\n******")
            print (stdout)
            print ("******")
            
        except Exception as e:
            print ("Couldn't create service or execute command. ", end="")
            print (e)
            
    except Exception as e:
        print ("Unable to connect. ", end="")
        print (e)
        
    finally:
        try:
            c.cleanup()
            c.disconnect()
        except:
            pass
        finally:
            print ("Cleaned up: " + host + "\n\n")
