import threading
import time
import psutil
import GPUtil
import os
import subprocess

SECONDS_TO_RUN = 30

# Function to append words to a list for 30 seconds
def append_words(target_list):
    start = time.time()
    while time.time() - start < SECONDS_TO_RUN:
        target_list.append("word")
        # time.sleep(0.01)
    # print( f'done; list length: ``{len(target_list)}``' ) 
    ## print length of target_list in human-readable format with commas
    print( f'done; list length: ``{len(target_list):,}``' )


# Function to track CPU, GPU, and memory usage for 30 seconds
def track_resources():
    start = time.time()
    while time.time() - start < SECONDS_TO_RUN:
        # Track CPU
        cpu_usage = psutil.cpu_percent(interval=1)

        # Track Memory
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        ## Track GPU ------------------------------------------------
        ''' doesn't work '''
        # gpus = GPUtil.getGPUs()
        # gpu_usage = [(gpu.id, gpu.load) for gpu in gpus]
        # for gpu_id, gpu_load in gpu_usage:
        #     print(f"GPU {gpu_id} Usage: {gpu_load * 100}%")
        # print(f"gpu_usage: {gpu_usage}%")

        '''
        TODO: check out...
        - <https://github.com/tlkh/asitop> and 
        - <https://www.unix.com/man-page/osx/1/powermetrics/> (which asitop uses)
        '''

        # Print stats
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")

        time.sleep(1)

if __name__ == "__main__":
    # List to append words
    word_list = []

    # Start threads
    word_thread = threading.Thread(target=append_words, args=(word_list,))
    resource_thread = threading.Thread(target=track_resources)

    word_thread.start()
    resource_thread.start()

    word_thread.join()
    resource_thread.join()

    print("Completed!")
