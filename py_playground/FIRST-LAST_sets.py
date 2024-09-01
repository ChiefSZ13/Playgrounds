# Defining a passage from "Hamlet" by Shakespeare.
hamlet = '''HORATIO.
What art thou that usurp’st this time of night,
Together with that fair and warlike form
In which the majesty of buried Denmark
Did sometimes march? By heaven I charge thee speak.
'''

# Defining a passage from "Pride and Prejudice" by Jane Austen.
pride_and_prejudice = '''I think, however, though the thought will doubtless seem heretical to
more than one school of critics, that construction is not the highest
merit, the choicest gift, of the novelist. It sets off his other gifts
and graces most advantageously to the critical eye; and the want of it
will sometimes mar those graces--appreciably, though not quite
consciously--to eyes by no means ultra-critical. But a very badly-built
novel which excelled in pathetic or humorous character, or which
displayed consummate command of dialogue--perhaps the rarest of all
faculties--would be an infinitely better thing than a faultless plot
acted and told by puppets with pebbles in their mouths. And despite the
ability which Miss Austen has shown in working out the story, I for one
should put_ Pride and Prejudice _far lower if it did not contain what
seem to me the very masterpieces of Miss Austen’s humour and of her
faculty of character-creation--masterpieces who may indeed admit John
Thorpe, the Eltons, Mrs. Norris, and one or two others to their company,
but who, in one instance certainly, and perhaps in others, are still
superior to them.'''

# Splitting the "Hamlet" passage into individual words to create a list.
hamlet_list = hamlet.split()
# Displaying the list of words.
print(hamlet_list)

# Splitting the "Pride and Prejudice" passage into individual words to create a list.
pap_list = pride_and_prejudice.split()
# Displaying the list of words.
print(pap_list)

# Finding the difference between the sets of words in both passages.
# The difference operator (-) removes words from "hamlet_list" that are also in "pap_list."
difference = set(hamlet_list) - set(pap_list)
print("The difference (-) operator removes items in one set from another.")
print(difference)
print()

# Finding the intersection (common words) between the two sets of words.
# The intersection operator (&) returns words found in both sets.
similar = set(hamlet_list) & set(pap_list)
print("The intersection (&) operator returns items found in both sets.")
print(similar)
print()

# Finding the union of the two sets of words.
# The union operator (|) returns all unique words across both sets, removing duplicates.
union = set(hamlet_list) | set(pap_list)
print("The union operator (|) returns a set composed of all the items from both sets, with duplicates removed.")
print(union)
print()

# Finding the exclusive-or (XOR) between the two sets of words.
# The XOR operator (^) returns a set of words that are only found in one of the sets but not in both.
exclusive_or = set(hamlet_list) ^ set(pap_list)
print("The XOR (^) operator returns a set of items that are only found in one set or the other, but not both.")
print(exclusive_or)
print()
