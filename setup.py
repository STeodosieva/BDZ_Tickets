from setuptools import setup, find_packages

setup(
    name="BDZ_Tickets",
    version="0.1",
    packages=find_packages(),
    install_requires=["flask"],
    author="Slavena Teodosieva",
    author_email="slavena.teodosieva@gmail.com",
    description="Brilliant Dashing Zestful system for buying tickets",
    license="MIT License",
    keywords="BDZ ticket online",
    url="https://github.com/STeodosieva/BDZ_Tickets",
    classifiers = ["Development Status :: 2 - Pre-Alpha",
                   "Environment :: Web Environment",
                   "Framework :: Flask",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: Microsoft :: Windows :: Windows 7",
                   "Programming Language :: Python :: 3.5",
                   "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
                   ],
    entry_points={
          'console_scripts': [
              'BDZ_tickets = BDZ_tickets.__main__:main'
          ]
      }
    )
