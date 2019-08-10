import subprocess

host1 = 'yandex.ru'
host2 = 'youtube.com'
ping1 = subprocess.Popen(
    ['ping', '-n', '4', host1],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
out1 = ping1.communicate()
ping2 = subprocess.Popen(
    ['ping', '-n', '4', host2],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
out2 = ping2.communicate()
print(out1[0].decode('866'))
print(out2[0].decode('866'))
