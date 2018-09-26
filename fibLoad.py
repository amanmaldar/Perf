import subprocess
import time

bashCommand = "sudo nfd-stop"
subprocess.check_output(['bash', '-c', bashCommand])

bashCommand = "sudo nfd &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/nfd.log &"
subprocess.check_output(['bash', '-c', bashCommand])

time.sleep(3)
print "Set up forwarding path to M2"

bashCommand = "nfdc face create udp://192.168.56.106"
subprocess.check_output(['bash', '-c', bashCommand])

bashCommand = "nfdc route add /ndn/d-site udp://192.168.56.106:6363"
subprocess.check_output(['bash', '-c', bashCommand])

bashCommand = "nfdc route add /ndn/pref_a/pref_b/pref_c/pref_d/d-site udp://192.168.56.106:6363"
subprocess.check_output(['bash', '-c', bashCommand])

print "Loading FIB Entries"
for i in range(0,100):
    bashCommand = "nfdc route add /ndn/dummyPrefix_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])

for i in range(101,200):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(201,300):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_b_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(301,400):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a/pref_b_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(301,400):
    bashCommand = "nfdc route add /ndn/pref_a/pref_b/pref_c_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(401,500):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a/pref_b/pref_c_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(501,600):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a/pref_b/pref_c/pref_d_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(601,700):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a/pref_b/pref_c/pref_e_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(701,800):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a/pref_b/pref_c/pref_e/pref_d_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(801,900):
    bashCommand = "nfdc route add /ndn/pref_a/pref_b/pref_c/pref_d_"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


for i in range(901,1000):
    bashCommand = "nfdc route add /ndn/dummyPrefix/pref_a/pref_b/pref_c"+str(i)+" udp://192.168.56.106:6363"
    output = subprocess.check_output(['bash', '-c', bashCommand])


print "1000 Fib Entries Loaded"

print "Printing status"
bashCommand = "nfdc status show"
output = subprocess.check_output(['bash', '-c', bashCommand])


# logPath = "/home/lenovo/clientLogs.txt"
# print "Starting the pings"
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 1 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand,capture_output=False])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 1 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand,capture_output=False])
# print "Finshed 1/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 6001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 6001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 2/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 10000 -n 15001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 10000 -n 15001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 3/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 20000 -n 30001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 20000 -n 30001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 4/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 25000 -n 60001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 25000 -n 60001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 5/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 100001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 100001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 6/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 110001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 110001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 7/8"

# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 120001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 120001 > logPath"
# subprocess.check_output(['bash', '-c', bashCommand])
# print "Finshed 100%"

# print "Get the results"




