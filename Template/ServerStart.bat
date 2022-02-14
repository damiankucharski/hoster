@echo off

:start_server
echo Starting Tekkit Classic Reloaded R1.1
java -server -Xms1024M -Xmx4096M -XX:+UseG1GC -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UnlockExperimentalVMOptions -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -Dfml.readTimeout=180 -jar forge-1.12.2-14.23.5.2847-universal.jar nogui
exit /B

goto start_server
