from setuptools import setup


extra = {}
f = open('README.rst', 'r')
try:
    extra['long_description'] = f.read()
finally:
    f.close()


setup(
    name='csscompressor',
    version='0.9.0',
    url='http://github.com/sprymix/csscompressor',
    license='BSD',
    author='Yury Selivanov',
    author_email='info@sprymix.com',
    description='A python port of YUI CSS Compressor',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Text Processing :: General'
    ],
    packages=['csscompressor', 'csscompressor.tests'],
    **extra
)
