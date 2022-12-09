FIGCODES = $(wildcard book/code/*.py)
SVGS = $(patsubst book/code/%.py,book/figures/%.svg, $(FIGCODES))
NBS = $(wildcard book/**/*.ipynb)
MDS = $(wildcard book/*.md) $(wildcard book/*/*.md)

.PHONY: figures all clean

all: $(SVGS) book/_build/html/index.html
figures: $(SVGS)
book: book/_build/html/index.html

book/figures/%.svg: book/code/%.py
	cd book/figures && python ../../$< 

book/_build/html/index.html: $(SVGS) $(NBS) $(MDS)
	jupyter book build book/

clean:
	rm -f book/figures/*.svg
	jupyter book clean book/