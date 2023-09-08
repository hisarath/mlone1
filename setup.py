from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="sarath",
      author_email="sarathkumaree@gmail.com",
      packages=find_packages(),
      insall_requires=["pandas","numpy","flask"]
      )