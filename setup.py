import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="plantNet",
	version="0.0.1",
	author="Jacob Harrison",
	author_email="jrhmtf@mst.edu",
	description="A Raspberry Pi networking tool for capturing images",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jacob-harrison/plantNet",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: Freely Distributable",
		"Operating System :: OS Independent",
	],
)
