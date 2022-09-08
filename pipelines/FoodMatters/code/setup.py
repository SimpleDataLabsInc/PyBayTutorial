from setuptools import setup, find_packages
setup(
    name = 'FoodMatters',
    version = '1.0',
    packages = find_packages(include = ('foodmatters*', )),
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.4'],
    entry_points = {
'console_scripts' : [
'main = foodmatters.pipeline:main', ], },
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
