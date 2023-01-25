from setuptools import setup, find_packages
import pypandoc

VERSION = '0.0.3' 
DESCRIPTION = 'My first Python package'


# LONG_DESCRIPTION = 'My first Python package with a slightly longer description'
# LONG_DESCRIPTION = pypandoc.convert_file('README.md', 'rst')



# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="test", 
        version=VERSION,
        author="Yong Wah",
        author_email="yongwahooi97@gmail.com",
        description=DESCRIPTION,
        long_description=open("README.md", 'r').read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)