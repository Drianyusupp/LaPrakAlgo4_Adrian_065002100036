# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:35:05 2021

@author: User
"""

a = input("Isi List Angka (Integer) : ")

ganjil = []
genap = []
for a in a.split() :
        
    if int(a)%2 == 0 :
        print("List Angka Memiliki Nilai Genap")
        break
        
    if int(a)%2 != 0 :
        print("List Angka Tidak Memiliki Angka Genap")
        break
            
      