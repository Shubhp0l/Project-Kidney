import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_desc = f.read()

__version__ = "0.0.0"

REPO_NAME = "Project-Kidney"
AUTHOR_USER_NAME = "debabratabhagat"
SRC_REPO = "projectKidney"
AUTHOR_EMAIL = "aplha@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="package for cnn app",
    long_description=long_desc,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
