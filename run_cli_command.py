import subprocess
import sys

auto_add = "--auto-add" in {*sys.argv}
command = [arg for arg in sys.argv[1:] if arg != "--auto-add"]

subprocess.run(command)
if auto_add:
    subprocess.run(["git", "add", "-u"])
