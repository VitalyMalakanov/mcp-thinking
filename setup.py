from setuptools import setup, find_packages

setup(
    name="enhanced-sequential-thinking-server",
    version="0.1.0",
    description="Advanced server for structured LLM thinking (MCP)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="[Your Name]",
    license="MIT",
    py_modules=["enhanced_sequential_thinking_server"],
    packages=find_packages(),
    install_requires=[
        "mcp[cli,http]",
        "colorama",
        "numpy",
        "scikit-learn",
        "textstat",
        "fastapi",
        "uvicorn"
    ],
    extras_require={
        "dev": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "enhanced-sequential-thinking-server=enhanced_sequential_thinking_server:main"
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
) 