import setuptools
with open("README.rst", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='sysreports',  
     version='1.0',
     scripts=['hellosriram'] ,
     author="Sriram Sreedhar",
     author_email="sriramsreedhar003@gmail.com",
     description="Hello Sriram",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/sriramsreedhar/hellosriram.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7 :: 3.0",
         "License :: OSI Approved :: MIT  License",
         "Operating System :: OS Independent",
     ],
 )
