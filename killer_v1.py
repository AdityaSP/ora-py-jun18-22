import subprocess

#collect the output of tasklist
output = subprocess.check_output('tasklist', shell=True)
#print type(output)
#print output[:500]


# split the output as lines
output_lines = output.split("\r\n")
#print output_lines[:5]

#collect only those lines which have chrome.exe
chrome_lines = filter(lambda line: 'chrome.exe' in line, output_lines)
#print chrome_lines[:5]

chrome_lines = [ line for line in output_lines if 'chrome.exe' in line ]
#print chrome_lines[:5]

#get the pids of chrome
pids = map(lambda line: line.split()[1], chrome_lines)
print pids

pids = [ line.split()[1] for line in chrome_lines]
print pids

#loop through the pids and pass it to taskkill

for pid in pids:
    subprocess.call('taskkill /f /pid ' + pid, shell=True)
