# Author: Varinder Kumar
# 19 Sept 2019

#**************************************************NOTE******************************************
# If you are accessing the rack first time after boot
# use the other script **CCNP_RACK_FIRST.phy** which have MORE FUNCATIONALITY .








 #Accessing the CCNP RACK Easily With automated Script in Secure CRT.

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


