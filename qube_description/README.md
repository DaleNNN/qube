Denne pakken inneholder en URDF/Xacro-beskrivelse av Quanser Qube for bruk i ROS2.



Innhold:



\- urdf/qube.macro.xacro

&#x20; Inneholder en gjenbrukbar Xacro-makro som beskriver selve Quben.



\- urdf/qube.urdf.xacro

&#x20; En enkel scene som instansierer Quben og plasserer den i verden.



\- launch/view\_qube.launch.py 

&#x20; Starter visualisering av Quben i RViz.



\- config/qube\_config.rviz

&#x20; RViz-konfigurasjon for visualisering.





\## Hvordan kjøre





Bygg workspace og kjør:



source install/setup.bash

ros2 launch qube\_description view\_qube.launch.py

