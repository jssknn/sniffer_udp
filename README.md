# sniffer_udp
Aplicación realizada en Python con scapy para tomar paquetes udp e insertarlos en MongoDB.

Servicio Web hecho con Flask para consultar los registros creados en MongoDB.
- Se debe correr el sniffer.py para realizar la escucha pasiva de los paquetes sobre el puerto indicado en el código y su posterior inserción en la base de datos MongoDB.
- server.py es el servicio que se debe ejecutar para montar la aplicación web.

Las consultas de registros se hacen a través de la siguiente web:

![imagen](https://github.com/jssknn/sniffer_udp/blob/main/logs.PNG)

Como resultado se obtiene una tabla que es posible exportarla a xls.
