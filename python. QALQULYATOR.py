# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:29:43 2022

@author: Ogabek
"""

print("Pythontilida yozilgan kalkulyator")    
def calculator(son1,son2):
    """Python tilida yozilgan kalkulyator"""
    son = {'son1':son1,
           'son2':son2}
         
    return son

print("\nArifmetik amallarni bajarish uchun son kiriting\n")
san = []
tarix = []

while True:
    son1 = int(input("Birinchi sonni kiriting: "))
    son2 = int(input("Ikkinchi sonni kiriting kiriting: "))

    print(san)
    san.append(calculator(son1,son2))
    print(san)
    javob = input("Yana son qo'shasizmi?  (yes/no)")
 
    if javob=='no':
        break
        
        
print(f"{son1 + son2}")
      
print(san)

for sonlar in san:
    hisob = (f"Qo'shish: {son1}+{son2} = {son1+son2} \n"
          f"Ayirish: {son1}-{son2} = {son1-son2} \n\n"
          f"Ko'paytirish: {son1}*{son2} = {son1*son2} \n\n"
          f"Bo'lish: {son1}/{son2} = {son1/son2} \n\n"
          f"O'nlik bo'lish: {son1}//{son2} = {son1//son2} \n\n"
          f"Daraja: {son1}**{son2} = {son1**son2} \n\n"
          f"Bo'linmani qoldig'i: {son1}%{son2} = {son1%son2} \n\n"
          f"Katta son: {son1}>{son2} = {son1>son2} \n\n"
          f"Kichik son: {son1}<{son2} = {son1<son2} \n\n")
tarix.append(hisob)
 
print(hisob)

print(f"Sizning tarixingiz {tarix}")
