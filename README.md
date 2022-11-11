# Jupyter Book project for weeks 2.7 and 2.8

This repository hosts the scripts to build the Jupyter Book for weeks 2.7 and 2.8. The class content will be developed in [this repository](https://gitlab.tudelft.nl/mude/uncertainty-2).

## Building the website

At the moment, this website is not hosted anywhere. We still need to figure out what is the best way to do this. For now, you can build and visit the website locally.

1. Clone the repository:
 
        git clone git@gitlab.tudelft.nl:mude/2_7-jupyter-book.git

2. Enter the repository:
   
        cd 2_7-jupyter-book

3. Install dependencies

        pip install -r requirements.txt

4. Build the book:

        jupyter book build book/

5. Open the website by opening `book/_build/index.html` in a webbrowser.