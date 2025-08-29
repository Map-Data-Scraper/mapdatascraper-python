from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='mapdatascraper',
    version='5.9.2',
    description='Python bindings for the MapDataScraper API',
    long_description=readme(),
    classifiers = ['Programming Language :: Python',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Topic :: Utilities',
    ],
    keywords='mapdatascraper webscraper extractor google api maps search json scrape parser reviews google play amazon',
    url='https://github.com/mapdatascraper/mapdatascraper-python',
    author='MapDataScraper',
    author_email='support@mapdatascraper.com',
    license='MIT',
    packages=['mapdatascraper'],
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
    long_description_content_type='text/x-rst',
)