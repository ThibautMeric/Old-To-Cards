from setuptools import setup, find_packages
import Old_To_Cards
setup(name = 'Old-To-Cards',
      version = Old_To_Cards.__version__,
      packages = find_packages(),
      entry_points = {'gui_scripts': ['Old-To-Cards = Old_To_Cards.old_to_cards:main',]},
      description='Update your CSS from Bootstrap 3 to Bootstrap 4',
      long_description='Update Panel,Thumbnails and Well definition to Cards with Old-To-Cards.',
      author='Thibaut Meric',
      author_email='thibaut.meric@microchip.com',
      url='www.microchip.com/iot/',
      maintainer= 'Iot & HASG Group',
      maintainer_email='xxxxxx@microchip.com',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers'
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                  ],
      platforms=['Operating System :: MacOS :: MacOS X','Operating System :: Microsoft :: Windows'],
      keywords='CSS HTML',
     )
# documentation -> https://packaging.python.org/en/latest/distributing/#setup-args
# classifiers list -> https://pypi.python.org/pypi?%3Aaction=list_classifiers
# Wheel name documentation -> https://www.python.org/dev/peps/pep-0427/
