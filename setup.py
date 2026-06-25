from setuptools import setup, find_packages


DESCRIPTION = 'Scrapeops Scrapy Proxy SDK, simple integration to use the Scrapeops Proxy API with your Scrapy Spiders.'

setup(name="scrapeops_scrapy_proxy_sdk",
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      author="ScrapeOps",
      author_email="info@scrapeops.io",
      version="1.1",
      license="BSD",
      url="https://github.com/ScrapeOps/scrapeops-scrapy-proxy-sdk",
      packages=find_packages(),
      install_requires=[
          "scrapy>=2.0",
      ],
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
      ],
      python_requires=">=3.8",
      )