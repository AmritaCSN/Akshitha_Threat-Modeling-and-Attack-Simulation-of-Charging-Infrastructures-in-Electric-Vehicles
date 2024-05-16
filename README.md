# Akshitha_Threat-Modeling-and-Attack-Simulation-of-Charging-Infrastructures-in-Electric-Vehicles
This repository contains the code for executing the project: "Threat Modeling and Attack Simulation of Charging Infrastructures in Electric Vehicles".

**Project Overview**

The purpose of this project is to comprehensively analyze the security risks 
and vulnerabilities inherent in Electric Vehicle (EV) charging infrastructures, 
encompassing Electric Vehicles, charging stations, and the grid.To do so, our 
project have tree section:

Threat modeling: This section focuses on identifying possible 
risks to the electric vehicle infrastructure.

Attack Simulation: This section focuses on identifying possible 
risks to the electric vehicle infrastructure.

Security requirements: This section focuses on to outlining a 
few possible solutions for the vulnerabilities found.


**Why the Project is Useful**

 Through the application of threat modeling methodologies, the study aims to 
identify potential threats and attack vectors that could compromise the 
integrity, availability, and confidentiality of EV charging networks. Also by 
utilizing the Mininet network emulator, the study will simulate the operation 
of EVs and charging stations within a controlled environment. The findings 
of this research will provide a practical insights for improving EV charging 
infrastructure security.

**Getting Started with the Project**

To get started with the project, you have to install the following tools.

For Threat modeling
* Microsoft Threat Modeling Tool (TMT), you can download it 
from its official website.

* Automotive Threat Modeling Template.

For EV Charging Network Simulation

* Virtual Machine

* Ubuntu 22.0

* Kali Linux

* Mininet

You also need to have sudo access to run Mininet inside Ubuntu.

For performing the simulation, first we have to setup Ubuntu and Kali inside the 
VM. Once Ubuntu is installed follow the following steps for installing Mininet 
inside Ubuntu.

* Open command line terminal in Ubuntu
* Set the root password
* sudo apt-get install mininet
* sudo mn -c
* sudo apt-get install git
* git clone git://github.com/mininet/mininet
* mininet/util/install.sh -a

Once the Mininet is installed run Mininet by following the command, 

* Open a terminal
* Login as a superuser(root)
* cd mininet -> changing directory to mininet
* mkdir directory_name -> creating new directory inside mininet
* cd directory_name
* create 3 python files inside the new directory, these .py files will have the code for simulating the behaviour of electric_vehicle, charging station, and network topology (electric_vehicle.py, charging.py, topology.py).

For Attack Simulation

We can simulate the attack by following the instruction

* Open kali linux/ open a terminal in mininet
* sudo apt-get install hping3 -> for simulating attack

Once the hping3 is installed, the attack can be performed in kali by following the command.

* sudo hping3 -i u1 -S -p <port> --rand-source <charging_station_ip>

**Detailed Explanation of the code**

The code topology.py will create a network topology with two hosts(electric vehicle & charging station) and one switch(s1) for establishing the connection between two hosts. Once the network topology is created the code electric_vehicle.py has the function for sending authentication credentials, and charging request to the charging station. Similarly the code in charging.py will has the function for handling the EV request and authentication. once the EV is authenticated it will displays authentication successfull and it start the charging process after the specified period of time it will stop the charging session.

For running the codes you have to open 4 terminals parallelly, start the charging station by running the python3 charging.py script in one terminal within your Mininet environment, similary for topology and electric vehicle (python3 thopology.py, python3 electric_vehicle.py). Before running these command you have to be in superuser mode and also in the directory where these 3 codes saved. Because the mininet will only run with root privillage. you can run wireshark inside the mininet environment for capturing the packet flow between ev and charging station by using the command: sudo wireshark &.

You can perform the attack either from the mininet environment or from a kali machine. For launching the attack open a terminal in kali/mininet and run the command: sudo hping3 -i u1 -S -p <port> --rand-source <charging_station_ip>, here replace the ip address and port number with the charging station ip address and port number. For analyzing the impact of attack we can open the system monitor using the command: gnome-system-monitor. capture the cpu & memory utilization of the system before and after launching the attack. 

**Architectural Block Diagram**

![alt text](https://github.com/AmritaCSN/Akshitha_Threat-Modeling-and-Attack-Simulation-of-Charging-Infrastructures-in-Electric-Vehicles/blob/main/ev%20communication.PNG)







