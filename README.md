# Qube ROS2 Mini-prosjekt

Dette prosjektet implementerer et komplett ROS2-system for styring av en Quanser Qube. Systemet består av flere pakker som samarbeider for å beskrive roboten, kommunisere med maskinvare eller simulator, og regulere vinkelen ved hjelp av en PID-kontroller.

---

## Struktur

Prosjektet består av følgende pakker:

- **qube_description**  
  Inneholder URDF/Xacro-beskrivelse av Quben. Brukes til visualisering og som grunnlag for resten av systemet.

- **qube_driver**  
  Håndterer kommunikasjon med fysisk Qube (eller simulering) via ROS2 Control.

- **qube_bringup**  
  Starter hele systemet. Kobler sammen URDF, driver, robot_state_publisher og RViz.

- **qube_controller**  
  Implementerer en PID-kontroller som styrer vinkelen til Quben.

---

## Hvordan kjøre

1. Bygg workspace:

- colcon build
- source install/setup.bash
- ros2 launch qube_bringup bringup.launch.py

2. Kjør pid_controller:
- ros2 run qube_controller pid_controller

3. Sett vinkel:
- ros2 topic pub /target_position std_msgs/msg/Float64 "{data: 1.0}"


