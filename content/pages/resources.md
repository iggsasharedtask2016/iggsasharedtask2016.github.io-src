Title: Tools
Date: 2016-03-12 17:32
Category: General
Tags: Tools
Slug: tools
Author: Josef Ruppenhofer
Summary: Potentially Useful Resources and Tools 
Lang: en

If you are interested in our shared task, we would like to help you get started. 

Here we provide a collection of resources and tools that you might find useful. We would be very grateful for any suggestions that you might have.


## STEPS Evaluation Tool 

The version for the 2016 iteration of the shared task will be made available soon.

## Opinion Role Extraction Systems

[Saarland University's lexicon-based system](https://github.com/miwieg/german-opinion-role-extractor)

## Corpora and Lexicons

### German resources

[SentiWS](http://asv.informatik.uni-leipzig.de/download/sentiws.html) - a Publicly Available German-language Resource for Sentiment Analysis

[GermanPolarityClues](http://www.ulliwaltinger.de/sentiment/) - A Lexical Resource for German Sentiment Analysis

[SALSA Corpus](http://www.coli.uni-saarland.de/projects/salsa/corpus/) - German corpus with semantic roles labeled in the FrameNet style

[GermaNet](www.sfs.uni-tuebingen.de/GermaNet/) - a WordNet-style resource for German

### English resources

There are also some English resources that you might use if you are interested in doing something using translation:

[MPQA corpus](http://mpqa.cs.pitt.edu/corpora/mpqa_corpus/)- a standard corpus for sentiment analysis for English

[Subjectivity Lexicon](http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/) - a widely used sentiment lexicon for English

## Tools

[Salto annotation tool, Salsa API](http://www.coli.uni-saarland.de/projects/salsa/page.php?id=software) - this tool was used to annotate the data

[Berkeley Parser](https://github.com/slavpetrov/berkeleyparser) - constituency parser with models for German

[ParZu](https://github.com/rsennrich/ParZu) - a dependency parser for German ([demo](http://kitt.ifi.uzh.ch/kitt/parzu/) available) -- note that a morphology is not necessary to run the tool; recommend to run the tool on pre-tagged text (use TreeTagger output)

[Stanford Parser](http://nlp.stanford.edu/software/lex-parser.shtml) - another well-known constituency parser with models for German

[sempar](de.sempar.ims.uni-stuttgart.de) - semantic role labeling software for German

[Shalmaneser](http://www.coli.uni-saarland.de/projects/salsa/shal/) - the first semantic role labeler for German based on a FrameNet representation; the Semafor role labeler has no model for German; Shalmaneser also works on English)


[Shalmaneser - open source](https://github.com/arbox/shalmaneser) - an attempt to keep the original Shalmaneser and its components up to date as the original creators are not currently maintaining it

[convert_treebank](http://search.cpan.org/~tiedemann/Lingua-Align-0.04/bin/convert_treebank) (Lingua-Align-0.04) -- note that you run the tool on command line with convert_treebank [-i] infile informat outformat > outfile

[TIGER Corpus](http://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/tiger.en.html) - this website contains information on TIGERxml and a conversion tool to dependency structures

[TIGERSearch and TIGERRegistry](http://www.ims.uni-stuttgart.de/forschung/ressourcen/werkzeuge/tigersearch.html) -  home page of tools for indexing and viewing corpora based on TIGER-xml  

[TreeTagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) -  part-of-speech tagger that also does lemmatization; suitable for German

[RFTagger](http://www.cis.uni-muenchen.de/~schmid/tools/RFTagger/)  - another POS-tagger for German

[Morphisto](https://code.google.com/archive/p/morphisto/) - morphological analysis tool for German

[SemiNER](http://grzegorz.chrupala.me/seminer.html) - Named-entity recognizer for German

[Named-entity recognizer for German](http://www.nlpado.de/~sebastian/software/ner_german.shtml) by Faruqui and Padó

[Giza++](http://www.statmt.org/moses/giza/GIZA++.html) - you will also find tutorials on the web that describe common applications such as word alignment using that tool

[CRF++](https://taku910.github.io/crfpp/) - an open source implementation of Conditional Random Fields (CRFs) for sequence labeling

[UIMA](http://uima.apache.org/) - Apache system for Unstructured Information Management applications

[DKPro](https://www.ukp.tu-darmstadt.de/research/current-projects/dkpro/) (Darmstadt Knowledge Processing Repository)

### Acknowledgments

The initial lists on the page were contributed by Michael Wiegand.
