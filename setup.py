from setuptools import setup, find_packages

setup(
    name='math_quiz', 
    version='1', 
    description='A simple math quiz game',  
    author='Chi Tai Bui',  
    author_email='buichitai2007@gmail.com',  
    url='https://github.com/buich/dsss_homework_2',  # Replace with your repository URL
    packages=find_packages(),  # Automatically find all packages in the project (i.e., math_quiz/)
    install_requires=[  # List any external dependencies here (empty for now if there are none)
        # 'numpy',  # Uncomment and add any dependencies as needed
    ],
    entry_points={  # Allows running the math_quiz game from the command line after installing
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # This assumes math_quiz.py has a `math_quiz()` function
        ],
    },
    classifiers=[  # Classifiers help users find your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
