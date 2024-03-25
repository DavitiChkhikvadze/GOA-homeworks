# პირველ ამოცანის პირობაში შეცდომა არის, ამიტომ თავიდან დავწერ მაგ პირობას
# ამოცანა 1.
# მოცემულია მასივი, საიდანაც ამოიღებთ მინიმალურ ციფრს/რიცხვს.
# თუ ამ მასივში არის ორი ან მეტი ერთნაირი მინიმალური ციფრი/რიცხვი,
# მაშინ ამოაგდეთ ის მინიმალური, რომლის ინდექსიც უფრო ნაკლებია.

# Input: [1,2,3,4,5], output = [2,3,4,5]
# Input: [5,3,2,1,4], output = [5,3,2,4]
# Input: [2,2,1,2,1], output = [2,2,2,1]

def handle_min_max (a):
    a.remove(min(a))
    # a.remove(max(a))
    return a

print(handle_min_max([1,2,3,4,5]))
print(handle_min_max([5,3,2,1,4]))
print(handle_min_max([2,2,1,2,1]))

# შექმენით ფუნქცია, რომლის საშუალებითაც ორ პარამეტრს 
# გაამრავლებთ ერთმანეთზე

# test case — (12, 100)
# test case — (97, 120)

def multyply(a,b):
    return a*b
print(multyply(12, 100))
print(multyply(97, 120))

# ამოცანა 3.
# შექმენით ფუნქცია, რომელიც მასივში ყველაზე მოკლე სიტყვის
# სიგრძეს ციფრად/რიცხვად დააბრუნებს.

# test case - ("Let's travel abroad shall we"), 2)
# test case - ("lets talk about javascript the best language"), 3)

def latest(a):
    arr = []
    a = a.split()
    for char in a:
        arr.append(len(char))
    print(min(arr))
latest("Let's travel abroad shall we")
latest("lets talk about javascript the best language")

# შექმენით ფუნქცია, რომლის საშუალებითაც მასივში მხოლოდ იმ ელემენტების
# ჯამს შეკრიბავთ, რომლებიც მხოლოდ ერთხელ მეორდება.

# test case -- ([4,5,7,5,4,8]),15)
# test case -- ([9, 10, 19, 13, 19, 13]),19)

def funtion_1(a):
    num =0 
    for i in a:
        if a.count(i) == 1:
            num +=i
    print(num)
funtion_1([4,5,7,5,4,8])
funtion_1([9, 10, 19, 13, 19, 13])



# ამოცანა 5.

# შექმენით ფუნქცია, რომელიც სტრინგში ამოიღებს 
# მაქსიმალურ და მინიმალურ რიცხვებს.

# test case -- ("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
# test case -- ("1 2 3"), "3 1")

def function_2 (a):
    a = a.split(" ")
    arr = []
    for i in a:
        arr.append(int(i))
    print(' '.join([str(max(arr)) , str(min(arr))] ))
function_2("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
function_2("1 2 3")

# ამოცანა 6.
# დაწერეთ ფუნქცია, რომელიც იღებს ორ პარამეტრს (integer, limit) 
# და უნდა გამოიტანოთ ყველა რიცხვი იქნება ყველა რიცხვი 
# integer-დან limit-მდე. თითოეული რიცხვი გაიზრდება integer-ით
# ანუ თუ (2, 8) იქნება პარამეტრები, მაშინ გამოიტანეთ [2, 4, 6, 8].

# test case -- (5, 25), [5, 10, 15, 20, 25]
# test case -- D, [1, 2])

def function_2(a, b):
    arr = []
    for i in range(a, b+1, a):
        arr.append(i)
    print(arr)

function_2(5, 25)

# ამოცანა 7.
# დაწერეთ ფუნქცია (Hashtag Generator) სადაც ცვლადის პირველი ელემენტი
# იქნება '#', შემდეგ მიუწერთ სტრინგის ყოველ სიტყვას ოღონდ 
# (Capitalize - ანუ პირველი ასო დიდი) ფორმაში.
# გამოიტანეთ False თუ სტრინგი ცარიელია.

# test case -- D  =>  "#HelloThereThanksForTryingMyKata"
# test case -- 'c i n' => '#CIN'
# test case -- '' => False

def function_3 (a):
    splited_str = a.split(" ")

    result = '#'
    if len(a) == 0:
        print(False)
    for i in a:
        if i != " ":
            result += i.capitalize()

    print(result)
function_3('c i n')


# ამოცანა 8.
# შექმენით ფუნქცია, რომლის საშუალებითაც გადაიტანთ
#  0-ებს მასივის ბოლო ინდექსებზე.
# მაგალითად --- ([1, 0, 1, 2, 0, 1, 3]) => [1, 1, 2, 1, 3, 0, 0]

# test case -- [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),  [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
# test case -- [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])d
def fucnrion_5(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    print(arr)
    
fucnrion_5([1, 0, 1, 2, 0, 1, 3])
fucnrion_5( [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])

# ამოცანა 9.
# საჩუქრად ❤️ 
# გადაიყვანეთ ამერიკული დოლარი, ჩინურ იენში.
# (ამ შემთხვევაში 6.75 ჩინური იენი => 1 ამერიკული დოლარის)
# აუცილებელია რომ წერტილის შემდეგ მეასედი იყოს ანუ (2 ციფრი)

# test case - 15  -> '101.25 Chinese Yuan'
# test case - 465 -> '3138.75 Chinese Yuan'
# test case - 178674 -> '1206049.50 Chinese Yuan'

def func_1 (a):
    print(str(round(a*6.75, 2)) +' '+ 'Chinese Yuan')
func_1(15)
func_1(465)