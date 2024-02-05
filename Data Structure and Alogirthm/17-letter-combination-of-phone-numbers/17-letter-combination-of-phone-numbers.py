class Solution(object):
    def get_telephone_letters_on_digits(self):
        telephone_num_list = ['2','3','4','5','6','7','8','9']
        alphabet_list = [chr(loc) for loc in range(97,123)]
        telephone_num_dict = {}
        letter = 0
    
        for i in range(len(telephone_num_list)):
            if i not in [5,7]:
                telephone_num_dict[telephone_num_list[i]] = alphabet_list[letter:(letter+3)]
                letter += 3
            else:
                telephone_num_dict[telephone_num_list[i]] = alphabet_list[letter:(letter+4)]
                letter += 4

        return telephone_num_dict

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        Return all possible letter combinations that the number could represent
        """
        outputs = []
        list_digits = list(digits)
        if not list_digits:  # Check for empty input
            return []  # Return an empty list if no digits are provided
        telephone_num_dict = self.get_telephone_letters_on_digits()
        telephone_num_input = {}
        for num in list_digits:
            telephone_num_input[num] = telephone_num_dict[num]
        
        letter_num = 0
        first_letter_list = telephone_num_input[list_digits[0]]
        if len(list_digits) == 1:
            return first_letter_list
        else:
        
        for i in range(len(list_digits)):
            for letter_num in range(len(first_letter_list)):
                for j in range(1, len(list_digits)):
                    # Ensure both letter_num and loc are within valid ranges
                    list_combine = []   
                    if letter_num < len(telephone_num_input[list_digits[0]]):  
                        list_combine = [first_letter_list[letter_num] + telephone_num_input[list_digits[j]][loc] for loc in range(3)]
                        outputs += list_combine
                    else:
                        break  # Exit inner loop if either index exceeds valid range


  
        return outputs

        