from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="copilot_pdf_exporter",
    version="1.0.0",
    description="Export all your Microsoft Copilot conversations to PDF using Playwright automation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jake Brewer",
    author_email="jake@example.com",
    url="https://github.com/Jake-Brewer/copilot-pdf-exporter",
    packages=find_packages(),
    install_requires=[
        "playwright",
    ],
    entry_points={
        "console_scripts": ["copilot-pdf-exporter = copilot_pdf_exporter.__main__:main"]
    },
    python_requires=">=3.8",
    include_package_data=True,
    license="MIT",
    keywords=["copilot", "pdf", "export", "playwright", "automation", "cli"],
    project_urls={
        "Documentation": "https://github.com/Jake-Brewer/copilot-pdf-exporter",
        "Source": "https://github.com/Jake-Brewer/copilot-pdf-exporter",
        "Tracker": "https://github.com/Jake-Brewer/copilot-pdf-exporter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Utilities",
    ],
)
