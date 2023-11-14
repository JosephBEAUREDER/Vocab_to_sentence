# Vocab_to_sentence #language_learning

Here is a website I created for the course "Langage Learning and NLP" of my master program.

I used the Django framework (python) for the back-end and javascript/css/bootstrap for the front-end.


The idea of the project is that a user can enter a list of words he/she wants to remember.

And, after pressing a button, the back-end selects one or multiple words from this list, a create an original sentence in the target language with this/these words. The sentence is generated using the API from OpenAI.

- The created sentence is first invisible, the user is only able to hear it in the target language (using the API of GoogleTTS).

- Two other buttons are also available, the first to see the sentence written in the target langage (using the API of GoogleTranslate).

- The second to see the translation in english.
