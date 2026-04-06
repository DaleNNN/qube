Denne pakken brukes til å starte hele Qube-systemet i ROS2. Den kobler sammen beskrivelse (`qube_description`), driver (`qube_driver`) og visualisering (RViz).

## Innhold:

- `launch/bringup.launch.py`  
  Starter hele systemet (driver, `robot_state_publisher` og RViz)

- `urdf/controlled_qube.urdf.xacro`  
  URDF med både robotbeskrivelse og ROS2 Control-konfigurasjon

## Hvordan kjøre:

```
ros2 launch qube_bringup bringup.launch.py
```

## Parametere:

- `baud_rate` (default: 115200)  
- `device` (default: /dev/ttyACM0)  
- `simulation` (default: false)  

## Eksempel:

Kjør med simulering:

```bash
ros2 launch qube_bringup bringup.launch.py device:=/dev/ttyACM0 baud_rate:=115200 simulation:=true
```
