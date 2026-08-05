n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
#print(scores) - testando valores
scores = student_marks[query_name]
soma_total = sum(scores)
numero_de_algarismos = len(scores)
#print(numero_de_algarismos)
media_de_score = soma_total / numero_de_algarismos
print(f"{media_de_score:.2f}")