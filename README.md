## 1. Prerequisites
### 1.1 **Ubuntu** and **ROS**
Ubuntu 64-bit 16.04 or 18.04.
ROS Kinetic or Melodic. [ROS Installation](http://wiki.ros.org/ROS/Installation) and its additional ROS pacakge:

```
    sudo apt-get install ros-XXX-cv-bridge ros-XXX-tf ros-XXX-message-filters ros-XXX-image-transport
```


### 1.2. **Ceres Solver**
Follow [Ceres Installation](http://ceres-solver.org/installation.html).

### 1.3. **PCL**
Follow [PCL Installation](http://www.pointclouds.org/downloads/linux.html).

**NOTICE:** Recently, we find that the point cloud output form the voxelgrid filter vary form PCL 1.7 and 1.9, and PCL 1.7 leads some failure in some of our examples ([issue #28](https://github.com/hku-mars/loam_livox/issues/28)). By this, we strongly recommand you to use update your PCL as version 1.9 if you are using the lower version.

## 2. Build
Clone the repository and catkin_make:

```
    cd ~/catkin_ws/src
    git clone https://github.com/zengy5/loam_livox_zyx.git
    cd ../
    catkin_make
    source ~/catkin_ws/devel/setup.bash
```
## 3. Directly run
    roslaunch loam_livox rosbag_mid100.launch