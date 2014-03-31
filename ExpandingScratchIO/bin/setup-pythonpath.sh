# To be appended to ~/.bashrc or sourced before running
# RpiScratchIO with a user-defined device.
#
user_devices=$HOME/user-devices
if [[ -z $PYTHONPATH ]]; then
  export PYTHONPATH=$user_devices
elif [[ $PYTHONPATH != *"$user_devices"* ]]; then 
  export PYTHONPATH="$PYTHONPATH:$user_devices"
fi
unset user_devices
