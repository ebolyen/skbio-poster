all:
	cd assets/py && python sniff.py > ../sniff.out
	cd assets/py && python pairwise_similarity.py > ../pairwise.out
	cd assets/py && python pcoa.py
	$(MAKE) poster

poster:
	pdflatex --shell-escape poster.tex
