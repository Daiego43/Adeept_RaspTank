#!/bin/bash
# Iniciar el servicio SSH
set -e
# custom_config
sudo service ssh start
source /opt/ros/humble/setup.bash
exec "$@"