import os
import RpiScratchIO
from RpiScratchIO.Devices import GenericDevice

class Ping(GenericDevice):
  def __init__(self,deviceName_,rpiScratchIO_,connections_):

    # Call the base class constructor
    super(Ping, self).__init__(deviceName_,rpiScratchIO_,connections_)

    # This device has a single input channel
    self.inputChannels += [0]

    # The default host, in case no host is configured
    self.hostname = "localhost"

    # Add the input channels as sensors to Scratch
    self.addSensors()


  #-----------------------------

  def config(self,argList):
    nargs = len(argList)
    if nargs == 0:
      print("WARNING: \"config\" in device %s expects at least one argument.  No arguments were given" % self.deviceName)
      return None

    # Set new host name to ping
    self.hostname = argList[0]

  #-----------------------------

  def read(self,channelId):

    # Check if this is a valid input channelId
    channelNumber = self.validInputChannel(channelId)
    if channelNumber == -1:
      return None

    # Run ping once with a timeout of one second and collect the return value
    ret_value = os.system('ping -c 1 -w 1 ' + self.hostname)
    if ret_value == 0:
      value = 1
    else:
      value = 0

    # Since there might be a significant delay, send Scratch a trigger message.
    self.broadcastTrigger(channelId) 

    # Send the value back to Scratch
    self.updateSensor(channelId,value)
