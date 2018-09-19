import subprocess

print "Fetching the status"
bashCommand = "nfdc status show > status.txt"
output = subprocess.check_output(['bash','-c', bashCommand])

