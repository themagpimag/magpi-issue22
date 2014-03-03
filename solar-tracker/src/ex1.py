month_str = getMonth()
filepath = '/home/pi/RST/Months/' + month_str + '.txt'
rawData = np.loadtxt(filepath, dtype=(str, float), usecols=(0,2))

motor_const = 0.462 # Units of deg/sec based upon speed of motor

angle_deg = np.zeros((len(rawData),1), dtype=(float))
motor_dir = np.zeros((len(rawData),1), dtype=(int))
motor_time = np.zeros((len(rawData),1), dtype=(int))

def readDayData:
  z = 0
  while(z < len(rawData)):
    loop_time[z,0] = int(convTimeSec(rawData[z,0]))

    if(z == 0):
      if(float(rawData[z,1]) <= 90):
        angle_deg[z,0] = 90 - float(rawData[z,1])
        motor_dir[z,0] = -1
        motor_time[z,0] = angle_deg[z,0]/motor_const
      else:
        angle_deg[z,0] = float(rawData[z,1]) - 90
        motor_dir[z,0] = 1
        motor_time[z,0] = angle_deg[z,0]/motor_const
    else:
      angle_deg[z,0] = float(rawData[z,1]) - float(rawData[z-1,1])
      motor_dir[z,0] = 1
      motor_time[z,0] = angle_deg[z,0]/motor_const

    z = z + 1
