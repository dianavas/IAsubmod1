========================================
Parser
========================================


Tool-uri de downloadat
----------------------------------------

- `NLTK`_ - momentan este optional
- `TreeTagger`_ - momentan este optional
- biblioteca requests(trebuie rulat in cmd ca administrator):

    .. code-block:: bash

		pip install requests

`NLTK`_
----------------------------------------

- Deschideti un command line ca administrator

- Tastati comanda:

	.. code-block:: bash
	
		pip install nltk
		
- Dupa ce s-a downloadat deschideti python de la linia de comanda:
	
	Deschideti un command line(daca cel precedent l-ati inchis)
	Tastati comanda: 
	
	.. code-block:: bash
			
		python
	
	ca sa va deschida python la linia de comanda.

- In python tastati comanzile:
	.. code-block:: python
	
		import nltk
		nltk.download()
		
- Ultima comanda ar trebui sa va deschida o interfata:
	De pe interfata ar trebui ca din colectii sa selectati all si sa apasati download. O sa dureze ceva vreme.

- Dupa ce ati downloadat ar trebui sa arate ca in screenshot.

	
`TreeTagger`_
----------------------------------------

- Rulati comanda:
	
	.. code-block:: bash
	
		pip install treetaggerwrapper
		
	intr-un comandline ca administrator.
- Copiati directorul Lbis\TreeTagger in disk-ul c.
- Adaugati o noua variabila de sistem. Numele variabilei va fi "TAGDIR" iar valoarea va fi "C:\TreeTagger"
- Trebuie modificat scriptul "treetaggerwrapper.py", scriptul ar trebui sa fie localizat in directorul : "c:\Program Files\Python37\Lib\site-packages\"
- Cautati dictionarul "g_langsupport" in acest script.
- Trebuie sa adaugati cheia si valoarea urmatoare la acest dictionar:

.. code-block:: python
			
	"ro": {
		"encoding": "utf-8",
		"tagparfile": "romanian-utf8.par",
		"abbrevfile": "romanian-abbreviations",
		"pchar": ALONEMARKS + "'",
		"fchar": ALONEMARKS + "'",
		"pclictic": "",
		"fclictic": "",
		"number": NUMBER_EXPRESSION,
		"dummysentence": "Ana are mere. Câte mere are"
							 "Ana?",
		"replurlexp": 'sustituir-url>',
		"replemailexp": 'sustituir-email',
		"replipexp": 'sustituir-ip',
		"repldnsexp": 'sustituir-dns'
	}

Status implementare curenta
--------------------------

- Tokenizer - `NLTK`_
- Post Tagger - `TreeTagger`_
- Lematizer - `TreeTagger`_
- NP Chuncker - none
- Dependency parser - none
- Multilingual Anaphora Resolution - none
- RoWordNet - none


.. _NLTK: http://nltk.org/
.. _TreeTagger: http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/