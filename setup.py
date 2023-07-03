import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Lucas A. Meyer',
    author_email='lucas@meyerperin.com',
    description='My toolbox package installation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lucas-a-meyer/lucas-toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/lucas-a-meyer/lucas-toolbox/issues"
    },
    license='None',
    packages=['toolbox'],
    install_requires=['requests'],
)