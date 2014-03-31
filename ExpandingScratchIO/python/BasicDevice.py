import RpiScratchIO
from RpiScratchIO.Devices import GenericDevice

class BasicDevice(GenericDevice):
  def __init__(self,deviceName_,scratchIO_,connections_):

    # Call the base class constructor
    super(BasicDevice, self).__init__(deviceName_,scratchIO_,connections_)

    # This device has a single input channel
    self.inputChannels += [0]

    # Add other code here if needed...
