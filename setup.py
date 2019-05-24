from setuptools import setup, find_packages

install_requires = [
    # "gurobipy",  	# install this manually
    # "alib",      	# install this manually
    # "vnep_approx" , 	# install this manually 
    "matplotlib>=2.2,<2.3",
    "numpy",
    "click==6.7",
    "pyyaml",
    "jsonpickle",
]

setup(
    name="evaluation-ieee-acm-ton-2019",
    # version="0.1",
    packages=["evaluation_ieee_acm_ton_2019"],
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "evaluation-ieee-acm-ton-2019 = evaluation_ieee_acm_ton_2019.cli:cli",
        ]
    }
)
