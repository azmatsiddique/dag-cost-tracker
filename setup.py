from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="dag-cost-tracker",
    version="0.1.2",
    description="A DAG cost tracking plugin for Apache Airflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azmatsiddique/dag-cost-tracker",
    project_urls={
        "Bug Tracker": "https://github.com/azmatsiddique/dag-cost-tracker/issues",
        "Source Code": "https://github.com/azmatsiddique/dag-cost-tracker",
    },
    author="Azmat Siddique",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "apache-airflow>=2.0.0",
        "SQLAlchemy>=1.3.0,<2.0.0",
        "PyYAML>=5.1",
        "click>=7.0",
        "tabulate>=0.8.0",
    ],
    entry_points={
        "console_scripts": [
            "dag-cost=dag_cost_tracker.cli:cli",
        ],
        "airflow.plugins": [
            "dag_cost_tracker=dag_cost_tracker.plugin:DagCostTrackerPlugin",
        ],
    },
)
