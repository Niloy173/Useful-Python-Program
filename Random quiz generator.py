# generating n number of different quizzes ( in this program n =2)
# creating n multiple choice question for each quiz in random order ( in this progam n =10)


import random
cities = {'Dhaka': '316', 'Chittagong': '155', 'Rajshahi': '97',
   'Mymensingh': '91.315', 'Khulna': '51', 'Sylhet': '42',
   'Barisal': '69', 'Rangpur': '50.69', 'Comilla': '23.44',
   'Narayangonj': '12.69', 'Gazipur': '47.23', 'Bogra': '69.56', 'Kushtia':
   '42.79', 'Jessore': '28.56', 'Cox''s Bazar': '24.45', 'Manikgonj':
   '42.28', 'Brahmanbaria': '22.49', 'Dinajpur': '22.00', 'Nawabganj':
   '32.09', 'Tangail': '33.80', 'Sirajganj': '31.27', '	Chandpur':
   '22', 'Feni': '22.00', 'Jamalpur': '55.25', 'naogaon':
   '38.36', 'narsingdi': '14.8', 'Pabna': '27.27', 'Maijdee':
   '23.79','Faridpur': '19.78', 'Jhenaidah': '39.63'

            }

for num in range(2):

    #create quiz and answer file

    quiz_file = open('cites_area_quiz %s.txt'%(num+1),'a')

    answer_file = open(f'answer_sheet{num+1}.txt','a')

    #header of each quiz

    quiz_file.write('Name:\n\nDate:\n\nTime:\n\n')
    quiz_file.write(('-'*20)+'City Area Question (FROM %s)'%(num+1)+('-'*20))
    quiz_file.write('\n\n')

    city = list(cities.keys())
    random.shuffle(city)

    #get the right and wrong answer
    # loop thrugh the cities and make 10 question for each

    for question_num in range(10):

        correct_answer = cities[city[question_num]]
        wrong_answer = list(cities.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer,3)
        answers = wrong_answer + [correct_answer]
        random.shuffle(answers)

        #writing the question and answer script

        quiz_file.write("%s.what is the area(persquare km) of %s ?\n"%(question_num+1,city[question_num]))

        for i in range(4):

            quiz_file.write(" %s. %s\n"%('ABCD'[i],answers[i])) #string'ABCD' as an array and will evaulate as 'A','B','C','D'
        quiz_file.write("\n")
            #give us correct letter/option  
            #answer_file.write(f"{question_num+1}.{'ABCD'[answers.index(correct_answer)]}")
        
        answer_file.write("%s %s\n"%(question_num+1,"ABCD"[answers.index(correct_answer)]))
            
# close all files

quiz_file.close()
answer_file.close()
    
