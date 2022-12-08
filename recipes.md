# Markdown and Notebook recipes for the MUDE Jupyter Book

## Figures

To add a figure, just copy the figure to the correct directory. Then, in your markdown file, include the figure as follows:

    ```{figure} <figurename>.png/.jpg
    ---
    height/width: <height or width in pixels>
    name: <name of the figure>
    ---
    <Figure caption>
    ```

You can find more documentation on including figures [here](https://jupyterbook.org/en/stable/content/figures.html).

## Videos

MUDE videos are uploaded to the YouTube channel. To embed them in the Jupyter Book, first obtain the embedding link of the video. In order to do so, go to the *YouTube* page of the video (so not the Brightspace page), then click *share* in the description box. There should be a button *embed*, click that. Copy the HTML code that appears in the panel. Then, to embed the video, use the following 

    ```{eval-rst}
    .. raw:: html
    
    <paste the HTML code here>
    ```

## Equations

Equations can be included in two ways: inline or display mode. To make an inline equation, just put the LaTeX equation between \$-signs. For example, `$F = m \cdot a$` produces: $F = m \cdot a$. 

Display mode equations (the ones that take up a whole line), can be inserted using double \$-signs, like this:

    $$
        F = m \cdot a
    $$

which will produce:

$$
    F = m \cdot a
$$

To number the equations and refer in text, you need to provide a label to the equation. Just put the label between brackets and place it after the last \$\$, like this:

    $$
        F = m \cdot a
    $$ (newtons_second_law)

## References

To make references to figures, equations et cetera, use the following syntax:

- For figures, use: ``{numref}`<name of the figure>` ``
- For equations, use: ``{eq}`<equation label>` ``
- For citations, use: ``{cite:p}`<bibtex_entry>` `` for a citation between parenthesis, or ``{cite:t}`<bibtex_entry>` `` for an inline citation.

## Code

There are two ways main ways to include code: directly within a Markdown file or as a Jupyter notebook. More methods are available, but we don't include them here. The first option is great for including simple calculations, or generating simple figures when an image file is not practical. *More will be added later.*

Note that if you are using a `*ipynb` file or including a code snippet in a `*.md` file, including a blank line between the text and the closing three tick marks will generate an empty code box of one line in the Jupyter Book.

## Notebooks

When making notebooks for the Book, you might want to hide certain cells from the reader. For example, when including a simple figure generated from code or making a JupyterQuiz, we have to execute a code cell that generates the quiz. This code cell is ugly and distracting, so we do not want to render this in the final book. 

We can change how the compiler treats notebook cells by using cell tags. You can find a detailled explanation on cell tags [here](https://jupyterbook.org/en/stable/interactive/hiding.html?highlight=cell%20tag). Specifically, have a look at the sections on *hiding* cell inputs and *removing* cell inputs. 

The workflow of editing cell tags depends on your editor. If you're using Jupyter Lab, you can find instructions [here](https://jupyterbook.org/en/stable/content/metadata.html#jupyter-cell-tags). 

For example, the following tag is used to convert the code input into either a drop-down (`hide-input`) or make it invisible (replace `hide-input` with `remove-input`). Replace `input` with `output` to do the same with the cell output:
```
{
    "tags": [
        "remove-input"
    ]
}
```
Once a correctly typed tag is added to the notebook it will appear in the buttons at the top and can be added to other cells. Multiple tags can be added to the same cell, in which case the tags are separated by commas.