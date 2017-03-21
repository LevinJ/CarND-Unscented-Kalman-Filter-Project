import sys
import os
# from _pickle import dump
sys.path.insert(0, os.path.abspath('..'))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


class AnalyzeResult(object):
    def __init__(self):
       
        return
    def __load_input_data(self,kalman_input_file):
        
        print('loading {}.....'.format(kalman_input_file))
     
        
        
        cols = ['type','px_est','py_est','vel_abs','yaw_angle','yaw_rate','vx_est','vy_est','px_meas','py_meas','nis','px_gt','py_gt','vx_gt','vy_gt']
        df = pd.read_csv(kalman_input_file, sep= '\t',names = cols, header=None)
        csv_file_name = os.path.dirname(kalman_input_file) + '/result_analysis/' + os.path.basename(kalman_input_file)[:-4] +'.csv'
        df.to_csv(csv_file_name)
        print(csv_file_name + ' saved')
        return df
    
    def disp_nis(self, df):
        
        
        # Two subplots, unpack the axes array immediately
        f, (ax1, ax2) = plt.subplots(2, 1, sharey=True)
        
        sub_df = df[df['type'] =='L']
        low_thres = 0.103
        high_thres = 5.991
        ax1.plot(sub_df.index.values, sub_df['nis'])
        ax1.plot([sub_df.index.values[0], sub_df.index.values[-1]], np.full(2, low_thres))
        ax1.plot([sub_df.index.values[0], sub_df.index.values[-1]], np.full(2, high_thres))
        ax1.set_title('lidar nis')
        
        low_thres = 0.352
        high_thres = 7.815
        sub_df = df[df['type'] =='R']
        ax2.plot(sub_df.index.values, sub_df['nis'])
        ax2.plot([sub_df.index.values[0], sub_df.index.values[-1]], np.full(2, low_thres))
        ax2.plot([sub_df.index.values[0], sub_df.index.values[-1]], np.full(2, high_thres))
        ax2.set_title('radar nis')
        plt.show()
        return
    
    
    def visulize_data(self,df):
        plt.scatter(df['px_gt'], df['py_gt'],marker='*', color='blue')
        plt.scatter(df['px_meas'], df['py_meas'],marker='v',color='red')
        plt.show()
        return
    def run_data_1(self):
        print('####data sample 1###')
        kalman_input_file = r'../data/sample-laser-radar-measurement-data-1_output.txt'
        df = self.__load_input_data(kalman_input_file)
        self.disp_nis(df)

        return df
    def run_data_2(self):
        print('####data sample 2###')
        kalman_input_file = r'../data/sample-laser-radar-measurement-data-2.txt'
        df = self.__load_input_data(kalman_input_file)
        self.__cal_input_rmse(df)
        return df
    
   
        
    def run(self):
        self.run_data_1()
#         self.run_data_2()
        
#         self.visulize_data(df)

        return



if __name__ == "__main__":   
    obj= AnalyzeResult()
    obj.run()