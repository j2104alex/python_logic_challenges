import calendar
import re
import textwrap
from collections import defaultdict

'''Given the participans score sheet for your University Sports Day, you are in required to find the runner-up-score
(segunda puntuacion). You are given n scores. Store them in a list and find the score of the runner-up'''


def up_score():
    """Se crea un objeto de tipo map y para poder trabajar con el se puede hacer en una lista"""
    score_list = list(map(int, input().split()))
    '''Ordenar la lista de mayor a menor'''
    score_list.sort(reverse=True)

    for score in score_list:
        if score < max(score_list):
            up_score_result = score
            print(up_score_result)
            break


# up_score()

'''You given 3 integers x,y,z and representing the dimensions of a cuboid along with an integer n
Print a list of all possible coordinates given by (i,j,k) on a 3d grid where the sum of i+j+k is not equial to n'''


def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())

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


'''Given the names and grades for each student in a class of N students, store them (almacenarlos) in a nested (anidada)
 list and print the names of any student having the second lowest grade
If there are multiple students with the second lowest grade, order their name alpabetically and print each name on a new
 line'''


def nested_list():
    list_students = []
    set_score = []
    second_lowest_grade = 0
    response = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp_student = [name, score]
        list_students.append(temp_student)
    print(list_students)

    for name, score_student in list_students:
        set_score.append(score_student)

    set_score = set(set_score)

    '''Retorna una lista ordenada descendente'''
    sorted_list = sorted(set_score)

    for score in sorted_list:
        if score > min(sorted_list):
            second_lowest_grade = score
            print(f'Segundo GRADO MAS BAJO: {second_lowest_grade}')
            break

    for name, score_student in list_students:
        if score_student == second_lowest_grade:
            response.append(name)
    print(response)
    response.sort()
    for student in response:
        print(student)


# nested_list()

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

    for name, scores in student_marks.items():
        if query_name == name:
            percent = round(sum(scores) / len(scores), 2)
            formatted_percent = "{:.2f}".format(percent)
            print(formatted_percent)

            '''format formatea un flotante y lo convierte en string
            OJO: La expresión "{:.2f}" es una cadena de formato utilizada en Python para formatear números de punto 
            flotante con una precisión específica.

            {}: Los corchetes {} se utilizan como marcadores de posición para los valores que se van a formatear.
            :'esta_seccion'   se utiliza para separar el especificador de formato del marcador de posición.
            El .2f es el especificador de formato en sí. En este caso, el .2 indica que se deben mostrar dos dígitos 
            después del punto decimal, y la f indica que el valor a formatear es un número de punto flotante.'''


# finding_the_percentage()

'''You given a string s consisting only of digits 0-9 commas , and dots . your task is to complete the regex_pattern 
defined below, which will be used to re.split() all
the , and . simbols in s
It's guaranteed that every comma and every dot in s is preceded and followed by a digit'''


def regex_and_parsing():
    regex_pattern = r"[,.]"
    print("\n".join(re.split(regex_pattern, input())))


# print(regex_and_parsing())

'''Consider a list (list=[]) you can perform the following commands:
    -insert i e: Insert integer e at position i
    -print: Print the list
    -remove e: Delete the first ocurrence of integer e
    -append e: IInsert integer e at the end of the list
    -sort Sort the list
    -pop_ Pop the last element from the list
    -reverse: Reverse the list'''


def lists():
    n = int(input())
    command_list = []
    response_list = []
    for i in range(n):
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


# print(lists())

'''Given an integer n and n space-separated integer as input, create a tuple t of those n integers. 
Then compute and print the result of hash(t)'''


def hash_tuppla():
    tup = tuple(map(int, input().split()))
    print(hash(tup))


# hash_tuppla()

'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
 letters and vice versa.'''


def swap_case(s):
    x = s.swapcase()
    print(x)


# swap_case('bACa')

'''split space delimiter and join with "-"'''


def split_and_join(line):
    line = line.split(' ')
    line = '-'.join(line)
    print(line)


# split_and_join('This is a string')

'''We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).'''


def mutate_string(string, position, character):
    lista = list(string)
    lista[position] = character
    string = ''.join(lista)
    return string


# print(mutate_string('abracadabra',5,'k'))

'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
 occurs in the given string. String traversal will take place from left to right, not from right to left.'''


def count_substring(string, sub_string):
    count = 0
    sub_length = len(sub_string)

    for i in range(len(string) - sub_length + 1):
        if string[i:i + sub_length] == sub_string:
            count += 1
    return count


# print(count_substring('ABCDCDC','CDC'))


'''You are given a string s and w width .
Your task is to wrap the string into a paragraph of width .'''


def wrap(string, max_width):
    text_wrap = textwrap.wrap(string, max_width)
    text_join = '\n'.join(text_wrap)
    return text_join


'''Given an n integer, , print the following values  for each integer i from  
1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary'''


def print_formatted(number):
    width = len(bin(number)[2:])  # Ancho maximo del binario que es el numero mas largo de las representaciones
    for i in range(1, number + 1):
        # Ajustar texto a la derecha con base al ancho de wisth
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(f'{decimal} {octal} {hexadecimal} {binary}')
        # Nota: En los octals, hexadecimales y binarios se anteponen prefijos por eso se ignora
        # La primera posición
        print(decimal, octal, hexadecimal, binary)


# print_formatted(14)

'''First letter capitalized'''


def solve(s):
    s = s.title()
    return s


# print(solve('Hola mundo'))

'''Ms. Gabriel Williams is a botany professor at District College. One day, 
she asked her student Mickey to compute the average of all the plants with 
distinct heights in her greenhouse.'''


def average(array):
    array_setted = set(array)
    total_average = (sum(array_setted) / (len(array_setted)))
    return total_average


# print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))

'''Output the symmetric difference integers in ascending order, one per line.'''


def symetric_difference():
    data = []
    for n in range(4):
        question = input()
        data.append(question)

    a = set(map(int, data[1].split()))
    b = set(map(int, data[3].split()))

    sym_difference = sorted(a.symmetric_difference(b))

    for number in sym_difference:
        print(number)


'''You are given an integer,N. Your task is to print an alphabet rangoli
 of size N. (Rangoli is a form of Indian folk art based on creation of 
 patterns.)'''


def rangoli_pattern(number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    usable_alphabet = alphabet[:number]

    lines = []

    for i in range(number):
        mid = usable_alphabet[number - i - 1:number]
        reversed_mid = usable_alphabet[number:number - i - 1:-1]
        line = (reversed_mid + mid)
        line = '-'.join(line)
        line = line.center((number * 4) - 3, '-')
        lines.append(line)
        lines.append('\n')
    down_lines = lines[:-2]
    down_lines.reverse()
    result = ''.join(lines).rstrip('\n') + ''.join(down_lines)

    print(result)


# rangoli_pattern(25)
'''Capitalize the first letter'''


def capitalize_word(s):
    for w in s.split():
        s = s.replace(w, w.capitalize())
    return s


# print(capitalize_word('hola mundo'))

'''Validations for basic data is a string is composed of alphanumeric character,
alphabetical characters, if has any digits and if has any lowercase character'''


def string_validations(s):
    print(any(letter.isalnum() for letter in s))
    print(any(letter.isalpha() for letter in s))
    print(any(letter.isdigit() for letter in s))
    print(any(letter.islower() for letter in s))
    print(any(letter.isupper() for letter in s))


# string_validations('qA2')

'''Get the day of the week from de given date'''


def date_day(date):
    date = date.split()
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    print(day, month, year)
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())


#date_day('08 05 2015')

def default_dict(a,b):

    positions=defaultdict(list)

    for i, element in enumerate(a):
       positions[element].append(i)

    for element in b:
        if element in positions:
            response = ' '.join(str(idx+1) for idx in positions[element])
        else:
            response = -1
        print(response)
a=['a', 'b', 'a']
b=['a','c']
default_dict(a,b)
