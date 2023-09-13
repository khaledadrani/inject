from setuptools import setup

setup(
    name='Inject',
    version='0.0.1',
    description='A Dependency Injection Framework For Python Projects',
    author='Khaled Adrani',
    author_email='khaledadrani@gmail.com',
    url='https://github.com/khaledadrani/inject',
    packages=['inject'],
    install_requires=[
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',

)
