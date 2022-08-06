import setuptools

with open('./README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pphysics',
    version='1.1.1',
    author='James H. Lasker',
    author_email='jameshlasker@gmail.com',
    maintainer='James H. Lasker',
    maintainer_email='jameshlasker@gmail.com',
    license='MIT License',
    license_file='LICENSE',
    description='Package pphysics to use physics in pygame.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    home_page='https://nhatnguyenjhl.github.io',
    project_usls={
        'Source': 'https://github.com/nhatnguyenjhl/pphysics/tree/main/pphysics',
        'Documentation': 'https://nhatnguyenjhl.github.io/pphysics'
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    requires_dist='setuptools',
    keywords=[
        'physics',
        'pyphysics',
        'pyame',
        'jameshlasker',
        'standard',
        'federation',
    ],
    zip_safe=False,
    install_requires=[
        'pygame>=3.8',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.8'
)
