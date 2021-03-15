#!python3
import random

capitals = {
    'Alabama': 'Montgomery', 
    'Alasca': 'Juneau', 
    'Arkansas': 'Little Rock', 
    'Arizona': 'Phoenix', 
    'Califórnia': 'Sacramento', 
    'Carolina do Norte': 'Raleigh', 
    'Carolina do Sul': 'Columbia', 
    'Colorado': 'Denver', 
    'Connecticut': 'Hartford', 
    'Dakota do Norte': 'Bismarck', 
    'Dakota do Sul': 'Pierre', 
    'Delaware': 'Dover', 
    'Flórida': 'Tallahassee', 
    'Geórgia': 'Atlanta', 
    'Havaí': 'Honolulu', 
    'Idaho': 'Boise', 
    'Indiana': 'Indianápolis', 
    'Iowa': 'Des Moines', 
    'Kansas': 'Topeka', 
    'Kentucky': 'Frankfort', 
    'Louisiana': 'Baton Rouge', 
    'Maine': 'Augusta', 
    'Maryland': 'Annapolis', 
    'Massachusetts': 'Boston', 
    'Michigan': 'Lansing', 
    'Minnesota': 'Saint Paul', 
    'Mississipi': 'Jackson', 
    'Missouri': 'Jefferson City', 
    'Montana': 'Helena', 
    'Nebraska': 'Lincoln', 
    'Nevada': 'Carson City', 
    'New Hampshire': 'Concord', 
    'New York': 'Albany', 
    'New México': 'Santa Fe', 
    'Oklahoma': 'Oklahoma City', 
    'Ohio': 'Columbus', 
    'Oregon': 'Salem', 
    'Pennsylvania': 'Harrisburg', 
    'Tennessee': 'Nashville', 
    'Texas': 'Austin', 
    'Utah': 'Salt Lake City', 
    'Vermont': 'Montpellier', 
    'Virgínia': 'Richmond', 
    'Washington': 'Olympia', 
    'Wisconsin': 'Madison', 
    'Wyoming': 'Cheyenne'
}
for quizNum in range(35):
    # Cria os arquivos com as provas e os gabaritos das respostas
    quizFile = open('capitalsquiz%s.txt'%(quizNum +1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt'%(quizNum +1), 'w')
    # Escreve o cabeçalho da prova
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)'%(quizNum +1))
    quizFile.write('\n\n')
    # Embaralha a ordem dos estados
    states = list(capitals.keys())
    random.shuffle(states)
    
    # Percorre todos os 46 estados em um loop, criando uma pergunta para cada um
    for questionNum in range(46):
        # obtém respostas corretas e incorretas
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # Grava a pergunta e as opções de resposta no arquivo de prova
        quizFile.write('%s. What is the capital of %s?\n'%(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s.%s\n'%('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
            # Grava o gabarito com as respostas em um arquivo
        answerKeyFile.write('%s.%s\n'%(questionNum +1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
