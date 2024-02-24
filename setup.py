from setuptools import find_packages, setup
from typing import List

Hypen_e_dot= "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function help us to read the requirement file and return a list
    '''
    require=[]
    with open(file_path) as file_obj:
        require=file_obj.readlines()
        require=[i.replace("\n","") for i in require]

        if Hypen_e_dot in require:
            require.remove(Hypen_e_dot)
    return require


setup(
name='mlProjectbykris',
version='0.0.1',
author='Biswa',
author_email='biswanathprasad2017@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)