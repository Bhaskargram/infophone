from setuptools import setup, find_packages

setup(
    name="MobileNumberDetector",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "whois",
    ],
    author="Bhaskar",
    description="A tool for mobile number lookup and data extraction",
)
