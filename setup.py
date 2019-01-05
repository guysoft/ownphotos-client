from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='ownphotos_client',
      version='0.1',
      description='Ownphotos client',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='ownphotos',
      url='http://github.com/guysoft/ownphotos-client',
      author='Guy Sheffer',
      author_email='guysoft@gmail.com',
      license='GPLv3',
      packages=['ownphotos_client'],
      test_suite="",
      tests_require=[],
      entry_points={
          'console_scripts': [],
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'requests>=2.21.0',
        ])
      
