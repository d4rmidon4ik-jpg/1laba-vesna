import json
import subprocess

data = {"message": "1 laba?"}

process = subprocess.Popen(
    ["go", "run", "main.go"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

stdout, _ = process.communicate(input=json.dumps(data))

print("Ответ от Go:", stdout)
