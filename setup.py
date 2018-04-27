from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['nltk', 'PyYAML', 'metaphone']

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
    packages=find_packages(exclude=['tests', 'dev', 'analysis']),  # Required
    install_requires=install_requires,  # Optional
    python_requires='>=3.5',
    dependency_links=['git+https://github.com/patarapolw/memorable-password.git#egg=memorable-password',
                      'git+https://github.com/patarapolw/randomsentence.git#egg=randomsentence'],
    package_data={  # Optional
        'pronounceable': ['database/*'],
    },
)
