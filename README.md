# Jupyter Book project for weeks 2.7 and 2.8

This repository hosts the source code of the Jupyter Book that is used in weeks 2.7 and 2.8 of the course Modelling, Uncertainty and Data for Engineers (CEGM1000). The website is currently hosted via GitHub pages at [tudelft-citg.github.io/MUDE](https://tudelft-citg.github.io/MUDE).

## Contributing to the website

To contribute, first clone the repository using your favorite `git` tool. For all the ins and outs of working with Jupyter Book and associated files, we refer to the [Jupyter Book website](https://jupyterbook.org/en/stable/intro.html).

When adding new content to the website, or making large changes, *please create a new branch and make a pull request once finished*.

Inside the repository, the contents of the book can be found in `book/`. Inside this directory, every chapter of the book has its own sub-directory, which contains all of the files associated with that chapter. Think of markdown, Jupyter notebooks or JSON files for Jupyter Quiz. When you've added your content, make sure to add the filenames to the `book/_toc.yml` file.

## Building the website locally

For testing your changes/additions to the website, it is recommended to build the website on your local machine. This is for three main reasons: 1) it is faster than waiting for the CI/CD pipeline to complete, 2) the amount of CI/CD minutes are limited, 3) no broken/incomplete pages will be presented to the students. In order to build the website locally, follow these steps:

1. Change into the root directory of the repository.
   
2. Install dependencies:

        pip install -r requirements.txt

3. Build the book:
   
        jupyter book build book/

4. Visit the website by opening `book/_build/html/index.html` in a web browser.

5. When you have made changes to the website, recompile with:

        jupyter book clean book/ && jupyter book build book/

## Useful websites

- [Main Jupyter Book website](https://jupyterbook.org/en/stable/intro.html) and the [git repository of the website](https://github.com/executablebooks/jupyter-book/tree/master/docs), which is also built with Jupyter Book
- [The Turing Way](https://the-turing-way.netlify.app/welcome) and the [git repository](https://github.com/alan-turing-institute/the-turing-way).