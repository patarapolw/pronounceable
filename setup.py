from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['nltk', 'PyYAML', 'metaphone']
# pytest_requires = ['xdist', 'repeat', 'timeout', 'doctestplus']
# tests_require = ['pytest'] + ['pytest-{}'.format(req) for req in pytest_requires]

setup(
    name='pronounceable',  # Required
    version='0.1.0',  # Required
    description='Analyze passwords\' memorizability and generate pronounceable words.',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/pronounceable',  # Optional
    author='Pacharapol Withayasakpunt',  # Optional
    author_email='patarapolw@gmail.com',  # Optional
    keywords='password password-analysis nltk word-synthesis',  # Optional
    packages=find_packages(exclude=['tests', 'dev']),  # Required
    install_requires=install_requires,  # Optional
    python_requires='>=3',
    # tests_require=pytest_requires,
    # extras_require={  # Optional
    #     'test': ['tox'] + pytest_requires,
    # },
    package_data={  # Optional
        'pronounceable': ['database/*'],
    },
)
