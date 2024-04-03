def intToRoman(num):
        roman_values = ["M","CM","D","CD","C", "XC","L","XL","X","IX","V","IV","I"]
        int_values = [1000, 900, 500, 400, 100,90, 50,40, 10, 9, 5,4, 1]
        result = ''
        for i in range(len(roman_values)):
            while num >= int_values[i]:
                # Add the symbol to the result
                result += roman_values[i]
                # Subtract the corresponding int_value from the number
                num -= int_values[i]
        
        return result