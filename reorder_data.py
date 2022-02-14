import numpy as np
import pandas as pd

# specify columns
cols = ['index', 'tag', 'xorig', 'x', 'y', 'z', 'adcerror', 'adcmeans', 'faerror', 'fameans', 'mderror', 'mdmeans']
# create dataframe
df = pd.DataFrame([], columns = cols)

# load origdata 
origdata = pd.read_csv('~/neonatewebsite/new_values.csv')

# dictionaries
xs = [1,2,3,4,5,6,7,8,9,10,11,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
xorigs=['L11', 'L10', 'L9', 'L8', 'L7', 'L6', 'L5', 'L4', 'L3', 'L2', 'L1', 'M0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11']

# find row or create empty one
def create_row(index,x,y,z):
    xstring = xorigs[x]
    search = f'{str(xstring)}_{str(y)}_{str(z)}'
    #print(search)   
    row = origdata.loc[origdata['tag'] == search]
    #print(row)   
    try: 
        adc_e = row['adcerror'].item()
        adc_m = row['adcmeans'].item()
        fa_e = row['faerror'].item()
        fa_m = row['fameans'].item()
        md_e = row['mderror'].item()
        md_m = row['mdmeans'].item() 
    except: 
        adc_e = ""
        adc_m = ""
        fa_e = ""
        fa_m = ""
        md_e = ""
        md_m = ""
    newrow = pd.DataFrame([[index, search, xstring, x+1, y, z, adc_e, adc_m, fa_e, fa_m, md_e, md_m]], columns = cols)
    return newrow

# loop through z
index = 0 
for z_count in range(24):
    z_value = 34 + z_count * 4

# loop through y     
    for y_count in range(32):
        y_value = 40 + y_count * 5

# loop through x       
        for x_count in range(23): 
            this_row = create_row(
                index, 
                x_count, 
                y_value, 
                z_value
            )      
            df = df.append(this_row)
    
    index +=1
