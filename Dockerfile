FROM ros:humble
LABEL authors="daiego"

VOLUME /dev:/dev

ARG USER=rasptank
ARG UID=1000
ARG GID=$UID


RUN groupadd --gid $GID $USER && \
    useradd -m -s /bin/bash --uid $UID --gid $GID $USER && \
    echo "$USER:$USER" | chpasswd && \
    usermod -aG sudo $USER && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER && \
    groupadd i2c && \
    usermod -aG i2c $USER

RUN echo "source /opt/ros/humble/setup.bash" >> /home/$USER/.bashrc && \
    echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Instalamos utilidades
RUN apt-get update && \
    apt-get install -y openssh-server \
    python3-pip \
    iproute2 \
    ranger \
    libgl1-mesa-glx

RUN echo "Port 2222" >> /etc/ssh/sshd_config
# Instalamos dependencias Python3.10 de nuestro proyecto
# Así las tenemos tambien con las de ROS2
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt && rm -rf /requirements.txt
# Copiamos el script de inicio
COPY start.sh /start.sh
RUN rm -rf /ros_entrypoint.sh
ENTRYPOINT ["/bin/bash", "/start.sh"]
# Definimos al usuario rasptank, que es igual al usuario que se encuentra en la Raspberry Pi








