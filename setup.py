from setuptools import setup

setup(
   name='enaBrowserTools',
   version='1.4.1',
   description='Seqeunce access to ENA',
   license="Apache",
   author='ENA',
   author_email='ena@ena.org',
   url="http://github.com/enasequence/enaBrowserTools",
   packages=['enaBrowserTools'],
   scripts=['bin/enaDataGet', 'bin/enaGroupGet']
)
