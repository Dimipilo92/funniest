from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
	
def readme():
	with open('README.rst') as f:
		return r.read()

setup(
	name='funniest',
	verstion='0.1',
	description='The funniest joke in the world',
	long_description='Really, the funniest around.', # extra
	classifiers=[ # extra
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
	  keywords='funniest joke comedy flying circus', # extra
	url='http://github.com/storborg/funniest',
	author='Flying Circus',
	author_email='flyingcircus@example.com',
	licence='MIT',
	packages=['funniest'],
	zip_safe=False,
	install_requires=requirements,
	# dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']  # for projects not on pypi
	test_suite='nose.collector', # testing
	tests_require=['nose', 'nose-cover3'], # testing
	scripts=['bin/funniest-joke'], # script will get copied into PATH
	entry_points = {
		'console_scripts': ['funniest-joke=funniest.command_line:main'],
	},
	include_package_data=True  # used to include all non-doc files listed in MANIFEST
)