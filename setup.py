# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='scrapper',
    version="1.61",
    packages=find_packages(),
    author="xell",
    author_email="not mention",
    install_requires=["termcolor","beautifulsoup4","requests","httpx","trio","tqdm","colorama"],
    description="holehe allows you to check if the mail is used on different sites like twitter, instagram , snapchat and will retrieve information on sites with the forgotten password function.",
    include_package_data=True,
    url='http://github.com/JENSLINJEMZ/mail_scrapper',
    entry_points = {'console_scripts': ['mailscrapper = holehe.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
