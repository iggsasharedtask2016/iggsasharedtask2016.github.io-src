Title: Task description
Date: 2016-03-13 20:12
Category: General
Tags: description
Slug: task description
Author: Josef Ruppenhofer
Summary: Description of the IGGSA 2016 Shared Task 
Lang: en

[TOC]

### Data
The data that we use comes from German-language speeches of the Swiss parliament (Bundesversammlung). It was chosen because

   * the source data is open to the public and allows for free distribution with the annotations
   * the text allows for annotation of multiple sources and targets
   * the text meets the research interests of several IGGSA-members, i.e. supports collaborations with political scientists and researches in digital humanities.

In selecting the data we took steps to minimize, or at least, mark any Swiss German idiosyncrasies. The selected speeches cover several different topics (foreign policy, book price controls, ...) so as to give better coverage of the variety of ways in which sources and targets might be expressed.

Training data will be release as per the schedule below.


### Annotations


Matching the general task we try to solve, the annotation scheme consists of three major types of labels:
Sources, Targets, and SubjectiveExpressions. These are inter-related by way of annotation frames that are centered on the Subjective Expressions. In addition, the three label types allow for several kinds of additional markings (flags), which indicate additional attributes of the labels.


![Annotation Example](http://iggsasharedtask2016.github.io/images/annoexample.png)

The annotations represent an adjudicated version of the 2014 test data. The guidelines will be linked here shortly.

Note that participating groups can use additional suitable training data as well as any kind of additional tools such as parsers etc. to develop their own systems.


### Subtasks and Evaluation

We offer three subtasks:

    * Full task Identification of subjective expressions with their respective sources and targets
    * Subtask a) Participants are given the subjective expressions and are only asked to identify opinion sources.
    * Subtask b) Participants are given the subjective expressions and are only asked to identify opinion targets.

### Formats

The STEPS data set has undergone the following pre-processing: sentence segmentation and tokenization using OpenNLP, lemmatization with the TreeTagger (Schmid, 1994), constituency parsing using the Berkeley parser (Petrov and Klein, 2007), and conversion of the parse trees into TigerXML-Format using TIGER-tools (Lezius, 2002). For the annotation we used the Salto-Tool (Burchardt et al. 2006). The existing Salsa API can be used for XML-files in this format.

For your convenience, *all* data from this Maintask has been preprocessed with tokenisation, part-of-speech tagging and syntactic analysis! But participants are of course free to do their own pre-processing.




### Schedule
<html>
<table cellpadding="5" cellspacing="5"  width="70%">
  <tr>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>March</td>
    <td></td>
    <td>Call for Participation</td>
  </tr>
  <tr>
    <td>Start of April</td>
    <td></td>
    <td>Release of training data</td>
  </tr>
  <tr>
    <td>July 29</td>
    <td></td>
    <td>Registration deadline</td>
  </tr>
<tr>
  <tr>
    <td>Start of August</td>
    <td></td>
    <td>Release of test data</td>
  </tr>
<tr>
    <td>Middle of August</td>
    <td></td>
    <td>System runs submitted</td>
  </tr>
<tr>
    <td>End of August</td>
    <td></td>
    <td>Notification of results</td>
  </tr>

<tr>
    <td>Middle of September</td>
    <td></td>
    <td>Drafts of workshop papers due</td>
  </tr>
<tr>
    <td>September 22</td>
    <td></td>
    <td>Workshop @ KONVENS 2016 in Bochum</td>
  </tr>

<tr>
    <td>End of October</td>
    <td></td>
    <td>Publication of final workshop papers</td>
  </tr>



</table>

### Acknowledgment

We are happy to acknowledge the finanical support that the GSCL (German Society for Computational Linguistics) has granted us 
for the annotation of the training data.