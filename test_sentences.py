from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
def test_get_noun():
    #Test the single noun

    single_noun =  ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    #Verify that the word returned from get noun 
    # is one of the words in the single get_noun list
    for i in range(10):
      word = get_noun(1)
      assert word  in single_noun


  # Test plural noun 

    plural_noun = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for i in range(10):
        word = get_noun(2)

        assert word in plural_noun
def test_get_verb():
    # Test past tense

    past_tense =  ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for i in range(10):
        word = get_verb(1, "past")

        assert word in past_tense

    # Test present tense 

    present_tense = [ "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    for i in range(10):
        
        word = get_verb(1, "present")

        assert word in present_tense

 # Test tense is presentbut quantity is not 1
    present_not_one = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    for i in range(10):
        word = get_verb(2, "present")

        assert word in present_not_one

# Test future tense 
    future_tense = ["will drink", "will eat", "will grow", "will laugh","will think", "will run",
                     "will sleep", "will talk",
                    "will walk", "will write"]
    for i in range(10):
        word = get_verb(1, "future")

        assert word in future_tense


# Test preposition
def test_get_preposition():
    prepositions = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for i in range(21):
        word = get_preposition()

        assert word in prepositions

def test_get_prepositional_phrase():
    #Test functions for single prepositional phrase

    preposition = get_preposition() # Get the prepositional word
    deter = get_determiner(1) # Get the determiner word
    now = get_noun(1)   #Get the noun 
    preposition_phrase = preposition + deter + now   #Get the prepositional phrase from the random word numbers

    strings = preposition_phrase 

    assert strings in preposition_phrase  # Check if the strings is  coresspond with the prepositional phrase
     

    #Test functions for plural prepositional phrase

    preposition = get_preposition() # Get the prepositional word
    deter = get_determiner(2) # Get the plural determiner word
    now = get_noun(2)   #Get the noun 
    preposition_phrase = preposition + deter + now   #Get the prepositional phrase from the random word numbers

    strings = preposition_phrase 

    assert strings in preposition_phrase  # Check if the strings is  coresspond with the prepositional phrase
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
