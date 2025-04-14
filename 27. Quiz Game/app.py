import random

# --- Quiz Data ---
quiz_data = {
    "science": [
        {
            "question": "Who is known as the 'Missile Man of India'?",
            "options": ["Homi Bhabha", "C.V. Raman", "A.P.J. Abdul Kalam", "Vikram Sarabhai"],
            "answer": "A.P.J. Abdul Kalam"
        },
        {
            "question": "What is India’s first satellite called?",
            "options": ["Aryabhata", "Chandrayaan", "INSAT", "Rohini"],
            "answer": "Aryabhata"
        },
        {
            "question": "Which Indian physicist won the Nobel Prize for scattering of light?",
            "options": ["Satyendra Nath Bose", "Homi Bhabha", "C.V. Raman", "Meghnad Saha"],
            "answer": "C.V. Raman"
        },
        {
            "question": "Which organization is responsible for space research in India?",
            "options": ["NASA", "ISRO", "DRDO", "BARC"],
            "answer": "ISRO"
        },
        {
            "question": "India's Mars Orbiter Mission is called?",
            "options": ["Chandrayaan", "Gaganyaan", "Mangalyaan", "Bhaskara"],
            "answer": "Mangalyaan"
        }
    ],
    "films": [
        {
            "question": "Which Indian movie won the Oscar for Best Original Song in 2023?",
            "options": ["Lagaan", "Slumdog Millionaire", "RRR", "Gully Boy"],
            "answer": "RRR"
        },
        {
            "question": "Who played the role of 'Munna Bhai'?",
            "options": ["Aamir Khan", "Sanjay Dutt", "Shah Rukh Khan", "Akshay Kumar"],
            "answer": "Sanjay Dutt"
        },
        {
            "question": "Which Bollywood film is based on the life of Milkha Singh?",
            "options": ["Dangal", "Chak De India", "Bhaag Milkha Bhaag", "Mary Kom"],
            "answer": "Bhaag Milkha Bhaag"
        },
        {
            "question": "What is the real name of superstar 'Rajinikanth'?",
            "options": ["Shivaji Rao Gaekwad", "Mohanlal Viswanathan", "Kamal Haasan", "Vijay Chandrasekhar"],
            "answer": "Shivaji Rao Gaekwad"
        },
        {
            "question": "Which Indian actress starred in 'Piku', 'Chennai Express', and 'Padmaavat'?",
            "options": ["Katrina Kaif", "Alia Bhatt", "Priyanka Chopra", "Deepika Padukone"],
            "answer": "Deepika Padukone"
        }
    ],
    "games": [
        {
            "question": "Which Indian won gold in javelin throw at Tokyo Olympics 2020?",
            "options": ["Milkha Singh", "Neeraj Chopra", "Abhinav Bindra", "P.V. Sindhu"],
            "answer": "Neeraj Chopra"
        },
        {
            "question": "Who is known as the ‘Master Blaster’ in cricket?",
            "options": ["MS Dhoni", "Virat Kohli", "Sachin Tendulkar", "Rahul Dravid"],
            "answer": "Sachin Tendulkar"
        },
        {
            "question": "Which city hosted the first IPL match in 2008?",
            "options": ["Mumbai", "Bangalore", "Delhi", "Kolkata"],
            "answer": "Bangalore"
        },
        {
            "question": "What is the national sport of India (officially)?",
            "options": ["Cricket", "Hockey", "Kabaddi", "Football"],
            "answer": "Hockey"
        },
        {
            "question": "P.V. Sindhu is associated with which sport?",
            "options": ["Tennis", "Badminton", "Table Tennis", "Athletics"],
            "answer": "Badminton"
        }
    ],
    "general": [
        {
            "question": "What is the capital city of India?",
            "options": ["Mumbai", "Kolkata", "New Delhi", "Chennai"],
            "answer": "New Delhi"
        },
        {
            "question": "Who was the first Prime Minister of India?",
            "options": ["Jawaharlal Nehru", "Indira Gandhi", "Sardar Patel", "Mahatma Gandhi"],
            "answer": "Jawaharlal Nehru"
        },
        {
            "question": "Which river is considered the holiest in India?",
            "options": ["Yamuna", "Godavari", "Ganga", "Brahmaputra"],
            "answer": "Ganga"
        },
        {
            "question": "Which state is known as the 'Land of Five Rivers'?",
            "options": ["Uttar Pradesh", "Punjab", "Rajasthan", "Bihar"],
            "answer": "Punjab"
        },
        {
            "question": "What is the national currency of India?",
            "options": ["Dollar", "Rupee", "Pound", "Yen"],
            "answer": "Rupee"
        }
    ]
}

def startQuiz(genera):
    score=0
    index=0
    data=quiz_data[genera]
    for item in data:
        print()
        print(f' {index+1}. {genera} Question '.center(100,'-'))
        print('Question:',item['question'])
        a=1
        for i in (item['options']):
            print(f'{a}. {i}')
            a+=1
        while True:
            try:
                ans=int(input('Enter No: '))
                if(ans>4 or ans<1):
                    print('Enter value in range 1-4')
                    continue
                break
            except ValueError:
                print('Enter int value')
                continue
        if(item["options"][ans-1]==item['answer']):
            score+=10
            print('Correct Answer ✅')
        else:
            print('Wrong Answer ❌')
        index+=1
    print('\nTotal Score is 🧿 ',score)
        
def main():
    while( True):
        try:
            print('🧠 Quiz Game '.center(100,'-'))
            print(' - Which Genere you want to play Quiz\n - Enter quit to exit\n')
            genera=input(' - we have science,films,genral,games\n Enter choice Name ').lower().strip()
            if(genera in quiz_data):
                print('We will ask 5 question provide option no accordingly\n')
                startQuiz(genera)
            else:
                print('we dont provide quiz for that genere')
            if(genera =='quit'):
                print('Goodbye')
                break
        except:
            print('Enter correct choice ')
            continue
main()

