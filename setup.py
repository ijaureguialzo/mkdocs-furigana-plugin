from setuptools import setup

setup(
    name="mkdocs-furigana-plugin",
    version="0.0.1",
    description="An MkDocs plugin to add furigana to Japanese Kanji text.",
    long_description="",
    keywords="mkdocs furigana",
    url="https://github.com/ijaureguialzo/mkdocs-furigana-plugin",
    author="Ion Jaureguialzo Sarasola",
    author_email="ion@jaureguialzo.com",
    license="Apache 2.0",
    python_requires=">=3.9",
    install_requires=[
        "mkdocs>=1.4.1",
    ],
    entry_points={
        "mkdocs.plugins": [
            "furigana = mkdocs_furigana_plugin.plugin:FuriganaPlugin",
        ],
    },
)
