import Regression 
from scipy import stats
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 25, 30, 40, 48, 60, 50, 80]

Regression.main(x,y)

n = len(x)
df = n - 1
MSR = Regression.ssr(x,y)/1
MSE = Regression.sse(x,y)/(n - 2)
F = MSR/MSE
df_regression = 1
df_residual = n - 2
pvalue = stats.f.sf(F, df_regression, df_residual)

print("Source of Variation" + "      " + "Sum of Squares" + "       " + "df" + "        " + "Mean Square" + "        " + "F" + "               " + "p-value")
print(f"Regression (explained)    {Regression.ssr(x, y)}    1    {MSR}      {F}     {pvalue}")
print(f"Regression (unexplained)    {Regression.sse(x, y)}   {df_residual}    {MSE}")
print(f"Total                      {Regression.sst(x, y)}             {df}")