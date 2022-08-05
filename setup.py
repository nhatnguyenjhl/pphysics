import setuptools

with open('./README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pphysics',
    version='1.1.0',
    author='James H. Lasker',
    author_email='jameshlasker@gmail.com',
    description='Package pphysics to use physics in pygame.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nhatnguyenjhl/pyphysics',
    project_usls={
        'Source': 'https://github.com/nhatnguyenjhl/pyphysics/tree/main/pyphysics',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.8'
)
