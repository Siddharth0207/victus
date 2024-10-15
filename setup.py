from setuptools import find_packages ,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    """
    Read the requirements file and return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

setup(
    name = "data-science project",
    version= "0.0.1" ,
    author= "siddharth_gauttam",
    author_email="siddharthkushwaha33@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)