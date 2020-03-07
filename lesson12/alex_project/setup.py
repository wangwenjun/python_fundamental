from distutils.core import setup
from setuptools import find_packages
setup(
        name = 'alex',
        version = '2020.01.05',
        description = 'this is my first setup project',
        long_description = 'looooooooooooooooooooooooooooooooooooog description',
        author = 'Alex Wang',
        author_email = 'xxxx@gmail.com',
        url = 'alexwang.github.com/test/fun',
        license = 'ASF 2.0',
        install_requires = [],
        classifiers = [
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Natural Language :: Chinese (Simplified)',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Utilities'
            ],
        keywords = 'package,install,setup,example', 
        packages = find_packages('src'),
        package_dir = {'':'src'},
        include_package_data = True
)
