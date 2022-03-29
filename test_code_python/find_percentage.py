ctr = 0
scores = 0.00
total_score = 0.00
student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks[query_name]:
        scores = float(i)
        total_score = total_score + scores
        ctr+=1
    
    print("%.2f" % round((total_score/ctr),3))