#!/bin/bash
# Iniciar el servicio SSH
set -e
# custom_config
sudo service ssh start
sudo chmod 0660 /dev/i2c-1
sudo chgrp i2c /dev/i2c-1
source /opt/ros/humble/setup.bash
exec "$@"