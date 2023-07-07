'''Given the participans score sheet for your University Sports Day, you are in required to find the runner-up-score
(segunda puntuacion). You are given n scores. Store them in a list and find the score of the runner-up'''
def up_score():
    n=int(input())
    '''Se crea un objeto de tipo map y para poder trabajar con el se puede hacer en una lista'''
    score_list=list(map(int,input().split()))
    '''Ordenar la lista de mayor a menor'''
    score_list.sort(reverse=True)

    for score in score_list:
        if score<max(score_list):
            up_score_result=score
            print(up_score_result)
            break

#up_score()

'''You given 3 integers x,y,z and representing the dimensions of a cuboid along with an integer n
Print a list of all possible coordinates given by (i,j,k) on a 3d grid where the sum of i+j+k is not equial to n'''
def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result_list = []

    for i in range(x + 1):
        print(f'externo: {i}')
        for j in range(y + 1):
            print(f'interno: {j}')
            for k in range(z + 1):
                print(f'interno interno: {k}')
                if i + j + k != 3:
                    tem_item = [i, j, k]
                    result_list.append(tem_item)
                    print(tem_item)
    print(result_list)

'''Given the names and grades for each student in a class of N students, store them (almacenarlos) in a nested (anidada) list
and print the names of any student having the second lowest grade
If there are multiple students with the second lowest grade, order their name alpabetically and print each name on a new line'''
def nested_list():
    list_students=[]
    set_score=[]
    second_lowest_grade=0
    response=[]

    for _ in range(int(input())):
        name=input()
        score=float(input())
        temp_student=[name,score]
        list_students.append(temp_student)
    print(list_students)

    for name,score_student in list_students:
        set_score.append(score_student)

    set_score=set(set_score)

    '''Retorna una lista ordenada descendente'''
    sorted_list=sorted(set_score)

    for score in sorted_list:
        if score > min(sorted_list):
            second_lowest_grade=score
            print(f'Segundo GRADO MAS BAJO: {second_lowest_grade}')
            break

    for name,score_student in list_students:
        if score_student==second_lowest_grade:
            response.append(name)
    print(response)
    response.sort()
    for student in response:
        print(student)

nested_list()