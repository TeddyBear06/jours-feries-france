from setuptools import setup

setup(
    name='jours_feries_france',
    license='MIT',
    packages=['jours_feries_france'],
    version='0.2.0',
    description='Get bank holidays for France',
    author='Antoine Augusti',
    author_email='hi@antoine-augusti.fr',
    url='https://github.com/AntoineAugusti/jours_feries_france',
    keywords=['bank-holidays', 'jours-feries', 'france'],
    extras_require={'dev': ['nose']},
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
