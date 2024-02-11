FROM ros:humble
LABEL authors="daiego"




# Instalamos utilidades
RUN apt-get update && \
    apt-get install -y openssh-server \
    python3-pip \
    iproute2 \
    ranger \
    libgl1-mesa-glx

# Instalamos dependencias Python3.10 de nuestro proyecto
# Así las tenemos tambien con las de ROS2
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt && rm -rf /requirements.txt
VOLUME /dev:/dev
# Copiamos el script de inicio
COPY start.sh /start.sh
RUN rm -rf /ros_entrypoint.sh
ENTRYPOINT ["/bin/bash", "/start.sh"]
CMD ["bash"]
# Definimos al usuario rasptank, que es igual al usuario que se encuentra en la Raspberry Pi
ARG USER=rasptank
ARG UID=1000
ARG GID=$UID

RUN groupadd --gid $GID $USER && \
    useradd -m -s /bin/bash --uid $UID --gid $GID $USER && \
    echo "$USER:$USER" | chpasswd && \
    usermod -aG sudo $USER && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER



