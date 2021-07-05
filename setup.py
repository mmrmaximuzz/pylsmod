import setuptools

setuptools.setup(
    name="pylsmod",
    version="0.1.0",
    author="Maxim Petrov",
    author_email="mmrmaximuzz@gmail.com",
    description="Draw your kernel module deps",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
)
