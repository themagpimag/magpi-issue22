class DataLoggingThread(threading.Thread):
  def __init__(self, threadID, stop_data_log, delay):
    super(DataLoggingThread, self).__init__(self)
    self.threadID = threadID
    self.delay = delay

  def run(self):
    ADS1015 = 0x00
    adc = ADS1x15(ic=ADS1015)
    logging.info(timestamp() + ': Running data logging thread.')
    while not stop_data_log.isSet():
      file = open('/home/pi/RST/Data/' + today + '.txt','a')
      voltage = adc.readADCSingleEnded(1, 4096, 250) / 1000
      file.write(timestamp() + '\t' + str(voltage))
      current = adc.readADCSingleEnded(2, 4096, 250)/ 1000
      file.write('\t' + str(current) + '\n')
      file.close()
      time.sleep(self.delay)
    logging.info(timestamp() + ': Exiting data logging thread.')
