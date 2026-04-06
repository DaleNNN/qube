Denne pakken inneholder en URDF/Xacro-beskrivelse av Quanser Qube for bruk i ROS2.

## Innhold

- `urdf/qube.macro.xacro`  
  Inneholder en gjenbrukbar Xacro-makro som beskriver selve Quben.

- `urdf/qube.urdf.xacro`  
  En enkel scene som instansierer Quben og plasserer den i verden.

- `launch/view_qube.launch.py`  
  Starter visualisering av Quben i RViz.

- `config/qube_config.rviz`  
  RViz-konfigurasjon for visualisering.

## Hvordan kjøre

Bygg workspace og kjør:

```bash
source install/setup.bash
ros2 launch qube_description view_qube.launch.py
