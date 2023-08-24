class RomanNumerals:

    @staticmethod
    def to_roman(val):
        num = [1000, 500, 100, 50, 10, 5, 1,0]
        roman = ["M", "D", "C", "L", "X", "V", "I"]

        out = ""

        for i in range(7):
            if int(val/num[i]) == 4:
                 val -= num[i]*4
                 out += roman[i] + roman [i-1]
            elif int(val/(num[i-1] - num[i+1])) == 1 and i % 2 == 1:
                val -= num[i+1]*9
                out += roman[i+1] + roman[i-1]
            else:
              for j in range(int(val/num[i])):
                out += roman[i]
                val -= num[i]
        return out

    @staticmethod
    def from_roman(roman_num):
        nums = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }

        out = 0
        hold = []

        for elem in roman_num:
            hold.append(elem)
            if (len(hold) >= 2):
                if nums[hold[0]] < nums[hold[1]]:
                    out +=  nums[hold[1]] - nums[hold[0]]
                    hold.pop(0)
                    hold.pop(0)
                elif nums[hold[0]] == nums[hold[1]]:
                    out += nums[hold[0]]
                    hold.pop(0)
                else :
                    out += nums[hold[0]]
                    hold.pop(0)
        
        for elem in hold:
            out += nums[elem]

        return out
