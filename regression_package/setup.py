#!/usr/bin/env python
# coding: utf-8

# In[7]:


import setuptools
from setuptools import setup, find_packages
    
setuptools.setup(
    name="Regression",
    version="0.0.1",
    author="Isabel Osgood",
    author_email="isabel.osgood@du.edu",
    description="This package has all the functions to conduct a linear regression with two lists as",
    long_description_content_type="text/markdown",
    url="https://github.com/belosgood/hw3.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


# In[ ]:




