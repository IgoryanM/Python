import time

class TrafficLight:
	
	__color = ['red', 'yellow', 'green']
	
	def running(self):
		print (self.__color[0])
		time.sleep(7)
		print (self.__color[1])
		time.sleep(2)
		print (self.__color[2])
		time.sleep(5)

tr_light = TrafficLight()
tr_light.running()
		
		
	