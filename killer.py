import subprocess

output = subprocess.check_output('tasklist', shell=True).split("\r\n")

pids = [ line.split()[1] for line in output if 'chrome.exe' in line ]

for pid in pids:
    subprocess.call('taskkill /f /pid ' + pid, shell=True)
    