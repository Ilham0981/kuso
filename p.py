import subprocess

def run_ssh_command(host, username, password, port, command):
    ssh_command = f'sshpass -p {password} ssh {username}@{host} -p {port} "{command}"'
    try:
        result = subprocess.run(ssh_command, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except Exception as e:
        return False, str(e)

# Usage
host = 'your_host'
username = 'your_username'
password = 'your_password'
port = 22  # Replace with your desired port
command = 'ls -l'  # Replace with your desired command

success, output = run_ssh_command(host, username, password, port, command)
if success:
    print('Command executed successfully:')
    print(output)
else:
    print('Error executing command:')
    print(output)
