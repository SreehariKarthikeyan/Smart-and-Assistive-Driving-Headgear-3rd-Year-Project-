# Smart-and-Assistive-Driving-Headgear-3rd-Year-Project-
This is my 3rd year college project. A helmet with a heads-up display enhanced with Augmented reality, which aids the rider in viewing route. 
It has an accident detection module, which detects the accident through vibration sensors placed at points where probability of getting hit is high and sends 
message to the priority contacts with the location of the mishap.


#Module 1:(Switching on the bike)
The rider wears the helmet. The pressure sensor gives high output when pressure is applied. 
This data is sent to the microcontroller. The microcontroller processes the input and sends it to the bike module via RF transmitter. 
The bike module receives the signal via RF receiver and send to the microcontroller. 
If the pressure sensor is high, it implies that helmet is worn, hence the bike will start else it will not start.

#Module 2:(Heads up Display)
As soon as the rider wears the helmet, it is connected to the mobile device via Bluetooth. The mobile device checks if the HUD is switched on.
If the HUD is switched on then it sends all data including current navigation, calls and message notifications to the microcontroller. 
The microcontroller processes this data and then displays it on the HUD.

#Module 3:(Detecting an accident)
When the helmet is worn by the rider, the vibration sensor is activated. It continuously measures the intensity of the vibration and sends this data to the microcontroller. 
The microcontroller processes this input and if the intensity of the vibration is above the set threshold value then signal is sent to mobile device via Bluetooth.
The mobile device responds by getting the crash location via GPS and sends this information to the emergency services and other two contacts via an installed application.

