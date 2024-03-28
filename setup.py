from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Daffa Arifadilah',
    author_email='dafa.130.df@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "pyPDF", "python-dotenv"], 
    packages=find_packages()
)