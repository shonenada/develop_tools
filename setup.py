from setuptools import setup, find_packages


metadata = {"name": "develop_tools",
            "version": "0.1",
            "author": "shonenada",
            "author_email": "shonenada@gmail.com",
            "url": "https://github.com/shonenada/develop_tools/",
            "platforms": "any",
            "packages": find_packages(),
            "scripts": ["tools.py"],
            "description": "A tools set to help develop."}


if __name__ == "__main__":
    setup(**metadata)
