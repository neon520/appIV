from setuptools import setup

setup(name='appIV',
      version='0.1',
      description='App web to rank enterprises',
      url='https://github.com/neon520/appIV',
      author='neon_520',
      author_email='javierpg93@correo.ugr.es',
      license='MIT',
      packages=['appIV'],
      install_requires=[
          'mysql-python',
          'jinja2',
          'webapp2',
          'Paste',
          'webob'
      ],
      zip_safe=False)

