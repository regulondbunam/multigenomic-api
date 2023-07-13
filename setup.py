import setuptools

setuptools.setup(
    name='multigenomic_api',
    version='1.1',
    description='API for RegulonDB Multigenomic DB',
    author='Pablo Pena',
    author_email='pablopl@ccg.unam.mx',
    license='MIT',
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'mongoengine',
    ]
)
