# System Monitoring App

This is a simple implementation of a process monitoring app. 

## General Info 
The app have a simple structure where in the class SysLogger under the folder app we have implemented a process monitoring tool. 
It is taking as arguments the process name, the monitoring interval and the number of samples we want to capture. Also, the app 
have a memory leak detection implementation and is generating a report with the average CPU usage, the average memory usage, 
the average file descriptors and if there is or there is not any memory leak.
Under the SysLogger folder also are stored the report with the name "Report.csv", and the monitoring logs during the 
specific period under the name "top_out.log". 
The file "monitoring_process.py" is the one we call in order to execute the app. 


    SysLogger
    |
    |---app
    |    |---SysLogger.py
    |
    |---test
    |    |---SysLoggerTest.py
    |
    |---monitoring_process.py
    
    
## How To
In order to run the application from CLI we have to call the "monitoring_process.py", then we will prompt to give the 
name of the process we want to monitor, the period in sec we want to monitor it and the sampling interval, which 
by default is 5 sec.

    dimitrisalexopoulos@192 SysLogger % python monitor_process.py 
    Enter the name of the process you want to monitor: firefox
    Enter the period in seconds you want to monitor: 10
    Enter the sampling interval in seconds: 2
    
## Miscellaneous
The application have been developed and tested on MAC environment, but it should be ok in every nix env. 
For the execution of the app the following libraries should be installed on the system: 

    pip install numpy
    pip install pandas
    pip install pytest
