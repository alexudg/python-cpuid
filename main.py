import subprocess
command = 'wmic cpu get processorid'
output = subprocess.getoutput(command)
print ('result:', output)
lines = output.splitlines()
noLine = 0
for line in lines:
    noLine += 1
    if noLine == 3:
        processorId = line
        print('linea ' + str(noLine), processorId)
print(processorId, len(processorId.strip()))