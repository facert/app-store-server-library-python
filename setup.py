# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="app-store-server-library",
    version="0.2.1",
    description="The App Store Server Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7, <4",
    install_requires=["attrs", 'PyJWT', 'requests', 'cryptography', 'pyOpenSSL', 'asn1', 'cattrs'],
    package_data={"appstoreserverlibrary": ["py.typed"]},
)
