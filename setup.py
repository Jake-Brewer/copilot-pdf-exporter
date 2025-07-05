from setuptools import setup, find_packages

setup(
    name="copilot_pdf_exporter",
    version="1.0.0",
    description="Export all your Microsoft Copilot conversations to PDF using Playwright automation.",
    author="Jake Brewer",
    packages=find_packages(),
    install_requires=[
        "playwright",
    ],
    entry_points={
        "console_scripts": ["copilot-pdf-exporter = copilot_pdf_exporter.__main__:main"]
    },
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
