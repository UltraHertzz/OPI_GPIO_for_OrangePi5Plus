FROM ros:humble-ros-base-jammy as builder

ENV ROS_WS=/root/ros_ws
#WORKDIR /home/orangepi/ros2_ws
WORKDIR $ROS_WS

COPY ./ src/car_driver

RUN apt-get update && \
    apt-get install python3-pip -y && \
    # cd / && \
    # git clone https://github.com/UltraHertzz/OPI_GPIO_for_OrangePi5Plus.git && \
    # pip install OPi.GPIO && \
    # cp -r /OPI_GPIO_for_OrangePi5Plus/OPi/ /usr/local/lib/python3.10/dist-packages/ && \
    cd $ROS_WS/ && colcon build && \
    apt-get remove --purge -y python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Attention: it's better not to use core image to build car driver. because the modification 
#            in OPi package need sudo group, which is not included in core image.

FROM ros:humble-ros-core-jammy

ENV ROS_WS=/root/ros_ws

WORKDIR ${ROS_WS}

COPY --from=builder ${ROS_WS}/install ${ROS_WS}/install

RUN apt-get update && \
    apt-get install python3-pip -y && \
    apt-get install git -y && \
    # cd / && \
    # git clone https://github.com/UltraHertzz/OPI_GPIO_for_OrangePi5Plus.git && \
    # pip install OPi.GPIO && \
    # cp -r /OPI_GPIO_for_OrangePi5Plus/OPi/ /usr/local/lib/python3.10/dist-packages/ && \
    apt-get remove --purge -y python3-pip && \
    apt-get remove --purge -y git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
CMD [ "/bin/bash" ,"-c", "source ${ROS_WS}/install/setup.bash && \
                          export ROS_DOMAIN_ID=30 && \
                          ros2 run car_driver drive_node" ]
