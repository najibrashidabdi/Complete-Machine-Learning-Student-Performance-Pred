from setuptools import find_packages, setup 
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip whitespace and newline characters
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    print("Processed requirements:", requirements)  # Debugging
    return requirements



setup(
    name = 'machine learning project',
    version= '0.0.1',
    author = 'Najib',
    author_email = 'cabdinajiibrcabdirashiid@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')


)