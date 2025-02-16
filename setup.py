import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="speaker_verification_toolkit",
    version="0.0.2",
    author="Alohomora Team",
    author_email="alohomorafga@gmail.com",
    description="A package designed to compose speaker verification systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alohomora-team/speaker-verification-toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'python_speech_features==0.6',
        'fastdtw==0.3.2'
    ],
    python_requires='>=3.6',
)
