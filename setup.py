from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name='labelord_IgorRosocha',
    version='0.5.1',
    description='Management of GitHub labels.',
    long_description=long_description,
    author='Igor Rosocha',
    author_email='rosocigo@fit.cvut.cz',
    keywords='github,labels,management,flask,web,cli',
    license='MIT',
    url='https://github.com/IgorRosocha/labelord_IgorRosocha',
    packages=find_packages(),
    package_data = {'labelord': ['templates/*.html']},
    python_requires='~=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Framework :: Flask',
        'Environment :: Console',
        'Environment :: Web Environment'
    ],
    install_requires=['Flask', 'click>=6', 'requests', 'sphinx_click', 'sphinx_rtd_theme'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
         'labelord = labelord.labelord:main',
        ],
    },
)
