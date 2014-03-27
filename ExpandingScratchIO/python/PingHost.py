import subprocess,string
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

    # Setup the ping command to run once
    ping = subprocess.Popen(
      ["ping", "-c", "1", self.hostname],
      stdout = subprocess.PIPE,
      stderr = subprocess.PIPE
    )

    # Set the default value to indicate something went wrong
    avgRoundTrip = -999

    # Run the ping command
    out, error = ping.communicate()

    # Parse the standard out and error
    if string.find(error,'unknown host') != -1: # LINUX specific
      avgRoundTrip = -2
    elif string.find(out,'100% packet loss') != -1: # LINUX specific
      avgRoundTrip = -1
    else:
      for line in string.split(out,'\n'):
        # This search string is Linux specific
        if string.find(line,'rtt min/avg/max/mdev') == -1:
          continue
        frags = string.split(line,' = ')
        if len(frags) != 2:
          print "WARNING: badly formatted string"
          continue
        values = string.split(frags[1],'/')
        if len(values) < 2:
          print "WARNING: badly formatted values string"
          continue
        avgRoundTrip = float(values[2])

    # Send the value back to Scratch
    self.updateSensor(channelId,avgRoundTrip)

    # Since there might be a significant delay, send Scratch a trigger message.
    self.broadcastTrigger(channelId) 
