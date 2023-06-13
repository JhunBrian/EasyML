from setuptools import setup, find_packages

# jupyter nbconvert --to markdown YourNotebook.ipynb
 
# python setup.py sdist (for initial)

# python setup.py sdist bdist_wheel (for update)

# twine check dist/*
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Science/Research',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

desc = """SmplML is a comprehensive Python module designed for machine learning classification and regression tasks. It offers a range of features and tools that simplify the entire ML workflow, from data preprocessing to model training and evaluation. With SmplML, you can efficiently handle your datasets, experiment with various algorithms, and obtain predictions. Whether you're a beginner or an experienced practitioner, SmplML empowers you to harness the full potential of machine learning in a straightforward and efficient manner."""
 
dependencies = ['pandas', 
                'numpy', 
                'scikit-learn']

setup(
  name='SmplML',
  version='1.0.6',
  description=desc,
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/JhunBrian/SmplML',  
  author='Jhun Brian Andam',
  author_email='andam.jhunbrian@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['Machine Learning', 'Classification', 'Regression'], 
  packages=find_packages(),
  install_requires=dependencies
)
