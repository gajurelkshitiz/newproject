from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # This function will return the lists of requirements.
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    description='A handful project',
    author='Kshitiz Gajurel',
    author_email='kshitiz.purbct042@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)