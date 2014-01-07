import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name='commonledger-sdk',
	version='0.0.1',
	description='Official CommonLedger API library client for python',
	author='Common Ledger',
	author_email='api@commonledger.com',
	url='https://commonledger.com',
	license='MIT',
	install_requires=[
		'requests >= 2.1.0'
	],
	packages=[
		'common_ledger'
	],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Topic :: Software Development :: Libraries :: Python Modules',
	]
)
