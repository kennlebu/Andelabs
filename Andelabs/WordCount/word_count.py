class WordCount:
    @staticmethod
    def words(sentence):
        dictionary = {}
        words_list = sentence.split()
        for each in words_list:
            try:
                each = int(each)
            except Exception:
                pass

        
        for word in (words_list):
            if word in dictionary.keys(): dictionary[word] += 1
            else: dictionary[word] = 1

        return dictionary
