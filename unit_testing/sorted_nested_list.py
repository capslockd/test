
class Sorter():
    def __init__(self, data):
        self.data = data
        self.ctr = 0

    def sort(self, element):
        self.data = sorted(self.data, key=lambda x: x[element], reverse=False)
        return self.data

    def score_checker(self, comparison_value, score_list):
        if comparison_value == score_list[0][1]:
            for _ in range(len(score_list)):
                
                if self.ctr != 0: 
                    if score_list[_][1] != comparison_value:
                        comparison_value = score_list[_][1]
                        break
                else:
                    self.ctr += 1

        return comparison_value

    def check_students(self, score_value, score_list):
        return_list = []
        results = []
        for i,j in score_list:
            if j == score_value:
                return_list.append(i)

        return_list.sort()
        for _ in return_list:
            results.append(_)

        return results

inputv = [['Harsh','20'],
['Beria','20'],
['Varun','19'],
['Kakunami','19'],
['Vikas','21']]

sorter = Sorter(inputv)
sorted_list = sorter.sort(1)
print (sorted_list)
second_lowest = sorter.score_checker(sorted_list[0][1], sorted_list)
check_students = sorter.check_students(second_lowest, sorted_list)