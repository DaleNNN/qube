Denne pakken brukes til å starte hele Qube-systemet i ROS2. Den kobler sammen beskrivelse (qube\_description), driver (qube\_driver) og visualisering (RViz).



Innhold:



\- launch/bringup.launch.py  

&#x20; Starter hele systemet (driver, robot\_state\_publisher og RViz)



\- urdf/controlled\_qube.urdf.xacro

&#x20; URDF med både robotbeskrivelse og ROS2 Control-konfigurasjon





Hvordan kjøre:



ros2 launch qube\_bringup bringup.launch.py





Parametere:



\- baud\_rate (default: 115200)  

\- device (default: /dev/ttyACM0)  

\- simulation (default: false)  



Eksempel:



Kjør med simulering:



bash

ros2 launch qube\_bringup bringup.launch.py device:=/dev/ttyACM0 baud\_rate:=115200 simulation:=true

