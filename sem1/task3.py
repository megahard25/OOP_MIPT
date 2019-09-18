dictionary =  {
                1 : 'a',
                2 : 'b',
                3 : 'c',
                4 : 'd',
                5 : 'e'
                }
print({key:dictionary[key] for key in reversed(list(dictionary.keys()))})
