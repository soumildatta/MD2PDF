from setuptools import setup

setup(
    name="MD2PDF",
    version="0.1.0",
    py_modules=["md2pdf"],
    install_requires=[
        "Markdown>=3.4.4",
        "pdfkit>=1.0.0",
    ],
    entry_points={
        'console_scripts': [
            'md2pdf = md2pdf:main',
        ],
    },
)
