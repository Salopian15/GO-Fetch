from setuptools import setup, find_packages

setup(
    name='GO-Fetch',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'numpy',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'go-fetch=main.cli:run'
        ],
    },
    author='Jack A. Crosby',
    author_email='jac180@aber.ac.uk',
    description='CLI interface to grab GO terms for a list of protein IDs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/GO-Fetch',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)