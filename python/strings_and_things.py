class StringsAndThings:
    """
    Python equivalent of the Java StringsAndThings class
    """

    def count_yz(self, input_str):
        """
        Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in "heavy" and the 'z' in "fez" count,
        but not the 'y' in "yellow" (not case sensitive). We'll say that a y or z is at the end of a word if there is not an alphabetic
        letter immediately following it. (Note: Character.isLetter(char) tests if a char is an alphabetic letter.)
        example : count_yz("fez day"); // Should return 2
                  count_yz("day fez"); // Should return 2
                  count_yz("day fyyyz"); // Should return 2
        """
        return None

    def remove_string(self, base, remove):
        """
        Given two strings, base and remove, return a version of the base string where all instances of the remove string have
        been removed (not case sensitive). You may assume that the remove string is length 1 or more.
        Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

        example : remove_string("Hello there", "llo") // Should return "He there"
                  remove_string("Hello there", "e") //  Should return "Hllo thr"
                  remove_string("Hello there", "x") // Should return "Hello there"
        """
        return None

    def contains_equal_number_of_is_and_not(self, input_str):
        """
        Given a string, return true if the number of appearances of "is" anywhere in the string is equal
        to the number of appearances of "not" anywhere in the string (case sensitive)

        example : contains_equal_number_of_is_and_not("This is not")  // Should return false
                  contains_equal_number_of_is_and_not("This is notnot") // Should return true
                  contains_equal_number_of_is_and_not("noisxxnotyynotxisi") // Should return true
        """
        return None

    def g_is_happy(self, input_str):
        """
        We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.
        Return true if all the g's in the given string are happy.
        example : g_is_happy("xxggxx") // Should return  true
                  g_is_happy("xxgxx") // Should return  false
                  g_is_happy("xxggyygxx") // Should return  false
        """
        return None

    def count_triple(self, input_str):
        """
        We'll say that a "triple" in a string is a char appearing three times in a row.
        Return the number of triples in the given string. The triples may overlap.
        example :  count_triple("abcXXXabc") // Should return 1
                   count_triple("xxxabyyyycd") // Should return 3
                   count_triple("a") // Should return 0
        """
        return None