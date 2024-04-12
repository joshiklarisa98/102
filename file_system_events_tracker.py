import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = “<Set path for tracking file system events>”

class FileEventHandler:
    def on_created(self,event):
        # Called when a file or a directory is created
        pass

    def on_modified(self, event):
        # Called when a file or directory is modified
        pass

    def on_moved(self, event ):
        # Called when a file or a directory is moved or renamed
        pass

    def on_deleted(self, event):
        # Called when a file or directory is deleted
        pass

class EventHandler:
    def on_created(self, event):
        print(f'New file created: {event.src_path}')

    def on_deleted(self, event):
        print(f'File deleted: {event.src_path}')

    def on_modified(self, event):
        print(f'File modified: {event.src_path}')


event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=True)
observer.start()



try: 
    while True:
        time.sleep(2)
        print("running ... ")
except KeyboardInterrupt: 
    print("stopped!") 
    observer. stop()