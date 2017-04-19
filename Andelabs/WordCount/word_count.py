class WordCount:
    @staticmethod
    def words(sentence):
        dictionary = {}
        words_list = sentence.split() #spliting at white spaces characters to make a list of the words
        counter = 0
        
        """ Looping through the words, changing the numbers to int objects """
        for each in words_list:
            try:
                words_list[counter] = int(words_list[counter])
                counter += 1
            except ValueError:
                counter += 1
        
        for word in (words_list):
            if word in dictionary.keys(): dictionary[word] += 1
            else: dictionary[word] = 1

        return dictionary
