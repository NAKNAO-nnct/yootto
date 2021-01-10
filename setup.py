from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
setup(
    name="yootto",
    version="0.0.1",
    description="yootto(ヨーッと) is tiny YouTube Music unofficial uploader",
    author="yanoshi",
    packages=find_packages(),
    install_requires=install_requirements,
    python_requires='>3.6',
    entry_points={
        "console_scripts": [
            "yootto=yootto.core:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
