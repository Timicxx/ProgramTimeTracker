import psutil
import datetime
import json

processes = [proc.as_dict(attrs=['pid', 'name', 'create_time']) for proc in psutil.process_iter()]
print(processes)

