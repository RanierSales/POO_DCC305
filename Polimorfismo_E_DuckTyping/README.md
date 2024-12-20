## Exercício Avaliativo 02 - Polimorfismo e Duck Typing

### Parte 01 - Polimorfismo "tradicional"

* Imagine que você está desenvolvendo um sistema de simulação para um zoológico virtual. Todos os animais do zoológico devem ser capazes de emitir um som característico.

    * Crie uma classe base chamada Animal com um método chamado emitir_som() (não implemente nada dentro deste método).
    * Crie pelo menos três classes que herdam de Animal (Cachorro, Gato, Leao) e implementam o método emitir_som() com sons diferentes, como "Au au", "Miau" e "Rugido", respectivamente.
    * Crie uma lista de instâncias dessas classes e use um loop para chamar o método emitir_som() para cada animal.
    * Mostre a saída esperada do programa.

####  Perguntas:
1. Explique como o polimorfismo ajuda a manter o código flexível e reutilizável neste exemplo.
2. O que aconteceria se você tentasse criar uma instância da classe Animal diretamente?
    
### Parte 02 - Polimorfismo do python - duck typing

* Você está desenvolvendo um jogo onde personagens podem realizar ações diferentes. Nem todos os personagens precisam ser da mesma classe, mas devem saber executar as ações básicas esperadas pelo jogo.

* Crie três classes (Cavaleiro, Mago, Dragao) e implemente um método atacar() em cada uma, com descrições diferentes (ex.: "O cavaleiro ataca com sua espada").
* Crie uma função chamada executar_ataque(lista_de_personagens) que recebe uma lista de objetos e chama o método atacar() de cada um.
* Teste a função com instâncias das três classes diferentes.

####  Perguntas:

3. Explique por que o método atacar() não precisa estar definido em uma classe base neste caso.
4. O que aconteceria se você passasse um objeto que não possui o método atacar() na lista para a função executar_ataque()?

### Parte 03

Você está desenvolvendo um sistema de combate para um jogo de RPG. No jogo, existem diversos tipos de personagens e criaturas, cada um **com habilidades e formas de ataque únicas**. Esses personagens podem atacar uns aos outros e interagir com elementos do cenário. Além disso, alguns elementos do cenário (como armadilhas) podem causar dano. Seu objetivo é modelar o sistema com os seguintes requisitos:

* Crie uma classe base chamada Entidade:
    * Cada entidade deve ter um atributo vida inicial (ex.: 100 para personagens e 50 para armadilhas).
    * Deve possuir um método acao() que será implementado de forma diferente para cada tipo de entidade. O método acao() de uma entidade deve permitir que ela ataque outra entidade, reduzindo sua vida.
    * Crie pelo menos 4 subclasses ou classes independentes que representam entidades diferentes:
        * Guerreiro: realiza ataques corpo a corpo, causando 10 pontos de dano.
        * Mago: realiza ataques mágicos, causando 15 pontos de dano.
        * Dragao: cospe fogo, causando 20 pontos de dano.
        * Armadilha: é um objeto do cenário que, quando ativado, causa 5 pontos de dano.

* Crie uma classe chamada Combate
    * Deve ter um atributo de classe que é uma lista das entidades que irão participar do combate.
    * Deve ter o método simular_combate.
        Para cada entidade na lista de entidades, chama o método acao() e imprime o resultado no console.
    * Deve ter um método chamado add_entidade para adicianar entidades para o combate;
        * Esse método recebe uma instância de uma entidade (como Guerreiros, Magos, Dragões ou Armadilhas).
    * Crie um método da classe Combate que atualize a função simular_combate para que o combate continue enquanto pelo menos duas entidades ainda tiverem vida maior que zero.
    
##### Exemplo de saída (parcial e hipotética) esperada:

* O Guerreiro realiza um ataque corpo a corpo, causando 10 de dano!
* O Mago lança uma magia poderosa, causando 15 de dano!
* O Dragão cospe fogo, causando 20 de dano!
* A Armadilha é ativada, causando 5 de dano!

####  Perguntas:

5. Explique como o uso de polimorfismo simplifica a implementação da função simular_combate.
6. Em que situações o duck typing pode causar erros neste sistema? Como você evitaria esses erros?
7. Qual seria a vantagem de usar classes base versus deixar as classes independentes e confiar no duck typing?
