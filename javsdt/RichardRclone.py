import rclone

cfg_path = r'C:\Users\Richard\.config\rclone\rclone.conf'
with open(cfg_path) as f:
   cfg = f.read()
result = rclone.with_config(cfg).listremotes()
print(result.get('out'))

result1 = rclone.with_config(cfg).run_cmd(command="ls", extra_args=["mydrive:/", "--drive-trashed-only ","-v", "--dry-run"])
print(result1.get('out'))