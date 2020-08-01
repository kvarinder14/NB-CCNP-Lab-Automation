# Author: Varinder Kumar
# 19 Sept 2019


#####################################################NOTE#################################################################
    #This Script should be used when you are accessing the rack first time after boot.
    #User the script ** CCNP_RACK_REGAIN.py ** to continue the access on already accessed device




 #Accessing the CCNP RACK Easily With automated Script in Secure CRT.



# IMPORTANT: Some commmands are commented can be uncommented as per required by user.

def main():

	

	# Ask for The Last Octet of The Rack You want to access
	ip=crt.Dialog.Prompt("Enter the Last Octet of IP Address Of Rack")
	# Intiating the Telent(Port 23) Sesson 
	Clear_S = crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")
	
	Clear_S.Screen.Synchronous = True

	#Asking for username and sending to console
	Clear_S.Screen.WaitForString("Username:")
	user=crt.Dialog.Prompt("Enter the username")
	Clear_S.Screen.Send(user + "\r")

	#Asking for password and sending to console
	Clear_S.Screen.WaitForString("Password:")
	password=crt.Dialog.Prompt("Enter the Password")
	Clear_S.Screen.Send(password+"\r")

	#Clearing all The lines.

	Clear_S.Screen.WaitForString(">")
	Clear_S.Screen.Send("cl 33\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 34\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 35\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 36\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 37\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 38\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 39\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 40\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 41\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 42\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 43\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 44\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 45\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 56\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 47\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 48\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	Clear_S.Screen.Send("cl 49\r")
	Clear_S.Screen.WaitForString("]")
	Clear_S.Screen.Send("\r")
	

	#Waiting for 2000 msec to complete all pending req.
	crt.Sleep(2000)

	# Accessing the Each Device in Tab

	r1 =  crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	r1.Screen.WaitForString("Username:")
	r1.Screen.Send(user + "\r")
	r1.Screen.WaitForString("Password:")
	r1.Screen.Send(password+"\r")
	r1.Screen.WaitForString('>')
	r1.Screen.Send("r1\r")
	
	



	r2 =  crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	r2.Screen.WaitForString("Username:")
	r2.Screen.Send(user + "\r")
	r2.Screen.WaitForString("Password:")
	r2.Screen.Send(password+"\r")
	r2.Screen.WaitForString('>')
	r2.Screen.Send("r2\r")
	r2.Screen.Send("\r")



	r3 =  crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	r3.Screen.WaitForString("Username:")
	r3.Screen.Send(user + "\r")
	r3.Screen.WaitForString("Password:")
	r3.Screen.Send(password+"\r")
	r3.Screen.WaitForString('>')
	r3.Screen.Send("r3\r")
	r3.Screen.Send("\r")



	r4 =crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	r4.Screen.WaitForString("Username:")
	r4.Screen.Send(user + "\r")
	r4.Screen.WaitForString("Password:")
	r4.Screen.Send(password+"\r")
	r4.Screen.WaitForString('>')
	r4.Screen.Send("r4\r")
	r4.Screen.Send("\r")



	sw1 = crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	sw1.Screen.WaitForString("Username:")
	sw1.Screen.Send(user + "\r")
	sw1.Screen.WaitForString("Password:")
	sw1.Screen.Send(password+"\r")
	sw1.Screen.WaitForString('>')
	sw1.Screen.Send("sw1\r")
	sw1.Screen.Send("\r")




	sw2 =  crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	sw2.Screen.WaitForString("Username:")
	sw2.Screen.Send(user + "\r")
	sw2.Screen.WaitForString("Password:")
	sw2.Screen.Send(password+"\r")
	sw2.Screen.WaitForString('>')
	sw2.Screen.Send("sw2\r")
	sw2.Screen.Send("\r")

	


	sw3 =  crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	sw3.Screen.WaitForString("Username:")
	sw3.Screen.Send(user + "\r")
	sw3.Screen.WaitForString("Password:")
	sw3.Screen.Send(password+"\r")
	sw3.Screen.WaitForString('>')
	sw3.Screen.Send("sw3\r")
	sw3.Screen.Send("\r")





	sw4 =  crt.Session.ConnectInTab("/TELNET 100.0.0." +ip + " 23")

	sw4.Screen.WaitForString("Username:")
	sw4.Screen.Send(user + "\r")
	sw4.Screen.WaitForString("Password:")
	sw4.Screen.Send(password+"\r")
	sw4.Screen.WaitForString('>')
	sw4.Screen.Send("sw4\r")
	sw4.Screen.Send("\r")





# Wait For 6 Sec

	crt.Sleep(6000)
	r1.Screen.Send("\r")
	r2.Screen.Send("\r")
	r3.Screen.Send("\r")
	r4.Screen.Send("\r")
	sw1.Screen.Send("\r")
	sw2.Screen.Send("\r")
	sw3.Screen.Send("\r")
	sw4.Screen.Send("\r")

# After Access Skipping intial Setup

	r1.Screen.Send("no\r")
	r2.Screen.Send("no\r")
	r3.Screen.Send("no\r")
	r4.Screen.Send("no\r")
	sw1.Screen.Send("no\r")
	sw2.Screen.Send("no\r")
	sw3.Screen.Send("no\r")
	sw4.Screen.Send("no\r")


# Enter 

	r1.Screen.Send("\r")
	r2.Screen.Send("\r")
	r3.Screen.Send("\r")
	r4.Screen.Send("\r")
	sw1.Screen.Send("\r")
	sw2.Screen.Send("\r")
	sw3.Screen.Send("\r")
	sw4.Screen.Send("\r")

# Wait for 10 sec then Enter

	crt.Sleep(10000)
	r1.Screen.Send("\r")
	r2.Screen.Send("\r")
	r3.Screen.Send("\r")
	r4.Screen.Send("\r")
	sw1.Screen.Send("\r")
	sw2.Screen.Send("\r")
	sw3.Screen.Send("\r")
	sw4.Screen.Send("\r")

# Wait 15 sec to get devices started and to get into user Mode
# Then get into Enable mode and Setup Hostname

	crt.Sleep(15000)
	r1.Screen.Send("en\r")
	r2.Screen.Send("en\r")
	r3.Screen.Send("en\r")
	r4.Screen.Send("en\r")
	sw1.Screen.Send("en\r")
	sw2.Screen.Send("en\r")
	sw3.Screen.Send("en\r")
	sw4.Screen.Send("en\r")

# Getting into Privlange Mode

	r1.Screen.Send("conf t\r")
	r2.Screen.Send("conf t\r")
	r3.Screen.Send("conf t\r")
	r4.Screen.Send("conf t\r")
	sw1.Screen.Send("conf t\r")
	sw2.Screen.Send("conf t\r")
	sw3.Screen.Send("conf t\r")
	sw4.Screen.Send("conf t\r")

# Give Each Device Hostname

	r1.Screen.Send("ho R-1\r")
	r2.Screen.Send("ho R-2\r")
	r3.Screen.Send("ho R-3\r")
	r4.Screen.Send("ho R-4\r")
	sw1.Screen.Send("ho SW-1\r")
	sw2.Screen.Send("ho SW-2\r")
	sw3.Screen.Send("ho SW-3\r")
	sw4.Screen.Send("ho SW-4\r")

# # Some Useful Line console 0  Config 

# 	r1.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	r2.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	r3.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	r4.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	sw1.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	sw2.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	sw3.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")
# 	sw4.Screen.Send("line console 0\r exec-timeout 0 0\r logging synchronous\r history size 100\r exit\r")

# # Other Config mode config 
#
# 	r1.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	r2.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	r3.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	r4.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	sw1.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	sw2.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	sw3.Screen.Send("no ip domain-lookup\r no logging console \r")
# 	sw4.Screen.Send("no ip domain-lookup\r no logging console \r")

# # Default switch port configurations 

# 	sw1.Screen.Send("default int range fa1/0/1-24 \r")
# 	sw1.Screen.Send("default int range fa2/0/1-24 \r")
# 	sw1.Screen.Send("default int range fa3/0/1-24 \r")
# 	sw1.Screen.Send("default int range fa4/0/1-24 \r")

# 	sw2.Screen.Send("default int range fa1/0/1-24 \r")
# 	sw2.Screen.Send("default int range fa2/0/1-24 \r")
# 	sw2.Screen.Send("default int range fa3/0/1-24 \r")
# 	sw2.Screen.Send("default int range fa4/0/1-24 \r")

# 	sw3.Screen.Send("default int range fa0/1-24 \r")

# 	sw4.Screen.Send("default int range fa0/1-24 \r")



	#Setting Up Tab Name

	r1.Caption='R--1'
	r2.Caption='R--2'
	r3.Caption='R--3'
	r4.Caption='R--4'
	sw1.Caption='SW--1'
	sw2.Caption='SW--2'
	sw3.Caption='SW--3'
	sw4.Caption='SW--4'
	

main()
































