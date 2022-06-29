# medovi40k 2022

import os
import json
import xml.etree.ElementTree as ET

def getdeviceid():
	b=os.popen("adb root & adb shell cat /data/data/com.valvesoftware.android.steam.community/shared_prefs/steam.uuid.xml").read()
	myroot = ET.fromstring(b)
	deviceid = [e.text for e in myroot.findall('.//string')]
	return deviceid[0]
if __name__ == '__main__':
	a=os.popen('adb root & adb shell cat /data/data/com.valvesoftware.android.steam.community/files/*')

	data1=json.load(a)
	steamid=data1["steamid"]
	f1 = open("replacement.maFile", "r")
	f2 = open(steamid+".maFile", "w")

	f2.write(f1.read())
	f2.close()
	f1.close()

	with open(steamid+".maFile", "r") as file1:
		file=file1.read()
		file=file.replace("REPLACEMENTN1", data1["shared_secret"], 1)
		file=file.replace("REPLACEMENTN2", data1["serial_number"], 1)
		file=file.replace("REPLACEMENTN3", data1["revocation_code"], 1)
		file=file.replace("REPLACEMENTN4", data1["uri"], 1)
		file=file.replace("REPLACEMENTN5", data1["server_time"], 1)
		file=file.replace("REPLACEMENTN6", data1["account_name"], 1)
		file=file.replace("REPLACEMENTN7", data1["token_gid"], 1)
		file=file.replace("REPLACEMENTN8", data1["identity_secret"], 1)
		file=file.replace("REPLACEMENTN9", data1["secret_1"], 1)
		file=file.replace("REPLACEMENTN10", getdeviceid(), 1)
		file=file.replace("REPLACEMENTN11", data1["steamid"], 1)

		with open(steamid+".maFile", "w") as file2:
			file2.write(file)

