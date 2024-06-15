from setuptools import setup, find_packages

setup(
    name='daiego43_rasptank',
    version='0.0.9',
    author='Daiego43',
    author_email='diedelcha@gmail.com',
    description='This is a clearer implementation of a library to interact with the Adeept rasptank robot. Pins are hardcoded',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Daiego43/Adeept_RaspTank',
    packages=find_packages(),
    install_requires=[
        "Adafruit-GPIO>=1.0.3",
        "Adafruit-PCA9685>=1.0.1",
        "RPi.GPIO>=0.7.1",
        "gpiozero>=2.0",
        "spidev>=3.6",
        "opencv-python>=4.8"
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.10'
)
