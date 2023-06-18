import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, o Galaxy A11 é um smartphone Android da Samsung que se destaca pela tela de 6,4 polegadas com resolução HD+, pela bateria de 4.000 mAh com carregamento rápido de 15W e pelo conjunto de três câmeras traseiras, sendo uma principal de 13 MP, uma ultra wide de 5 MP e uma de profundidade de 2 MP. A câmera frontal é de 8 MP e fica dentro da tela em um furo.{os.linesep}O Galaxy A11 tem duas versões, uma com 2 GB de memória RAM e outra com 3 GB, ambas com 32 GB de armazenamento interno, expansível até 512 GB com cartão microSD. O processador é um octa-core de 1,8 GHz, que pode variar conforme o mercado. O sistema operacional é o Android 10 com a interface One UI 2.0 da Samsung.{os.linesep}O Galaxy A11 é um smartphone básico, indicado para quem procura um aparelho simples, mas com alguns recursos interessantes, como o leitor de digitais na parte traseira, o carregador rápido e as câmeras versáteis. No entanto, ele também tem algumas limitações, como a resolução da tela, que poderia ser melhor, o desempenho modesto, que pode não rodar alguns aplicativos mais pesados, e a qualidade das fotos, que pode variar conforme a iluminação.{os.linesep}O Galaxy A11 foi lançado no Brasil em junho de 2020 pelo preço sugerido de R$ 1.699 na versão com 3 GB de RAM. Atualmente, ele pode ser encontrado por cerca de R$ 900 em algumas lojas online. Vale a pena comparar o custo-benefício do Galaxy A11 com outros modelos da mesma faixa de preço ou da mesma linha Galaxy A da Samsung.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, a bateria do Galaxy A11 tem uma capacidade de 4.000 mAh, o que pode oferecer uma boa autonomia, dependendo do uso do smartphone. Em condições normais, a bateria pode durar um dia inteiro com uso moderado. No entanto, a duração da bateria pode variar dependendo das configurações de brilho da tela, uso de aplicativos mais exigentes e outros fatores. Recomenda-se também fechar os aplicativos em segundo plano e otimizar o uso de energia para obter a melhor duração possível da bateria.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, os requisitos mais visados pelos clientes na hora de comprar um celular podem variar de acordo com as necessidades individuais de cada pessoa. No entanto, alguns requisitos comuns são:{os.linesep}- Desempenho: um processador rápido e memória suficiente para executar os aplicativos e jogos desejados sem problemas de desempenho.{os.linesep}- Tela: tamanho adequado, resolução de qualidade e recursos como taxa de atualização alta ou tecnologia HDR.{os.linesep}- Câmera: qualidade das câmeras traseiras e frontais para tirar fotos e gravar vídeos de boa qualidade.{os.linesep}- Bateria: capacidade suficiente para durar o dia todo com uso moderado.{os.linesep}- Armazenamento: espaço de armazenamento interno suficiente para aplicativos, fotos, vídeos e outros arquivos.{os.linesep}- Sistema operacional: preferência por um sistema operacional específico, como Android ou iOS.{os.linesep}- Design e construção: design atraente, construção robusta e materiais de qualidade.{os.linesep}- Preço: adequação ao orçamento do cliente.{os.linesep}Esses são apenas alguns dos requisitos mais comuns, mas cada pessoa pode ter prioridades diferentes ao escolher um celular.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, sim, é possível encontrar descontos na loja online da Samsung para o Galaxy A11. A loja oferece diversas promoções ao longo do ano, então é recomendado verificar o site oficial da Samsung para conferir as ofertas atualizadas. Além disso, também é possível encontrar o Galaxy A11 com desconto em outras lojas online e físicas que vendem produtos Samsung. Certifique-se de comparar os preços e as condições de compra antes de tomar uma decisão.{os.linesep}')
    else:
        print(f'{os.linesep}Desculpe, não entendi sua pergunta. Por favor, escolha uma opção válida.{os.linesep}')

def start():
    # Apresentar o chatbot    
    print('Olá! Bem-vindo à nossa plataforma!')

    # Pedir o nome
    nome = input('Digite seu nome: ')

    while True:
        # Oferecer menu de opções
        resposta = input(f'O que gostaria de saber hoje, {nome}?{os.linesep}[1] - Vale a pena comprar um Galaxy A11?{os.linesep}[2] - A bateria do Galaxy A11 dura bastante?{os.linesep}[3] - Quais são os requisitos mais visados pelos clientes na hora de comprar um celular?{os.linesep}[4] - Tem desconto na loja Samsung?{os.linesep}Escolha uma opção (1, 2, 3 ou 4), ou digite "sair" para encerrar: ')

        if resposta.lower() == 'sair':
            break

        # Processar a resposta enviada 
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, o Galaxy A11 é um smartphone Android da Samsung que se destaca pela tela de 6,4 polegadas com resolução HD+, pela bateria de 4.000 mAh com carregamento rápido de 15W e pelo conjunto de três câmeras traseiras, sendo uma principal de 13 MP, uma ultra wide de 5 MP e uma de profundidade de 2 MP. A câmera frontal é de 8 MP e fica dentro da tela em um furo.{os.linesep}O Galaxy A11 tem duas versões, uma com 2 GB de memória RAM e outra com 3 GB, ambas com 32 GB de armazenamento interno, expansível até 512 GB com cartão microSD. O processador é um octa-core de 1,8 GHz, que pode variar conforme o mercado. O sistema operacional é o Android 10 com a interface One UI 2.0 da Samsung.{os.linesep}O Galaxy A11 é um smartphone básico, indicado para quem procura um aparelho simples, mas com alguns recursos interessantes, como o leitor de digitais na parte traseira, o carregador rápido e as câmeras versáteis. No entanto, ele também tem algumas limitações, como a resolução da tela, que poderia ser melhor, o desempenho modesto, que pode não rodar alguns aplicativos mais pesados, e a qualidade das fotos, que pode variar conforme a iluminação.{os.linesep}O Galaxy A11 foi lançado no Brasil em junho de 2020 pelo preço sugerido de R$ 1.699 na versão com 3 GB de RAM. Atualmente, ele pode ser encontrado por cerca de R$ 900 em algumas lojas online. Vale a pena comparar o custo-benefício do Galaxy A11 com outros modelos da mesma faixa de preço ou da mesma linha Galaxy A da Samsung.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, a bateria do Galaxy A11 tem uma capacidade de 4.000 mAh, o que pode oferecer uma boa autonomia, dependendo do uso do smartphone. Em condições normais, a bateria pode durar um dia inteiro com uso moderado. No entanto, a duração da bateria pode variar dependendo das configurações de brilho da tela, uso de aplicativos mais exigentes e outros fatores. Recomenda-se também fechar os aplicativos em segundo plano e otimizar o uso de energia para obter a melhor duração possível da bateria.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, os requisitos mais visados pelos clientes na hora de comprar um celular podem variar de acordo com as necessidades individuais de cada pessoa. No entanto, alguns requisitos comuns são:{os.linesep}- Desempenho: um processador rápido e memória suficiente para executar os aplicativos e jogos desejados sem problemas de desempenho.{os.linesep}- Tela: tamanho adequado, resolução de qualidade e recursos como taxa de atualização alta ou tecnologia HDR.{os.linesep}- Câmera: qualidade das câmeras traseiras e frontais para tirar fotos e gravar vídeos de boa qualidade.{os.linesep}- Bateria: capacidade suficiente para durar o dia todo com uso moderado.{os.linesep}- Armazenamento: espaço de armazenamento interno suficiente para aplicativos, fotos, vídeos e outros arquivos.{os.linesep}- Sistema operacional: preferência por um sistema operacional específico, como Android ou iOS.{os.linesep}- Design e construção: design atraente, construção robusta e materiais de qualidade.{os.linesep}- Preço: adequação ao orçamento do cliente.{os.linesep}Esses são apenas alguns dos requisitos mais comuns, mas cada pessoa pode ter prioridades diferentes ao escolher um celular.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, sim, é possível encontrar descontos na loja online da Samsung para o Galaxy A11. A loja oferece diversas promoções ao longo do ano, então é recomendado verificar o site oficial da Samsung para conferir as ofertas atualizadas. Além disso, também é possível encontrar o Galaxy A11 com desconto em outras lojas online e físicas que vendem produtos Samsung. Certifique-se de comparar os preços e as condições de compra antes de tomar uma decisão.{os.linesep}')
    else:
        print(f'{os.linesep}Desculpe, não entendi sua pergunta. Por favor, escolha uma opção válida.{os.linesep}')

def start():
    # Apresentar o chatbot    
    print('Olá! Bem-vindo à nossa plataforma!')

    # Pedir o nome
    nome = input('Digite seu nome: ')

    while True:
        # Oferecer menu de opções
        resposta = input(f'O que gostaria de saber hoje, {nome}?{os.linesep}[1] - Vale a pena comprar um Galaxy A11?{os.linesep}[2] - A bateria do Galaxy A11 dura bastante?{os.linesep}[3] - Quais são os requisitos mais visados pelos clientes na hora de comprar um celular?{os.linesep}[4] - Tem desconto na loja Samsung?{os.linesep}Escolha uma opção (1, 2, 3 ou 4), ou digite "sair" para encerrar: ')

        if resposta.lower() == 'sair':
            break

        # Processar a resposta enviada 
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
