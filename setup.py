from setuptools import setup, find_packages

setup(
    name = 'template-applier',
    version='0.0.1',
    author="jyp",
    author_email="bit6449@naver.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        'console_scripts':[
            'clickscript = templateApplier.main:main'
        ]
    }
    
)


print("hello setup")