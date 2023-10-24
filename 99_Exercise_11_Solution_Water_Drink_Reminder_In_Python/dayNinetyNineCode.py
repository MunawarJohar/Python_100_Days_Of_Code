import os
import time
#it is for mac
Repeat_interval=10
while True:

    command=f'''osascript -e 'say'"Hello world"'; osascript -e' 'display alert \ " hey munawar. Drink water"\"\''
    os.system(command)
    time.sleep(Repeat_interval)