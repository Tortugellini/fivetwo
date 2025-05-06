## Background
This repository is inspired by a card game that I play.
As I became more and more familiar with the game, I found myself wondering about all the different methods there are to shuffle a deck and which one randomizes the deck the most, and possibly, how much of an effect these have on the game itself.<br>
So I decided to model them in the hopes of:
1. Improving my understanding of the math behind the game I enjoy playing
2. Improving my methods as a Python developer
3. Just having fun coding. :grin:
## Meet the Objects
Below are short descriptions for each piece of this module.
### Deck
The Deck is the object that holds information about, well, the deck of cards we are shuffling.
It is currently designed to generate a numbered list (non-Pythonically indexed) but will most likely be changed to a dictionary that holds information about each card.
In its current form, it is good for visualizing an "ordered" deck.
### Shuffler
The Shuffler is the object responsible for holding the methods that shuffle the deck. <br>
The current shuffling methods modeled are:
1. Mash Shuffle<br>
Splits the deck into two not-necessarily-even piles and recombines the piles by interleaving the cards together.
2. Pile Shuffle<br>
The deck is separated into N piles and then restacked in a random order.
<br>*Currently only supports a number of stacks that results in evenly sized stacks.*

With each shuffle, the Shuffler automatically updates an attribute of the deck that indicates which method was used to shuffle the deck. More methods will appear in time.
### Statistics
What should probably have been called TheStatistician, Statistics is the object that, currently, calculates the entropy of the Deck after each shuffle.
Currently, this object is based on a Frequentist approach but may be changed to a Bayesian approach in the future. 
## Contribution
While this is a small pet project, I welcome contribution:
~~~
git clone (whatever method you prefer)
~~~
~~~
cd fivetwo
~~~
~~~
pip install .
~~~
