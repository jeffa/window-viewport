from setuptools import setup, find_packages

setup(
    name='window-viewport',
    version=window-viewport.__version__,
    description='Just another window to viewport coordinates translator',
    author='Jeff Anderson',
    author_email='jeffa@cpan.org',
    url='https://github.com/jeffa/window-viewport',
    license='Artistic',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        "Topic :: Scientific/Engineering :: Visualization",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Artistic License",
    ],
    long_description="Translate real world coordinates into any viewport coordinates"
)
