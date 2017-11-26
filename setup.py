from setuptools import setup


extra = {}
f = open('README.rst', 'r')
try:
    extra['long_description'] = f.read()
finally:
    f.close()


deps = []
try:
    import argparse
except ImportError:
    deps.append('argparse')


setup(
    name='csscompressor',
    version='0.9.5',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities'
    ],
    packages=['csscompressor', 'csscompressor.tests'],
    install_requires=deps,
    **extra
)
