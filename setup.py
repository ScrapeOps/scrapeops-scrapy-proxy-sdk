from setuptools import setup, find_packages


DESCRIPTION = 'Scrapeops Scrapy Proxy SDK, simple integration of the scrapeops proxy with your scrapy spiders.'

setup(name="scrapeops_scrapy_proxy_sdk",
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      author="ScrapeOps",
      author_email="info@scrapeops.io",
      version="0.22",
      license="BSD",
      url="https://github.com/ScrapeOps/scrapeops-scrapy-proxy-sdk",
      packages=find_packages(),
      install_requires=[
          "requests>=2.24.0",
          "scrapy>=2.0",
          "urllib3>=1.25.10",
          ],
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
      ],
      python_requires=">=3.6",
      )