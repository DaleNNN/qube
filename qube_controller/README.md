Denne pakken implementerer en PID-kontroller for Quanser Qube i ROS2. Kontrolleren leser posisjon og hastighet fra Quben og beregner en hastighetskommando som sendes til motoren.

Kontrolleren bruker et PID-oppsett med P-, I- og D-ledd, og håndterer vinkler korrekt ved å bruke korteste vei rundt sirkelen.

## Hvordan kjøre:

Start først hele systemet:

```
ros2 launch qube_bringup bringup.launch.py
```

Deretter start kontrolleren:

```
ros2 run qube_controller pid_controller
```

## Topics:

### Abonnerer på:

- `/joint_states` (posisjon og hastighet fra Quben)
- `/target_position` (ønsket vinkel i radianer)

### Publiserer til:

- `/velocity_controller/commands` (hastighetskommando)

## Hvordan bruke:

Sett ønsket vinkel ved å publisere til `/target_position`:

```
ros2 topic pub /target_position std_msgs/msg/Float64 "{data: 1.0}"
```

Kontrolleren vil da prøve å regulere Quben til denne vinkelen.

## Parametere (i kode):

- `kp` – proporsjonal gain  
- `ki` – integral gain  
- `kd` – derivat gain  
- `max_command` – maks tillatt kommando  
- `max_integral` – begrensning på integrator (anti-windup)  
- `output_scale` – skalering av kontrollsignal  
