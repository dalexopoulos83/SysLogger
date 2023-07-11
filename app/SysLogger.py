import os
import pandas as pd
import time
import numpy as np


class SysLogger:

    def __init__(self, process_name, monitoring_duration, sampling_interval=5):
        self.process_name = process_name
        self.monitoring_duration = monitoring_duration
        self.sampling_interval = sampling_interval

    def get_process_id(self):
        process_id = os.popen('pgrep ' + self.process_name).read()
        return process_id

    def start_monitoring(self):
        top_out = ""
        pid = self.get_process_id()

        smps = round(self.monitoring_duration / self.sampling_interval)
        interval = self.sampling_interval
        top_command = 'top -pid ' + pid.strip() + ' -n 1 -o -PID -l 1 | awk \'{print $1,$2,$3,$8,$9,$10}\''
        lsof_command = 'lsof -p ' + pid.strip() + ' | wc -l'

        for _ in np.arange(0, smps):
            top_out += os.popen(top_command).read()
            top_out += "File_descriptors " + os.popen(lsof_command).read().strip() + '\n\n'
            time.sleep(interval)

        file = open('top_out.log', 'w')
        file.write(top_out)
        file.close()

    def avg_calc(self, data_frame, column):
        df_temp = data_frame[column].str.extract('(\d+)', expand=False)
        df_temp = df_temp.astype(int)
        avg = df_temp.mean()
        return avg

    def max_value(self, data_frame, column):
        df_temp = data_frame[column].str.extract('(\d+)', expand=False)
        df_temp = df_temp.astype(int)
        max = df_temp.max()
        return max

    def pandas_cleanup_top_data(self):
        top_raw_dataset = pd.read_table("top_out.log", header=None)
        top_df_1 = top_raw_dataset[top_raw_dataset[0].str.contains("PID|470") == True]
        top_dataset_list = list(top_df_1[0])
        top_line_split = [line.split(' ') for line in top_dataset_list]
        top_df_2 = pd.DataFrame(top_line_split)
        top_df_3 = top_df_2.rename(columns=top_df_2.iloc[0]).loc[1:]
        top_df = top_df_3[top_df_3["PID"].str.contains("PID") == False]

        fd_df = top_raw_dataset[top_raw_dataset[0].str.contains("File_descriptors") == True]
        fd_df_list = list(fd_df[0])
        fd_line_split = [line.split(' ') for line in fd_df_list]
        fd_df = pd.DataFrame(fd_line_split)
        return top_df, fd_df

    def report_generator(self):
        top_df, fd_df = self.pandas_cleanup_top_data()
        fd_avg = fd_df[1].astype(int).mean()

        mem_avg = self.avg_calc(top_df, 'MEM')
        cpu_avg = self.avg_calc(top_df, '%CPU')
        memory_leak = self.memory_leak_calculator(mem_avg, fd_avg, top_df)

        report = {'Average %CPU Usage': [cpu_avg], 'Average Memory Usage': [mem_avg], 'File descriptors': [fd_avg], 'Memory leak': memory_leak}
        df = pd.DataFrame(report)
        print(df)
        print(memory_leak)
        df.to_csv('Report.csv', header=True, index=False, sep=',')

    def memory_leak_calculator(self, mem_avg, fd_avg, top_df):
        if self.max_value(top_df, 'MEM') < mem_avg and self.max_value(top_df, 0) < fd_avg:
            result = 'Warning memory leak detected!!!!'
        else:
            result = 'No memory leak detected'
        return result
