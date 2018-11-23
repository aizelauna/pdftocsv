from setuptools import setup

setup(name='pdftocsv',
      version='0.2',
      description='CLI tool to convert PDF table to CSV',
      url='http://github.com/aizelauna/pdftocsv',
      author='Aizelauna',
      author_email='aize.launa@gmail.com',
      license='MIT',
      packages=['pdftocsv'],
      install_requires=[],
      python_requires='>=3.5',
      entry_points={
        'console_scripts': [
            'pdftocsv = pdftocsv.cli:main',
        ],
      },
      zip_safe=False)
