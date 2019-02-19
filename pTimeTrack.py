import psutil
import datetime
import json
import asyncio


SCAN_DELAY = 1000

previous_processes = {}


def save(processes):
  with open('output/started.json', 'w') as f:
    json.dump(0, f)


def get_all_running_processes_as_dict():
  processes = [proc.as_dict(attrs=['pid', 'name', 'create_time']) for proc in psutil.process_iter()]
  return processes


def processes_to_pid_list(processes):
  if not processes or type(processes) is not dict:
    return []
  pid_list = [process['pid'] for process in processes.]
  return pid_list


def compare_processes(previous_processes, current_processes):
  previous_pid_list = processes_to_pid_list(previous_processes)
  current_pid_list = processes_to_pid_list(current_processes)

  stopped_processes = set(previous_pid_list).difference(current_pid_list)
  
  for pid in set(current_pid_list).difference(previous_pid_list):
    if pid in current_pid_list.items()
  
  return compared_processes


def scan():
  current_processes = get_all_running_processes_as_dict()
  compared_processes = compare_processes(previous_processes, current_processes)
  
  save()
  previous_processes = current_processes
  
if __name__ == "__main__":
  while(True):
    scan()
    sleep(SCAN_DELAY)
