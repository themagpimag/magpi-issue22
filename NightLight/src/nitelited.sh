#!/bin/sh
# /etc/init.d/nitelited 

### BEGIN INIT INFO
# Provides: nitelited
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Simple script to start a program at boot
# Description: A simple script from www.stuffaboutcode.com which will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting nitelited"
    # run application you want to start
    python /home/pi/Downloads/nitelited.py &
    ;;
  stop)
    echo "Stopping nitelited"
    # kill application you want to stop
    pkill -INT -f "python /home/pi/Downloads/nitelited.py"
    ;;
  *)
    echo "Usage: /etc/init.d/nitelited {start|stop}"
    exit 1
    ;;
esac

exit 0 
