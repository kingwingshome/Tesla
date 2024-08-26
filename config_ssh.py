# 导入必要的Python库
import os
import subprocess
 
# 步骤1: 设置root用户密码
password = "kinglong"
command = f"echo 'root:{password}' | chpasswd"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    print("Root密码设置成功")
else:
    print("设置root密码失败:", result.stderr.decode())
 
# 步骤2: 修改/etc/ssh/sshd_config以允许root登录
sshd_config_addition = "PermitRootLogin yes\n"
with open("/etc/ssh/sshd_config", "a") as sshd_config:
    sshd_config.write(sshd_config_addition)
print("已添加PermitRootLogin yes到sshd_config")
 
# 步骤3: 重启SSH服务
result = subprocess.run(["service", "ssh", "restart"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    print("SSH服务重启成功")
else:
    print("SSH服务重启失败:", result.stderr.decode())
 
# 步骤4: 修改LD_LIBRARY_PATH环境变量
os.environ["LD_LIBRARY_PATH"] = ':'.join(filter(lambda x: '/opt/conda/lib' not in x, os.getenv("LD_LIBRARY_PATH", "").split(':')))
print("LD_LIBRARY_PATH已更新")
