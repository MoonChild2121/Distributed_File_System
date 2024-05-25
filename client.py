import sys
import client_manager
from datetime import datetime
import csv
import os
from time import gmtime, strftime

CSV_FILE = "operation_log.csv"

def log_operation(process_id, operation, success):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([strftime("%Y-%m-%d %H:%M:%S", gmtime()), process_id, operation, "yes" if success else "no"])

def main():

    print ("\n")
    client_manager.instructions()
    client_id = strftime("%Y%m%d%H%M%S", gmtime())
    file_version_map = {}
    file_version_map = {}
    process_id = os.getpid()

    while True:
       
        client_input = sys.stdin.readline()
            
        if "<write>" in client_input:
            while not client_manager.check_valid_input(client_input):       # error check the input
                 client_input = sys.stdin.readline()
            
            filename = client_input.split()[1]      # get the filename from the input
            response = client_manager.handle_write(filename, client_id, file_version_map)    # handle the write request
            if response == False:
                print("File unlock polling timeout...")
                print("Try again later...")
                log_operation(process_id, "write", False)
            else:
                log_operation(process_id, "write", True)
            print ("Exiting <write> mode...\n")
            

        if "<read>" in client_input:
            while not client_manager.check_valid_input(client_input):    # error check the input
                 client_input = sys.stdin.readline()

            filename = client_input.split()[1]   # get file name from the input
            client_manager.handle_read(filename, file_version_map, client_id)        # handle the read request 
            log_operation(process_id, "read", True)
            print("Exiting <read> mode...\n")
        

        if "<instructions>" in client_input:
            client_manager.instructions()
            log_operation(process_id, "instructions", True)



        if "<quit>" in client_input:
            log_operation(process_id, "quit", True)
            print("Exiting application...")
            sys.exit()

if __name__ == "__main__":
    main()