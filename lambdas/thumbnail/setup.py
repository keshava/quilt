from setuptools import setup

setup(
    name='t4_lambda_thumbnail',
    version='0.0.1',
    py_modules=['index'],
    packages=['tifffile', 'aicsimageio', 'aicsimageio.readers', 'aicsimageio.writers', 'aicsimageio.vendor']
)
