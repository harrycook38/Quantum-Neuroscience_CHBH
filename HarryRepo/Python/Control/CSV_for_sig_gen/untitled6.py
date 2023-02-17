# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:43:38 2023

@author: vpixx
"""
import numpy as np
import matplotlib.pyplot as plt

length = np.ones(10000)

A = [0, 0.5, 1, 1.5, 2, 5, 10, 20]

pp_conv = 3.073e-3 # V(amp)/pTcm

sig = np.zeros((len(A),len(length)))

for i in range(len(A)):
    sig[i,:] = A[i]*pp_conv*length
    
output = sig.flatten()

plt.figure()
plt.plot(output)


np.savetxt("0_20pT_steps.csv", output, delimiter=",")