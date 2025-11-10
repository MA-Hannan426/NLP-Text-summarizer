import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"


REPO_NAME = "NLP-Text-summarizer"
AUTHOR_USER_NAME = "MA-Hannan426"
AUTHOR_EMAIL = "ma.hannan230@gmail.com"
SRC_REPO = "text summarizer"
DESCRIPTION = "A text summarization project using NLP techniques and Deep-Learning Transformers Technology."


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
