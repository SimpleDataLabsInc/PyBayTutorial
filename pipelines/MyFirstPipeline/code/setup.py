from setuptools import setup, find_packages
setup(
    name = 'MyFirstPipeline',
    version = '1.0',
    packages = find_packages(include = ('myfirstpipeline*', )),
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.4'],
    entry_points = {
'console_scripts' : [
'main = myfirstpipeline.pipeline:main', ], },
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
