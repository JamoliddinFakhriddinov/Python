# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:58:57 2024

@author: Jamoliddin
"""

'''
ismlar = ['Ali','Vali','Hasan','Husan','Olim','Jamoliddin','Isomiddin']
j = 0
for i in ismlar:
    print(f"Salom {i}")
    j+=1
print(f"{j} marta takrorlandi.")

'''

'''
def salom_ber():
    """ Salom beruvchi funksiya """
    print("Assalomu alaykum!")
'''

'''
def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}.")
    print(salom_ber.__doc__)
'''

'''
def salom_ber(ism, familiya):
    """Foydalanuvchi ismini, familiyasini hamda tug'ulgan yilini
qabul qilib, unga ism va familiyasi aytib salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {familiya.title()} {ism.title()}")
    print(salom_ber.__doc__)
'''

'''
def ism_familiya(ism, familiya):
    """Foydalanuvchi ismini, familiyasini hamda tug'ulgan yilini
qabul qilib, unga ism va familiyasi aytib salom beruvchi funksiya"""
    print(f"Foydalanuvchi familiyasi: {familiya.title()}\n")
    print(f"Foydalanuvchi ismi: {ism.title()}")
'''

'''
def ism_familiya(ism, familiya, tugilgan_yil):
    """Foydalanuvchi ismini, familiyasini hamda tug'ulgan yilini
qabul qilib, unga ism va familiyasi aytib salom beruvchi funksiya"""
    print(f"Foydalanuvchi familiyasi: {familiya.title()}\n")
    print(f"Foydalanuvchi ismi: {ism.title()}")
    print(f"{familiya.title()} {ism.title()} {2024-tugilgan_yil} yoshda.")
'''

'''
def ism_familiya(ism='Ziyoviddin', familiya='Shamsiddinov', tugilgan_yil='2020'): 
print(f"{familiya.title()} {ism.title()} {2024-tugilgan_yil} yoshda.")
'''

'''
def yosh_hisobla(ism, familia, tugilgan_yil, joriy_yil=2024):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"{familia} {ism} siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
ism = input('Ismingizni kiriting: ')
familia = input('Familiangizni kiriting: ')
yosh_hisobla(familia, ism, tyil)
'''
















