import threading
from time import sleep

lock = threading.Lock()

def test1():
  print("TEST 1 - Lock Aquire")
  lock.acquire()
  sleep(5)
  print("TEST 1 - Done")
  lock.release()
  print("TEST 1 - Lock Release")

def test2():
  print("TEST 2 - Wait lock")
  with lock:
    print("TEST 2 - Available")

thread1 = threading.Thread(target=test1)
thread2 = threading.Thread(target=test2)
thread1.start()
thread2.start()