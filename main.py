from app.SysLogger import SysLogger

if __name__ == '__main__':
    process_name = input("Enter the name of the process you want to monitor: ")
    period = input("Enter the period in seconds you want to monitor: ")
    sampling = input("Enter the sampling interval in seconds: ")

    if not isinstance(process_name, str) or not period.isnumeric() or not sampling.isnumeric():
        print("Only numerical types supported")
        raise ValueError("Input Value is not correct")

    tst = SysLogger(process_name, int(period), int(sampling))
    tst.get_process_id()
    tst.start_monitoring()
    tst.report_generator()
