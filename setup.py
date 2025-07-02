from setuptools import setup, find_packages

setup(
    name="task_manager",
    version="0.1.0",
    description="A simple task manager application.",
    author="sumanengg.sg@gmail.com",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'task-manager=task_manager.cli:main',
        ],
    },
    include_package_data=True,
    extras_require={
    "dev": ["pytest"]
}
)