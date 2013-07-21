from distutils.core import setup

setup(name='magpie',
      version='0.0.1',
      description='Magpie Hardware Library',
      author='Steve kelly',
      author_email='kd2cca@gmail.com',
      url='http://www.github.com/textcad/pyMagpie',
      packages=['magpie'],
      package_data={'magpie': ['dimensions/Hardware-Dimensions/json/*.json']},
     )
