.DEFAULT_GOAL := topdf
OUTPUT_DIR = submission
OUTPUT_FILE = labs.pdf
FILES = README.md pandoc-metadata/frontmatter.yaml
FLAGS_PDF = --highlight-style tango
FLAGS = --pdf-engine=xelatex \
		--lua-filter=pandoc-metadata/scholarly-metadata.lua \
		--listings \
		-H pandoc-metadata/listing-setup.tex \
		--lua-filter=pandoc-metadata/format-authors.lua \
		-s \
		-f markdown

topdf:
	pandoc $(FILES) $(FLAGS) $(FLAGS_PDF) -o $(OUTPUT_DIR)/$(OUTPUT_FILE) && open $(OUTPUT_DIR)/$(OUTPUT_FILE)

clean:
	rm -rf submission/*
