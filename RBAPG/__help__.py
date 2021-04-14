help_content="""
[!]This python module is a "Wordlist Generator".
[!]This module can be used in projects based on Dictionary Attacks.
	USAGE:

        NECESSERY STEPS:

        Defind a variable for RuleBasedAttackPasswordGenerator class.
            #>RBAPG=RBAPG_.RuleBasedAttackPasswordGenerator()

        Set a name for the wordlist
            #>RBAPG.setWordlistName("wordlist.txt")

        Set the length of password
            #>RBAPG.setLengthOfGeneratedPassword(min2-max4)

        Set the wordlist content
            #>RBAPG.wordlist="name surname year etc."

        Generate the wordlist:
            #RBAPG.generate_wordlist()

	--------------------------------------------------------------------------------------------
	OPTIONAL STEPS:

	Aziz's combination algorithm. It's based on changing some certain indexes of password in the wordlist.
	    #>RBAPG.CombineCozily()

        Tries the every combination of each password in the wordlist.
        Note:Not recommended for a huge content of wordlist.
	    #>RBAPG.CombineTheWords()

        """
print(help_content)