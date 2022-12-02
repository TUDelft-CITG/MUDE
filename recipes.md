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

## Notebooks

When making notebooks for the Book, you might want to hide certain cells from the reader. For example, when making a JupyterQuiz, we have to execute a code cell that generates the quiz. This code cell is ugly and distracting, so we do not want to render this in the final book. 

We can change how the compiler treats notebook cells by using cell tags. You can find a detailled explanation on cell tags [here](https://jupyterbook.org/en/stable/interactive/hiding.html?highlight=cell%20tag). Specifically, have a look at the sections on *hiding* cell inputs and *removing* cell inputs. 

The workflow of editing cell tags depends on your editor. If you're using Jupyter Lab, you can find instructions [here](https://jupyterbook.org/en/stable/content/metadata.html#jupyter-cell-tags). 