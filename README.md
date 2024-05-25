# CS-432 Parallel & Distributed Computing  
## Semester Project Report

# Distributed File System

# How to Run
1.	Start File Manager:
python file_manager.py 
2.	Start Mutual Exclusion Service:
python mutual_exclusion.py 
3.	Start File Servers: 
cd primary_server
python primary.py 
(separately)
cd secondary_server1
python secondary1.py
(separately)
cd secondary_server2
python secondary1.py
4.	Start Client(s):
python client.py 


## Overview
This project implements a distributed file system (DFS) in Python, inspired by the Network File System (NFS) and some features of Google File System (GFS). It aims to provide a robust and efficient file storage solution distributed across multiple servers. Key features include fault tolerance, concurrency control, data replication, and caching, ensuring high availability and data consistency. The system consists of several components, including clients, a file manager, a mutual exclusion service employing the Suzuki-Kasami algorithm, an operation log, and multiple file servers.

## Objectives
- **High Availability:** Ensure the file system is accessible even if some servers fail.
- **Data Consistency:** Maintain consistency across distributed file servers.
- **Concurrency Control:** Prevent conflicts and ensure correct data access in a multi-client environment.
- **Fault Tolerance:** Enable the system to continue operating properly in the event of server failures.
- **Replication:** Distribute file copies across multiple servers to enhance availability and reliability.
- **Caching:** Improve performance by reducing latency in file read operations.

## Tools and Technologies
1. **Python:** Programming language used for implementing the entire project.
2. **Socket Programming:** For network communication between clients, services, and servers.
3. **CSV:** For storing file mappings and logs.
4. **Multithreading:** To handle multiple client requests concurrently.
5. **Suzuki-Kasami Algorithm:** For distributed mutual exclusion in the Mutual Exclusion Service.

## Key Components
1. **Clients**
2. **File Manager**
3. **Mutual Exclusion Service**
4. **File Servers (Primary, and two secondary)**
5. **Operation Log**

## Detailed Component Description

### Clients
The clients provide the user interface for performing file operations such as reading and writing. They interact with the directory and Mutual Exclusion Services to locate and access files safely. Clients handle user inputs and coordinate with the underlying library to perform the necessary operations.

### File Manager
The File Manager maintains a mapping of file names to file servers using a CSV file (file_mappings.csv). It provides clients with the information needed to locate files in the distributed system. When a client requests the location of a file, the File Manager responds with the appropriate server information.

### Mutual Exclusion Service
The Mutual Exclusion Service manages file locks using the Suzuki-Kasami distributed mutual exclusion algorithm. This ensures that only one client can write to a file at a time, preventing write conflicts and maintaining data consistency. The Mutual Exclusion Service keeps track of lock requests and grants tokens to clients based on the Suzuki-Kasami protocol.

### File Servers
Each file server (Primary, and two secondary) handles specific roles in the distributed file system:
- **Primary Server:**
  - Handles write operations.
  - Manages the main copy of files and updates replicated copies on secondary servers.
  - Logs all operations to an operation log for fault tolerance and recovery.
- **Secondary Server 1:**
  - Primarily handles read operations.
  - Maintains a replicated copy of the files from the primary server.
  - Can serve read requests to balance load and improve performance.
- **Secondary Server 2:**
  - Similar to Secondary Server 1, it primarily handles read operations.
  - Stores another replicated copy of files.
  - Enhances fault tolerance and load balancing.

### Operation Log
The operation log records all write operations performed by clients. This log is crucial for fault tolerance, allowing the system to recover and maintain consistency in case of server failures. The log helps in synchronizing file states across servers during recovery.

## Distributed Computing Concepts Applied
- **Fault Tolerance:** Achieved through replication and operation logging.
- **Concurrency Control:** Managed by the Suzuki-Kasami algorithm in the Mutual Exclusion Service.
- **Replication:** Files are replicated across secondary servers from the primary server.
- **Caching:** Implemented on the client side to reduce read latency and improve performance.
- **Load Balancing:** Read requests are distributed between secondary servers.

## Additional Notes
- Each file server should be run in a separate directory to simulate a distributed environment.
- Multiple clients can be launched in different terminals to simulate concurrent file operations.
- The file manager and mutual exclusion services must be started before launching the file servers and clients.

