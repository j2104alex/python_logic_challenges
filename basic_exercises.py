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

#nested_list()

'''The provided code stub will read in a dictionary containig key/value pairs of name:[marks] for a list of student.
Print the average of the marks array for the student name provided, showing 2 places after the decimal'''
def finding_the_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)

    for name,scores in student_marks.items():
        if query_name==name:
            percent=round(sum(scores)/len(scores),2)
            formatted_percent = "{:.2f}".format(percent)
            print(formatted_percent)

            '''format formatea un flotante y lo convierte en string
            OJO: La expresión "{:.2f}" es una cadena de formato utilizada en Python para formatear números de punto flotante con una precisión específica.

            {}: Los corchetes {} se utilizan como marcadores de posición para los valores que se van a formatear.
            :'esta_seccion'   se utiliza para separar el especificador de formato del marcador de posición.
            El .2f es el especificador de formato en sí. En este caso, el .2 indica que se deben mostrar dos dígitos después del punto decimal, y la f 
            indica que el valor a formatear es un número de punto flotante.'''
#finding_the_percentage()

'''You given a string s consisting only of digits 0-9 commas , and dots . your task is to complete the regex_pattern defined below, which will be used to re.split() all
the , and . simbols in s
It's guaranteed that every comma and every dot in s is preceded and followed by a digit'''
import re
def regex_and_parsing():
    regex_pattern = r"[,.]"
    print("\n".join(re.split(regex_pattern, input())))
#print(regex_and_parsing())

'''Consider a list (list=[]) you can perform the following commands:
    -insert i e: Insert integer e at position i
    -print: Print the list
    -remove e: Delete the first ocurrence of integer e
    -append e: IInsert integer e at the end of the list
    -sort Sort the list
    -pop_ Pop the last element from the list
    -reverse: Reverse the list'''
def lists():
    N = int(input())
    command_list = []
    response_list = []
    for i in range(N):
        command = input().split()
        command_list.append(command)

    for command, *args in command_list:
        if command == 'reverse':
            response_list.reverse()
        elif command == 'insert':
            i, e = map(int, args)
            response_list.insert(i, e)
        elif command == 'remove':
            e = int(args[0])
            response_list.remove(e)
        elif command == 'append':
            e = int(args[0])
            response_list.append(e)
        elif command == 'sort':
            response_list.sort()
        elif command == 'pop':
            response_list.pop()
        else:
            print(response_list)
#print(lists())

'''Given an integer n and n space-separated integer as input, create a tuple t of those n integers. Then compute and print the result of hash(t)'''
def hash_tuppla():
    tup=()
    n = int(input())
    tup = tuple(map(int, input().split()))
    print(hash(tup))

#hash_tuppla()