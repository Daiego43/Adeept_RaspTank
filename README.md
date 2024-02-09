# My Rasptank

Estoy estudiando el código del rasptank para aprender como programar el hardware y hacer una
interfaz para controlarlo desde ROS.

## Hardware: Sensores

El hardware del rasptank es el siguiente:

### Servos

Los servos van conectados a la Adafruit PCA9685 que es un controlador de servos de 16 canales.
El controlador se conecta al Raspberry Pi mediante I2C.

Con la librería de Adafruit se pueden controlar los servos y por tanto he realizado una clase
para controlar los servos de forma básica.

Haciendo un poco de experimentación he podido concluir los siguientes valores para controlar los servos:
Se especifica Angulo maximo y minimo y el valor inicial.

| Servo  | Pin | Min | Max | Inicial |
|--------|-----|-----|-----|---------|
| Pinza  | 15  | 0   | 90  | 90      |
| Muñeca | 14  | 0   | 180 | 80      |
| Codo   | 13  | 0   | 135 | 110     |
| Brazo  | 12  | 0   | 180 | 120     |
| Cámara | 11  | 70  | 120 | 110     |

La posicion inicial tambien será la posicion Home. Aparte he tenido que programar los servos por mi
cuenta ya que creo que tengo dos servos defectuosos que causan el reinicio de la raspberry pi.

### Motores
Se ha hecho otra interfaz un poco más clara para controlar los motores, el angulo en la trayectoria
se especificará a través de ROS.