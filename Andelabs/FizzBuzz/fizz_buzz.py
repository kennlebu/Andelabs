class FizzBuzz(object):
    @staticmethod
    def fizz_buzz(num):
        result = ''
        if num%3 == 0: result += 'Fizz'
        if num%5 == 0: result += 'Buzz'
        if len(result) < 4: result = num

        return result
    
    
