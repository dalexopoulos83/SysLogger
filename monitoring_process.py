from app.SysLogger import SysLogger

if __name__ == '__main__':
    process_name = input("Enter the name of the process you want to monitor: ")
    period = input("Enter the period in seconds you want to monitor: ")
    sampling = input("Enter the sampling interval in seconds: ")

    tst = SysLogger(process_name, int(period), int(sampling))
    tst.start_monitoring()
