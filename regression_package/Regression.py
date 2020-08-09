#!/usr/bin/env python
# coding: utf-8

# In[49]:


##create all new functions
def mean(x):
    n = len(x)
    sigma = sum(x)
    return sigma/n


def variance(x):
    n = len(x)
    sigma = 0 
    for i in x:
        a = ((i - mean(x)**2))
        sigma +=a
    return sigma/(n-1)

def covariance(x, y):
    if len(x) == len(y):
        n = len(x)
        sigma = 0
        for i in range(0, len(x)):
            #print(i)
            #print(x[i]) 
            a = (x[i] - mean(x))*(y[i] - mean(y))
            sigma += a
        return sigma/(n-1)

def coeff(x, y):
    if len(x) == len(y):
        b1 = covariance(x, y)/variance(x)
        b0 = mean(y) - b1*mean(x)
        d = {'b1': b1, 'b0': b0}
        return d
    
def yhat(x, y):
    d = coeff(x, y)
    b1 = d['b1']
    b0 = d['b0']
    yhat_form = f"{b0} + {b1}*x"
    yhat_list = []
    for i in x:
        yhat = b0 + (b1*i)
        yhat_list.append(yhat)
    return yhat_list
    #this isnt exactly correct but follows the hw - my stats is a little rusty 
    
def residuals(x, y):
    es = []
    yhat_res = yhat(x, y)
    n = 0
    for i in y:
        a = i - yhat_res[n]
        es.append(a)
        n += 1
    return es

def sse(x, y):
    residual = residuals(x, y)
    total = 0
    for e in residual:
        e2 = e**2
        total += e2
    return total

def ssr(x, y):
    ssr = 0 
    yi = yhat(x, y)
    for i in yi:
        sigma = (i - mean(y))**2
        ssr += sigma
    return ssr 

def sst(x, y):
    sst = 0
    for i in y:
        sigma = (i - mean(y))**2
        sst += sigma
    return sst

def r_squared(x, y):
    r2 = ssr(x, y)/sst(x, y)
    return r2

def mse(x, y):
    n = len(x)
    mse = sse(x, y)/n
    return mse

def main(x, y):
    covar = covariance(x, y)
    print(covar)
    d = coeff(x, y)
    intercept = d['b0']
    slope = d['b1']
    print(intercept)
    print(slope)
    r = r_squared(x, y)
    print(r)
    m = mse(x, y)
    print(m)
    
    
#test 
#main(x = [2, 4, 6, 8, 10, 15, 20], y = [10, 15, 17, 25, 40, 42, 50])   

def main2():
    pass
if __name__ == "__main__":
    main2()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




