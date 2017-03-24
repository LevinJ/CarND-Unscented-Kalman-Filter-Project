# Unscented Kalman Filter Project Starter Code
Self-Driving Car Engineer Nanodegree Program

---

### Overview
The goals / steps of this project are the following:  

* Complete the Unscented Kalman Filter algorithm in C++.
* Apply it to pedestrian position/speed estimation problem 
* Evaluate it again two sampled data, the metrics used is RMSE

### Final Result

1. sample data I
Accuracy - RMSE: 
0.0824666  
0.0878453  
0.644505  
0.584015  

2. sample data II
Accuracy - RMSE:  
0.15118  
0.189515  
0.237983  
0.287951  

Note that the elements in RMSE vector corresponds to [px, py, vx, vy]  

### Interesting Charts

1. nis lidar

![nis lidar](https://github.com/LevinJ/CarND-Extended-Kalman-Filter-Project/blob/master/pedestrian_tracking_2.png)

We use normalized innovation squared to evaluate if the process noise (nu_a, nu_yawdd) is appropriate for the estimation problem in this problem. In general,if we have too many larege nis values throughout the estimation process, it means that underestimation the noise in system, and would want to increase it. On the other side, if we have many small values throughout the estimation process, it means that overestimation the noise in system, and would want to increase it. From this chart, we can see for lidar data, the process noise chosen is appropriate.  

2. nis_radar
![nis_radar](https://github.com/LevinJ/CarND-Extended-Kalman-Filter-Project/blob/master/pedestrian_tracking_2.png)

from this chart, there are some room for improvement here. The nis values a bit too large, which means we could further fine tune the system by increase process noise or initial covariance matrix.  

3. position estimation  

![position estimation](https://github.com/LevinJ/CarND-Extended-Kalman-Filter-Project/blob/master/pedestrian_tracking_2.png)

4. velocity estimation

![velocity estimation](https://github.com/LevinJ/CarND-Extended-Kalman-Filter-Project/blob/master/pedestrian_tracking_2.png)

5. yaw angle estimation

![yaw angle estimation](https://github.com/LevinJ/CarND-Extended-Kalman-Filter-Project/blob/master/pedestrian_tracking_2.png)


## Dependencies

* cmake >= v3.5
* make >= v4.1
* gcc/g++ >= v5.4

## Basic Build Instructions

1. Clone this repo.
2. Make a build directory: `mkdir build && cd build`
3. Compile: `cmake .. && make`
4. Run it: `./UnscentedKF path/to/input.txt path/to/output.txt`. You can find
   some sample inputs in 'data/'.
    - eg. `./UnscentedKF ../data/sample-laser-radar-measurement-data-1.txt output.txt`
