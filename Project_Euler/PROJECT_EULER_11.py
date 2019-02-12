#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
product1=0
product2=0
product3=0  
product4=0
for i in range(0,17):
    for j in range(0,17):
        
        phorizontal=grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if product1<=phorizontal:
            product1=phorizontal
        
            
        pvertical=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if product2<=pvertical:
            product2=pvertical
        pcross=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if product3<=pcross:
            product3=pcross
            
        pcross1=grid[19-i][j]*grid[18-i][j+1]*grid[17-i][j+2]*grid[16-i][j+3]
        if product4<=pcross1:
            product4=pcross1   
        if i==16:
            j=0
            for i in range(16,20):
                for j in range(0,17):
                    phorizontal=grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
                    if product1<=phorizontal:
                        product1=phorizontal
        if j==16:
            i=0
            for i in range(0,17):
                for j in range(16,20):
                    pvertical=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
                    if product2<=pvertical:
                        product2=pvertical
                    
            
print(max(product1,product2,product3,product4))            
