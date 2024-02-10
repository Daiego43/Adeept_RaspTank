FROM osrf/ros:humble-desktop-full
LABEL authors="daiego"

# Configuración SSH
RUN apt-get update && apt upgrade -y && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:rasptank' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd && \
    echo "export VISIBLE=now" >> /etc/profile \

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && rm -rf /requirements.txt
COPY rasptank_control /rasptank_control
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]