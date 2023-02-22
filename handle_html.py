# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:02:32 2023

@author: bvranic
"""

with open(r"C:\Users\bvranic\Documents\leadResponse.txt") as f:
    data = f.read()
    
    
lines = data.split('\n')    
target_line  = ""
for i, line in enumerate(lines):
    if 'id="leadId"' in line:
        print(lines[i+1])
        target_line = lines[i+1]
        break
    
lead_id = target_line.split('"')[1]
with open(r"C:\Users\bvranic\Documents\leadId.txt", "w") as f:
    f.write(lead_id)
        
promene