import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name="profile_block",
        version="0.0.1",
        author="Sujay Mansingh",
        author_email="sujay.mansingh@gmail.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/sujaymansingh/profile_block",
        license="LICENSE.txt",
        description="Provide a context manager to cProfile code",
        long_description="View the github page (https://github.com/sujaymansingh/profile_block) for more details.",
        install_requires=[],
)
