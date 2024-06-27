# Add depois 
#variavel peso
# usar no sistema for ------- 1º pessoa ----- pra separar cada uma que for criada.
#Bibliotecas
import random
import time

      
nomes_masculinos = ["Caetano","Marcelo","Rafael","Miguel","Eduardo","Bartolomeu","Pedro","João", "José", "Antônio", "Luiz", "Carlos", "Paulo", "Pedro", "Lucas", "Gabriel", "Marcos", "André", "Rafael", "Leonardo", "Gustavo", "Marcelo", "Daniel", "Rodrigo", "Eduardo", "Felipe", "Bruno", "Diego", "Fernando", "Thiago", "Alexandre", "Ricardo", "Samuel", "Vinícius", "Matheus", "Roberto", "Lucas", "Fabio", "Guilherme", "Igor", "Caio", "Miguel", "William", "Renato", "Arthur", "Renan", "Alan", "Victor", "Lucas", "Sérgio", "Raul", "Fernando", "Enzo", "Nathan", "Junior", "Cesar", "Levi"]

nomes_femininos = ["Laura","Joana","Diana","Rafaela","Tayna","Vitoria","Fernanda","Eduarda","Barbara","Maria", "Ana", "Francisca", "Antônia", "Juliana", "Mariana", "Adriana", "Roberta", "Patrícia", "Camila", "Fernanda", "Isabela", "Larissa", "Letícia", "Vanessa", "Aline", "Amanda", "Bruna", "Carolina", "Daniela", "Elisa", "Flávia", "Gisele", "Heloísa", "Ingrid", "Jéssica", "Karina", "Lívia", "Márcia", "Natália", "Priscila", "Rafaela", "Sabrina", "Taís", "Valéria", "Vivian", "Yara", "Zara", "Alice", "Bárbara", "Cláudia", "Débora", "Erika", "Fabiana", "Gabriela", "Helena", "Inês", "Júlia", "Kelly"]

sobrenomes1 = ["de Oliveira","Cardoso","Silva","Mendes"," dos Santos","Dias","Barbosa","Cunha","Siqueira","Boarque"]

sobrenomes2 = ["Pereira","Barros","Melo","Andrade","Alves","Batista","Borges","de Campos","Carvalho","de Castro"]

regiao = ["Sul","Norte","Leste","Oeste"]

paises = ["da Africa do Sul", "da Guiné", "da Argelia","da Angola","da Somalia","de Mali","da India", "da Libia", "de Madadascar", "do Sudão", "da Nigeria", "da Tazânia", "do Canada", "do Mexico","do Brasil", "da Argentina", "das Bahamas", "de Honduras", "do Panamá", "da Guiana", "do Paraguai"]

ambientes = ["zona rural","zona urbana"]

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

crença_h = ["Cristão", "Muçulmano", "Hinduísta", "Budista", "Sikhista", "Judeu", "Espirita", "Bahaísta", "Xintoísta", "Zoroastrista","Ateista"]

crença_m = ["Cristã", "Muçulmana", "Hinduísta", "Budista", "Sikhista", "Judia", "Espirita", "Bahaísta", "Xintoísta", "Zoroastrista","Ateista"]


corrente = ["ao idealismo","ao materialismo","a escolástica","ao racionalismo","ao empirismo","ao pragmatismo","ao existencialismo","ao pós-modernismo","ao psicologismo","ao neocriticismo","ao metafísica"]

artes = ["o expressionismo","o fauvismo","o cubismo","o abstracionismo ","o futurismo","o dadaísmo","o surrealismo","a op art","a pop Art","a renascença italiana","o barroco ","o impressionismo","o pós-impressionismo","o expressionismo abstrato","o pós-modernismo"]
 
artistas_plastico = ["Leonardo da Vinci","Michelangelo Buonarroti","Pablo Picasso","Vincent van Gogh","Rembrandt van Rijn","Claude Monet","Salvador Dalí","Johannes Vermeer","Andy Warhol","Sandro Botticelli","Francisco de Goya","Jackson Pollock","Raphael","Henri Matisse","Edvard Munch","Caravaggio","Paul Cézanne","Wassily Kandinsky","Gustav Klimt","Frida Kahlo","Georgia O'Keeffe","Marc Chagall","Diego Rivera","Joan Miró","Edgar Degas","Roy Lichtenstein","Edward Hopper","Peter Paul Rubens","Willem de Kooning","Paul Gauguin","Mark Rothko","Jean-Michel Basquiat","Tintoretto","William Turner","Alberto Giacometti","Artemisia Gentileschi","Alberto Burri","Lucian Freud","El Greco","Pierre-Auguste Renoir","Giorgio de Chirico","Joan Brown","Jean Dubuffet","Auguste Rodin","Anselm Kiefer","David Hockney","Louise Bourgeois","Man Ray","Paul Klee","Fernand Léger","Jasper Johns","Max Ernst","Francis Bacon","Amedeo Modigliani","Camille Pissarro","Marcel Duchamp","Yayoi Kusama","Takashi Murakami","Cy Twombly","Agnes Martin","Frida Baranek","Betye Saar","Vasily Kandinsky","Robert Rauschenberg","Berthe Morisot","Édouard Manet","Mary Cassatt","Berenice Abbott","Banksy","Victor Vasarely","Yves Klein","Chuck Close","AlexanderCalder","Giorgio Morandi","Pierre Bonnard","Jean-Baptiste-Siméon Chardin","David Smith","Jean-Paul Riopelle","Lee Krasner","Helen Frankenthaler","Sol LeWitt","Helen Chadwick","Peter Blake","Richard Hamilton","Joseph Beuys","Thomas Hart Benton","Cindy Sherman","Frank Stella","Jeff Koons","Marina Abramović","Louise Nevelson","Niki de Saint Phalle","Marcel Broodthaers","Donald Judd","Ellsworth Kelly","Fernand Khnopff","George Grosz","Salvador Allende","Camille Claudel","Nancy Spero"]

obra_plastica = ["Mona Lisa de Leonardo da Vinci", "A Última Ceia de Leonardo da Vinci", "Guernica de Pablo Picasso", "Noite Estrelada de Vincent van Gogh", "O Grito de Edvard Munch", "A Ronda Noturna de Rembrandt", "Nascimento de Vênus de Sandro Botticelli", "O Beijo de Gustav Klimt", "A Criação de Adão de Michelangelo", "Les Demoiselles d'Avignon de Pablo Picasso", "A Persistência da Memória de Salvador Dalí", "O Nascimento de Vênus de Sandro Botticelli", "A Primavera de Sandro Botticelli", "O Pensador de Auguste Rodin", "David de Michelangelo", "O Quarto em Arles de Vincent van Gogh", "Vitruvian Man de Leonardo da Vinci", "Três Estudos para Figuras no Pé de Cristo de Francis Bacon", "Retrato de Adele BlochdeBauer I de Gustav Klimt", "O Grito do Anjo de Paul Klee", "A Mulher Chorando de Pablo Picasso", "A Noite Estrelada sobre o Ródano de Vincent van Gogh", "Composição VIII de Wassily Kandinsky", "Les Nymphéas de Claude Monet", "O Nascimento de Vênus de Alexandre Cabanel", "Ponto de Ignição de Philip Guston", "O Grande Nude Descendo a Escada de Marcel Duchamp", "Broadway Boogie Woogie de Piet Mondrian", "A Persistência da Memória de Salvador Dalí", "A Última Ceia de Tintoretto", "A Casa do Guarda de Paul Cézanne", "O Chafariz de Marcel Duchamp", "O Pensador de Auguste Rodin", "A Lua de Mel de René Magritte", "O Amor e a Morte de Gustav Klimt", "Dora Maar com Gato de Pablo Picasso", "Arranjo em Cinza e Preto nº 1 de James Abbott McNeill Whistler", "A Noite Estrelada de Wassily Kandinsky", "Les Demoiselles d'Avignon de Pablo Picasso", "O Grito de Edvard Munch", "A Cabeça de Medusa de Peter Paul Rubens", "O Raft dos Medusa de Théodore Géricault", "Lavando os Pés dos Apóstolos de Ford Madox Brown", "A Virgem do Rosário de Bartolomé Esteban Murillo", "O Êxtase de Santa Teresa de Gian Lorenzo Bernini", "Cabeça de Mulher (Fernande) de Pablo Picasso", "Mulher com um Vaso de Flores de Pablo Picasso", "Guernica de Pablo Picasso", "A Cabeça de Medusa de Caravaggio", "Retrato de Dora Maar de Pablo Picasso", "O Desespero do Homem de Gustave Courbet", "A Liberdade Guiando o Povo de Eugène Delacroix", "A Sesta de Paul Gauguin", "O Pintor e sua Modelo de Pablo Picasso", "O Quadro Negro de René Magritte", "A Bela Princesa de Gustav Klimt", "Homem com um Gorro de Veludo de Raphael", "Mulheres de Argel de Eugène Delacroix", "Autorretrato com Gorro de Feltro de Vincent van Gogh", "Amantes de René Magritte", "A Filha do Pescador de Jules Breton", "O Assassinato de Marat de JacquesdeLouis David", "Retrato de Madame X de John Singer Sargent", "A Banhista de JeandeAugustedeDominique Ingres", "Ninféias de Claude Monet", "Banhistas de Paul Cézanne", "Autorretrato de Rembrandt", "Guernica de Pablo Picasso", "A Estrela Noturna de Vincent van Gogh", "O Nascimento de Vênus de WilliamdeAdolphe Bouguereau", "Retrato de Sir Thomas More de Hans Holbein, o Jovem", "O Jardim das Delícias Terrenas de Hieronymus Bosch", "O Julgamento Final de Michelangelo", "A Última Ceia de Ticiano", "A Última Ceia de Peter Paul Rubens", "A Queda dos Anjos Rebeldes de Pieter Bruegel, o Velho", "O Homem do Nariz Quebrado de Salvador Dalí", "Retrato de Adele BlochdeBauer II de Gustav Klimt", "O Jardim das Delícias Terrenas de Hieronymus Bosch", "A Ronda Noturna de Rembrandt", "O Sonho de Henri Rousseau", "A Caminho do Paraíso de Giovanni Bellini", "Retrato de Madame Recamier de JacquesdeLouis David","O Grito de Edvard Munch", "O Sonho de Pablo Picasso", "As Meninas de Diego Velázquez", "A Perspectiva de Pietro Perugino", "A Última Ceia de Jacopo Tintoretto","O Beijo de Auguste Rodin"]

livro_favorito = ["A Divina Comédia de Dante Alighieri", "A Odisséia de Homero", "A Ilíada de Homero", "Dom Quixote de Miguel de Cervantes", "Hamlet de William Shakespeare", "1984 de George Orwell", "Orgulho e Preconceito de Jane Austen", "Guerra e Paz de Lev Tolstói", "Crime e Castigo de Fiódor Dostoiévski", "O Processo de Franz Kafka", "Ulisses de James Joyce", "Moby Dick de Herman Melville", "O Príncipe de Nicolau Maquiavel", "As Vinhas da Ira de John Steinbeck", "O Retrato de Dorian Gray de Oscar Wilde", "Cem Anos de Solidão de Gabriel García Márquez", "Em Busca do Tempo Perdido de Marcel Proust", "Os Irmãos Karamazov de Fiódor Dostoiévski", "A Metamorfose de Franz Kafka", "Odisseia de Homero", "A Revolução dos Bichos de George Orwell", "O Grande Gatsby de F. Scott Fitzgerald", "O Apanhador no Campo de Centeio de J.D. Salinger", "O Vermelho e o Negro de Stendhal", "O Estrangeiro de Albert Camus", "O Nome da Rosa de Umberto Eco", "Meditações de Marco Aurélio", "O Leão, a Feiticeira e o GuardadeRoupa de C.S. Lewis", "A Metamorfose de Ovídio", "O Conde de Monte Cristo de Alexandre Dumas", "Os Miseráveis de Victor Hugo", "As Crônicas de Nárnia de C.S. Lewis", "Maus de Art Spiegelman", "Os Três Mosqueteiros de Alexandre Dumas", "O Guia do Mochileiro das Galáxias de Douglas Adams", "O Amor nos Tempos do Cólera de Gabriel García Márquez", "O Poder do Hábito de Charles Duhigg", "O Código Da Vinci de Dan Brown", "O Hobbit de J.R.R. Tolkien", "O Senhor dos Anéis de J.R.R. Tolkien", "O Alquimista de Paulo Coelho", "Paraíso Perdido de John Milton", "A Vida de Pi de Yann Martel", "O Pequeno Príncipe de Antoine de SaintdeExupéry", "O Médico e o Monstro de Robert Louis Stevenson", "A Cabana de William P. Young", "O Mundo de Sofia de Jostein Gaarder", "As Aventuras de Sherlock Holmes de Arthur Conan Doyle", "O Silmarillion de J.R.R. Tolkien", "Os Lusíadas de Luís de Camões", "O Sol é para Todos de Harper Lee", "O Morro dos Ventos Uivantes de Emily Brontë", "O Retrato de Dorian Gray de Oscar Wilde", "Moby Dick de Herman Melville", "O Velho e o Mar de Ernest Hemingway", "Guerra e Paz de Lev Tolstói", "Anna Karenina de Lev Tolstói"]


musicas = ["Bohemian Rhapsody - Queen", "Imagine - John Lennon", "Hey Jude - The Beatles", "Like a Rolling Stone - Bob Dylan", "Stairway to Heaven - Led Zeppelin", "Thriller - Michael Jackson", "Smells Like Teen Spirit - Nirvana", "Hotel California - Eagles", "Billie Jean - Michael Jackson", "Yesterday - The Beatles", "Wonderwall - Oasis", "Sweet Child o' Mine - Guns N' Roses", "I Will Always Love You - Whitney Houston", "Hallelujah - Leonard Cohen", "What a Wonderful World - Louis Armstrong", "Let It Be - The Beatles", "My Way - Frank Sinatra", "Rolling in the Deep - Adele", "Hound Dog - Elvis Presley", "Somewhere Over the Rainbow - Judy Garland", "Another Brick in the Wall - Pink Floyd", "Piano Man - Billy Joel", "Respect - Aretha Franklin", "Johnny B. Goode - Chuck Berry", "Every Breath You Take - The Police", "Unchained Melody - Righteous Brothers", "Brown Eyed Girl - Van Morrison", "Livin' on a Prayer - Bon Jovi", "Don't Stop Believin' - Journey", "Dancing Queen - ABBA", "Tutti Frutti - Little Richard", "Sweet Caroline - Neil Diamond", "Let's Stay Together - Al Green", "Good Vibrations - The Beach Boys", "My Girl - The Temptations", "Bridge Over Troubled Water - Simon & Garfunkel", "I Want to Hold Your Hand - The Beatles", "A Day in the Life - The Beatles", "Space Oddity - David Bowie", "I Heard It Through the Grapevine - Marvin Gaye", "Every Breath You Take - The Police", "I Heard It Through the Grapevine - Marvin Gaye", "Don't Stop Believin' - Journey", "Hey Jude - The Beatles", "Brown Eyed Girl - Van Morrison", "Billie Jean - Michael Jackson", "Hotel California - Eagles", "Piano Man - Billy Joel", "Sweet Child o' Mine - Guns N' Roses", "Imagine - John Lennon", "Smells Like Teen Spirit - Nirvana", "Hallelujah - Leonard Cohen", "What a Wonderful World - Louis Armstrong", "Hey Jude - The Beatles", "Yesterday - The Beatles", "Stairway to Heaven - Led Zeppelin", "Wonderwall - Oasis", "Thriller - Michael Jackson", "Another Brick in the Wall - Pink Floyd", "Hotel California - Eagles", "Bohemian Rhapsody - Queen", "Let It Be - The Beatles", "My Way - Frank Sinatra", "Like a Rolling Stone - Bob Dylan", "I Will Always Love You - Whitney Houston", "Rolling in the Deep - Adele", "Sweet Child o' Mine - Guns N' Roses", "Hound Dog - Elvis Presley", "Respect - Aretha Franklin", "Every Breath You Take - The Police", "Unchained Melody - Righteous Brothers", "Thriller - Michael Jackson", "Imagine - John Lennon", "Don't Stop Believin' - Journey", "Dancing Queen - ABBA", "Tutti Frutti - Little Richard", "Brown Eyed Girl - Van Morrison", "Bohemian Rhapsody - Queen", "Let's Stay Together - Al Green", "Livin' on a Prayer - Bon Jovi", "My Girl - The Temptations", "Another Brick in the Wall - Pink Floyd", "Sweet Caroline - Neil Diamond", "Good Vibrations - The Beach Boys", "Like a Rolling Stone - Bob Dylan", "What a Wonderful World - Louis Armstrong", "Wonderwall - Oasis", "Space Oddity - David Bowie", "Yesterday - The Beatles", "Hey Jude - The Beatles", "Hotel California - Eagles", "Smells Like Teen Spirit - Nirvana", "I Will Always Love You - Whitney Houston", "Rolling in the Deep - Adele", "Sweet Child o' Mine - Guns N' Roses", "Hallelujah - Leonard Cohen", "Respect - Aretha Franklin", "Every Breath You Take - The Police", "Bohemian Rhapsody - Queen", "Thriller - Michael Jackson", "Imagine - John Lennon", "Let It Be - The Beatles", "Billie Jean - Michael Jackson", "Don't Stop Believin' - Journey", "Another Brick in the Wall - Pink Floyd", "Like a Rolling Stone - Bob Dylan", "Hey Jude - The Beatles", "Wonderwall - Oasis", "Hound Dog - Elvis Presley", "Piano Man - Billy Joel", "Brown Eyed Girl - Van Morrison", "Garota de Ipanema - Tom Jobim e Vinícius de Moraes", "Construção - Chico Buarque", "Asa Branca - Luiz Gonzaga e Humberto Teixeira", "Águas de Março - Tom Jobim", "Carinhoso - Pixinguinha e João de Barro", "Trem das Onze - Adoniran Barbosa", "Aquarela do Brasil - Ary Barroso", "Romaria - Renato Teixeira", "Cálice - Chico Buarque e Gilberto Gil", "O Bêbado e a Equilibrista - Aldir Blanc e João Bosco", "Canto de Ossanha - Baden Powell e Vinícius de Moraes", "Eu Sei que Vou te Amar - Tom Jobim e Vinícius de Moraes", "Disparada - Geraldo Vandré e Théo de Barros", "Roda Viva - Chico Buarque"]

personalidade1 = ["alegre","triste","calorosa","antipatica","odiosa","malefica","bondosa","amorosa","fragil","instavel","temperamental","fria","calculista"]
personalidade2 = ["alegre","triste","calorosa","antipatica","odiosa","malefica","bondosa","amorosa","fragil","instavel","temperamental","fria","calculista"]
peles = ["negra","branca","parda"]

queimadas = [", queimada do sol, sua pele tem um brilho quente",", não é queimada pelo sol, sua pele tem um tom frio"]

cabelos = ["crespos","ondulados","cacheados"]

volume_cabelos = ["bastante volumosos"," pouco volumosos"]

cor_cabelos = ["rosa","verde","branco","azul","vermelho","amarelo","castanho","preto","loiro"]

tamanho = ["longas","curtas","medias","longas e coloridas","curtas e coloridas","medias e coloridas","longas e com pontas coloridas","curtas e com pontas coloridas", "medias e com pontas coloridas"]

olhos = ["azuis","castanhos","verdes","cinzas","heterocromaticos em tons de azul e verde","heterocromaticos em tons de azul e castanho","heterocromaticos em tons de castanho e verde"]

corpos = ["corpo bem delineado, cheio de musculos","corpo grande, definido, cheio de curvas","corpo esguio" ]




print('Escolha um das opções.\n 1- Homem\n 2- Mulher\n 3- Encerrar\n')

escolha = input('Digite o numero correspondente a opção: ')
while escolha not in '3':
    
    if escolha == "1": 
        num_homem = int(input("\nQuantas homens deseja criar? "))
        for c in range(1,num_homem + 1):
            nome_masculino = random.choice(nomes_masculinos)
            sobrenome1 = random.choice(sobrenomes1)
            sobrenome2 = random.choice(sobrenomes2)

            zona = random.choice(ambientes)
            cardial = random.choice(regiao)
            pais = random.choice(paises)

            vida = random.randint(9,100)
            dia = random.randint(1,28)
            mes = random.choice(meses)
            ano_nascimento = random.randint(1900,3000)

            credoh = random.choice(crença_m)
            filos = random.choice(corrente)
            persona1 = random.choice(personalidade1)
            persona2 = random.choice(personalidade2)

            movimento_artistico = random.choice(artes)
            artista = random.choice(artistas_plastico)
            obra = random.choice(obra_plastica)
            musica = random.choice(musicas)
            livro = random.choice(livro_favorito)
        

            pele = random.choice(peles)
            queimada = random.choice(queimadas)
            cabelo = random.choice(cabelos)
            volume = random.choice(volume_cabelos)
            cor_cabelo = random.choice(cor_cabelos)
            madeixas = random.choice(tamanho)
            olho = random.choice(olhos)
            altura = random.uniform(1.60,2.05)
            corpo = random.choice(corpos)
            print('\n------- {}º pessoa -----'. format(c))
            homi = str('{} {} {},nascido na {} da região {} {}, no dia {} do mes de {} do ano de {}, possui {} anos.\n{}, porem com fortes tendencias {}.\nPossui uma personalidade {}, se considera uma pessoa {}.\nAmante de arte, sendo {} seu movimento artistico mais admirado.\nPossui um fascínio por {}.\nTambém é um grande amante das belas artes.\nSendo que seu livro, música e obra plástica favoritos são respectivamente {}, {} e {}.\nPossui a pele {}{}, seus cabelos são {}, {}, seu cabelo é {}, possuindo madeixas {}, seus olhos são {} que mais se parecem com minerais, possui {:.3} de altura e um {}.'.format(nome_masculino, sobrenome1, sobrenome2,zona, cardial,pais, dia, mes, ano_nascimento,vida,credoh,filos, persona1, persona2,movimento_artistico, artista, livro, musica, obra,pele, queimada, cabelo, volume, cor_cabelo, madeixas, olho, altura,corpo))
            print('\n{}'.format(homi))
        
        
    elif escolha == "2": 
        num_mulher = int(input("Quantas mulheres deseja criar?"))
        for _ in range(num_mulher):
            nome_feminino = random.choice(nomes_femininos)
            sobrenome1 = random.choice(sobrenomes1)
            sobrenome2 = random.choice(sobrenomes2)

            zona = random.choice(ambientes)
            cardial = random.choice(regiao)
            pais = random.choice(paises)

            vida = random.randint(9,100)
            dia = random.randint(1,28)
            mes = random.choice(meses)
            ano_nascimento = random.randint(1900,3000)

            credom = random.choice(crença_m)
            filos = random.choice(corrente)
            persona1 = random.choice(personalidade1)
            persona2 = random.choice(personalidade2)

            movimento_artistico = random.choice(artes)
            artista = random.choice(artistas_plastico)
            obra = random.choice(obra_plastica)
            musica = random.choice(musicas)
            livro = random.choice(livro_favorito)


            pele = random.choice(peles)
            queimada = random.choice(queimadas)
            cabelo = random.choice(cabelos)
            volume = random.choice(volume_cabelos)
            cor_cabelo = random.choice(cor_cabelos)
            madeixas = random.choice(tamanho)
            olho = random.choice(olhos)
            altura = random.uniform(1.40,1.80)
            corpo = random.choice(corpos)

            muie = str('{} {} {},nascida na {} da região {} {}, no dia {} do mes {} do ano de {}, possui {} anos.\n{}, porem com fortes tendencias {}.\nPossui uma personalidade {}, se considera uma pessoa {}.\nAmante de arte, sendo {} seu movimento artistico mais admirado.\nPossui um fascínio por {}.\nTambém é uma grande amante das belas artes.\nSendo que seu livro, música e obra plástica favoritos são respectivamente {}, {} e {}.\nPossui a pele {}{}, seus cabelos são {}, {}, seu cabelo é {}, possuindo madeixas {}, seus olhos são {} que mais se parecem com minerais, possui {:.3} de altura e um {}./'.format(nome_feminino, sobrenome1, sobrenome2,zona, cardial,pais, dia, mes, ano_nascimento,vida,credom,filos, persona1, persona2,movimento_artistico, artista, livro, musica, obra,pele, queimada, cabelo, volume, cor_cabelo, madeixas, olho, altura,corpo))
            print('\n{}'.format(muie))

    else:
        print('Obrigado por utilizar o software.\n')
        exit()
    




