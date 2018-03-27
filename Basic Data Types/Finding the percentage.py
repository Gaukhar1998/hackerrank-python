if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
        
#another solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
d = [raw_input().split() for i in xrange(input())]
e = dict(zip([i[0] for i in d], [sum(map(float,i[1:]))/(len(i)-1) for i in d]))
print "%.2f" % e[raw_input()]
