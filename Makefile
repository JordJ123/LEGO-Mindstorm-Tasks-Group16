.DEFAULT_GOAL := topdf

OUTPUT_DIR = submission
OUTPUT_FILE = labs
FILES = README.md pandoc-metadata/frontmatter.yaml
FLAGS = --lua-filter=pandoc-metadata/scholarly-metadata.lua \
		--lua-filter=pandoc-metadata/format-authors.lua \
		-s \
		-f markdown
FLAGS_PDF = 

topdf:
	pandoc $(FILES) $(FLAGS) $(FLAGS_PDF) -o $(OUTPUT_DIR)/$(OUTPUT_FILE).pdf 

clean:
	rm -rf submission/*
