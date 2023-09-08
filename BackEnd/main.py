from flask import Flask 
import pandas as pd

app = Flask(__name__)

df = pd.read_excel('mudadadicio (1).xlsx')
df['deficiências'] = df['deficiências'].astype(str)

sports = {
    "Atletismo": 1,
    "Badminton": 2,
    "Bocha": 3,
    "Canoagem velocidade": 4,
    "Ciclismo de estrada": 5,
    "Ciclismo de pista": 6,
    "Equestre": 7,
    "Futebol de cinco": 8,
    "Golbol": 9,
    "Judo": 10,
    "Levantamento de peso": 11,
    "Remo": 12,
    "Tiro": 13,
    "Voleibol paralimpico": 14,
    "Natação": 15,
    "Tenis de mesa": 16,
    "Taekwondo": 17,
    "Triatlo": 18,
    "Basquete em cadeira de rodas": 19,
    "Esgrima em cadeira de rodas": 20,
    "Rugby em cadeira de rodas": 21,
    "Tenis em cadeira de rodas": 22,
    "Tiro com arco": 23,
    "Basquete": 24,
    "Tenis": 25,
    "Jiu-jitsu": 26
}

description = {
    1: 'O atletismo é um esporte formado por três modalidades: corridas, saltos e arremessos. Essas modalidades são disputadas em vários tipos de provas, e que cada prova pode ter subdivisões conforme as diferentes distâncias, os tipos de percurso, os equipamentos usados, entre outros.', 
    2: 'Badminton é um esporte dinâmico praticado entre dois ou quatro jogadores. Ainda que seja semelhante ao tênis, que usa raquetes e está dividido por uma rede, ele possui suas peculiaridades. Ao invés de uma bola, ele é jogado com uma espécie de peteca, chamada de volante ou birdie.',
    3: 'A Bocha é um esporte jogado entre duas equipes, cada qual tendo direito a seis bochas (bolas) na modalidade trio, quatro bochas na modalidade de duplas – duas para cada atleta –, e quatro também na modalidade individual. O esporte consiste em lançar bochas (bolas) e situá-las o mais perto possível de um bolim (bola pequena), previamente lançado.',
    4: 'A canoagem velocidade é um esporte aquático em que os atletas competem de canoa ou caiaque em águas calmas.',
    5: 'O ciclismo de estrada é a forma mais difundida de ciclismo em que os ciclistas andam em estradas pavimentadas. Inclui lazer , corrida , deslocamento e ciclismo utilitário.',
    6: 'O ciclismo de pista é um tipo de competição esportiva, derivada do ciclismo de estrada, porém é disputada em pistas especialmente construídas para esta modalidade conhecidas como velódromo.',
    7: 'Atividades relativas a montar em cavalos.',
    8: 'O futebol de cinco é uma versão do minifutebol, em que cada equipe coloca cinco jogadores. Outras diferenças em relação ao futebol de associação incluem um campo menor, gols menores e uma duração de jogo reduzida.',
    9: 'O golbol é um esporte coletivo com bola, praticado por atletas que possuem deficiência visual. O objetivo do jogo é arremessar uma bola com as mãos de modo a que a bola entre no gol do adversário.',
    10: 'Judô é uma arte marcial japonesa, praticada como esporte de combate. Os seus principais objetivos são fortalecer o físico, a mente e o espírito de forma integrada, além de desenvolver técnicas de defesa pessoal.',
    11: 'O levantamento de peso é um esporte de força consistente em três modalidades: o agachamento, o supino e o levantamento terra.',
    12: 'Remo é um esporte de velocidade, praticado em embarcações estreitas, nas quais os atletas se sentam sobre barcos móveis, de costas voltadas para a proa, usando os braços, tronco e pernas para mover o barco o mais depressa possível, em geral em lagoas, rios, enseadas ou pistas construídas especialmente para a prática da modalidade, mas por vezes também no mar.',
    13: 'Esportes de tiro é a designação genérica do coletivo de atividades ligadas a atividades esportivas, tanto as competitivas como as recreativas. Essas atividades envolvem testes de proficiência, exatidão, precisão e velocidade no "tiro", tanto de curto quanto de longo alcance.',
    14: 'O voleibol paralímpico é uma forma de voleibol para atletas com deficiência. Ao contrário do vôlei em pé, os jogadores de vôlei paralímpico devem se sentar no chão para jogar.',
    15: 'Natação é a capacidade de se deslocar através de movimentos efetuados no meio líquido, geralmente sem ajuda artificial. A natação é uma atividade física que pode ser, de maneira simultânea, útil e recreativa. As suas principais utilizações são recreativas, balneares, pesca, exercício e esporte.',
    16: ' tênis de mesa, também conhecido como pingue-pongue, é o jogo em que duas pessoas ou duplas usam raquetes de madeira para passar uma bolinha de um lado a outro de uma rede instalada em uma mesa. O nome pingue-pongue deve-se ao barulho que a bola faz ao bater na raquete e na mesa.',
    17: 'O taekwondo é uma arte marcial bastante influente na Coréia do Sul. Em coreano, a palavra significa "caminho dos pés e das mãos" através da força da mente e todas as suas atividades estão baseadas em táticas defensivas.',
    18: 'O triatlo é um esporte que combina três modalidades esportivas: atletismo, ciclismo e natação. Em geral, as competições de triatlo começam no meio aquático, mais especificamente no mar. Após esta prova, os atletas montam na bicicleta e percorrem determinada quantidade de quilômetros. Uma vez concluída, os esportistas realizam a parte final da prova correndo até alcançar a meta final.',
    19: 'Basquete em cadeira de rodas são jogos disputados por duas equipes com cinco jogadores cada. A partida é dividida em quatro quartos de 10 minutos cada. A principal diferença em relação ao basquete convencional é que os jogadores devem quicar, arremessar ou passar a bola a cada dois toques dados na cadeira de rodas.',
    20: 'Praticado por pessoas com amputações, lesão medular ou paralisia cerebral, a esgrima em cadeira de rodas é um esporte rápido e tenso, onde os atletas devem usar sua inteligência e raciocínio estratégico para vencer seu adversário, julgando o momento e a quantidade de ataques assim como de movimentos defensivos.',
    21: 'O Rugby em Cadeira de Rodas é disputado em uma quadra de basquete, e a bola é semelhante à do voleibol. Uma partida é disputada em quatro tempos de oito minutos cada. Os atletas podem conduzir a bola sobre as coxas, quicá-la ou passá-la.',
    22: 'O tênis em cadeira de rodas é um esporte paraolímpico praticado por cadeirantes cuja deficiência seja a perda dos membros ou a incapacidade de utilizá-los para locomoção. Utiliza as mesmas quadras do tênis convencional utilizando as mesmas regras com pequenas adaptações.',
    23: 'O tiro com arco é a prática de utilizar um arco e flechas para atingir um alvo.',
    24: 'O basquete é um esporte no qual competem duas equipas constituídas por cinco jogadores cada. O objetivo é acertar com a bola, fazendo com que ela entre dentro dos aros do cesto da equipe adversária.',
    25: 'Tênis é um esporte praticado entre dois oponentes ou duas duplas de oponentes em uma quadra dividida por uma rede, onde os jogadores usam raquetes para rebater uma pequena bola de um lado para o outro.',
    26: 'Método de luta que envolve técnicas de bater, dar pontapés, joelhadas, fazer estrangulamentos e imobilizações, junto com o uso de partes duras do corpo contra pontos vulneráveis do antagonista.'
}

aptitude = {
    "1": "🥇",
    "1.5": "🥇",
    "2": "🥈",
    "2.5": "🥈",
}


def classify_aptitude(value):
    if value not in df['deficiências'].unique():
        return "Value not found in the 'deficiencies' column."
    df_deficiency = df[df['deficiências'] == value]
    df_classification = df_deficiency.groupby('esportes')['aptidão'].mean().reset_index()
    df_classification = df_classification.sort_values('aptidão', ascending=True)
    df_classification = df_classification.reset_index(drop=True)
    # Get only aptitude values 1, 1.5, 2, and 2.5
    df_classification = df_classification[df_classification['aptidão'].isin([1, 1.5, 2, 2.5])]
    result_list = df_classification.values.tolist()

    # Replace aptitude value with aptitude name from the dictionary
    for i in range(len(result_list)):
        for key, aptitude_name in aptitude.items():
            if result_list[i][1] == float(key):
                result_list[i][1] = aptitude_name

    result_dict_list = []
    for item in result_list:
        result_dict_list.append({'name': item[0], 'aptitude': item[1], 'description': description[item[0]]})
    
    # Replace sport ID with sport name from the dictionary
    for item in result_dict_list:
        sport_id = item['name']
        for key, sport_name in sports.items():
            if sport_id == sport_name:
                item['name'] = key


    return result_dict_list
  

def transformRequest(string):
    replaced_string = string.replace('/', ',')
    return replaced_string

@app.route('/getResult/<path:string>', methods=['GET'])
def result(string):
    for value in string.split('/'):
        if value not in ['1','2','3','4','5']:
            return 'Invalid request'
    value = transformRequest(string)
    response = classify_aptitude(value)

    return response

if __name__ == '__main__':
    app.run(debug=True, port=3000)
