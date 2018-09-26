import subprocess
print "Loading FIB Entries"
for i in range(0,1000):
    bashCommand = "nfdc route add /ndn/dummyPrefix_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])
    #print bashCommand


