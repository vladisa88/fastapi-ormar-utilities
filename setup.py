from os import path
from setuptools import setup, find_packages

directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.1.0'
DESCRIPTION = 'Small, but usefull library for interaction with Ormar ORM'

# Setting up
setup(
        name="fastapi-ormar-utilities",
        version=VERSION,
        author="Vladislav Isakov",
        author_email="vladisa88@gmail.com",
        url="https://github.com/vladisa88/fastapi-ormar-utilities",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=['pydantic', 'ormar', 'fastapi'],
        keywords=['python', 'ormar', 'async', 'fastapi', 'pydantic'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Operating System :: OS Independent",
            "Topic :: Internet",
            "Topic :: Office/Business",
            "Topic :: Software Development :: Libraries",
        ]
)
