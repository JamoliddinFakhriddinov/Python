# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 08:51:06 2024

@author: Jamoliddin
"""
# Sariq dev python kursinjng "FUNKSIYA" bo'limidagi Amaliyotdagi misollar

# 1.amaliyot

'''
def yilni_hisobla(ism, familia, yosh, joriy_yil=2024):
    """Foydalanuvchi ismi va familiasini so'rab, tug'ilgan yilini hisoblaydi"""
    print(f"{familia.title()} {ism.title()} siz {joriy_yil-yosh} - yilsiz!")
    
Ism = input('Ismingizni kiriting: ')
Familia = input('Familiangizni kiriting: ')
Yosh = int(input("Yoshingizni kiriting: "))
yilni_hisobla(Ism, Familia, Yosh)
'''

'''
# 2.amaliyot

def hisobla(son, kv, kub):
    """Foydalanuvchidan son olib, uni kvadrati hamda kubini hisoblaydi"""
    print(f"Siz kiritgan {son} ning kvadrati {kv} ga, kubi esa {kub} ga teng.")

son=int(input("Biror son kiriting: "))
Kv = pow(son,2)
Kub = pow(son,3)
hisobla(son, Kv, Kub)
'''
'''
def hisobla(son, daraja):
    """Foydalanuvchidan son olib, uni kvadrati hamda kubini hisoblaydi"""
    print(f"Siz kiritgan {son} ning {daraja} - darajasi {Daraja} ga teng.")

son=int(input("Biror son kiriting: "))
daraja=int(input("Sonni drajasini kiriting: "))
Daraja = pow(son,daraja)
hisobla(son, daraja)
'''

'''
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kv_kub(son):
    """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")


kv_kub(-4)
'''

'''
# 3.amaliyot

"""Foydalanuvchidan son olib, uni juft yoki toqligini aniqlaydi"""
def juftmi(son):
    if(son%2==0):
        print(f"Siz kiritgan {son} - juft son.")
    else:
        print(f"Siz kiritigan {son} - toq son.")
son = int(input("Biror son kiriting: "))
juftmi(son)

'''

