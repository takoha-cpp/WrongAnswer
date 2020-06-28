import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wrong-answer",
    version="0.0.7",
    author="Takoha",
    author_email="author@example.com",
    description="Download AtCoder Testcases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takoha-cpp/WrongAnswer",
    packages=setuptools.find_packages(exclude=['docs']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.6',
    keywords = 'downloader competitive-programming AtCoder test-cases',
    project_urls = {
        'Documentation': 'https://takoha-cpp.github.io/WrongAnswer',
        'Source': 'https://github.com/takoha-cpp/WrongAnswer',
    },
    install_requires = [
        'online-judge-tools >= 10.0.3'
    ],
    entry_points = {
        'console_scripts': [
            'wa = wrong_answer.main:main',
        ],
    },
)

