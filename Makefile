FIGCODES = $(wildcard book/code/*.py)
SVGS = $(patsubst book/code/%.py,book/figures/%.svg, $(FIGCODES))
NBS = $(wildcard book/**/*.ipynb)
MDS = $(wildcard book/*.md) $(wildcard book/*/*.md)

BASEDIR = $(CURDIR)

export MPLCONFIGDIR := $(CURDIR)/config/

help:
	@echo 'Makefile for the MUDE Jupyter Book'
	@echo ''
	@echo 'Usage:'
	@echo '   make figures          generate figures'
	@echo '   make book             generate the Jupyter Book'
	@echo '   make clean            remove generated files'
	@echo '   make test             test the Jupyter Book on errors'

all: $(SVGS) book/_build/html/index.html

figures: $(SVGS)

book: book/_build/html/index.html

book/figures/%.svg: book/code/%.py
	cd book/figures && python ../../$< 

book/_build/html/index.html: $(SVGS) $(NBS) $(MDS)
	jupyter book build book/

test: $(SVGS) $(NBS) $(MDS)
	jupyter book build -n -W --keep-going book/

clean:
	rm -f book/figures/*.svg
	jupyter book clean book/

.PHONY: figures all clean test