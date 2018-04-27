from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['nltk', 'PyYAML', 'metaphone']

setup(
    name='pronounceable',  # Required
    version='0.1.3',  # Required
    description='Analyze passwords\' memorizability and generate pronounceable words.',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/pronounceable',  # Optional
    author='Pacharapol Withayasakpunt',  # Optional
    author_email='patarapolw@gmail.com',  # Optional
    keywords='password password-analysis nltk word-synthesis',  # Optional
    packages=['pronounceable'],  # Required
    install_requires=install_requires,  # Optional
    python_requires='>=3.5',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security :: Cryptography'
    ],
    package_data={  # Optional
        'pronounceable': ['database/*'],
    },
    extras_require={
        'tests': ['pytest', 'pytest-doctestplus'],
        'analysis': ['memorable_password', 'randomsentence']
    }
)
