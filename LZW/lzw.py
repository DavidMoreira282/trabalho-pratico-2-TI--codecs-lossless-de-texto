import argparse
import os
import pickle

try:
    from tqdm import tqdm
except ImportError as err:
    os.system('pip install -U tqdm')
    from tqdm import tqdm


def compressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}
    resultado = []
    temp = ""

    for i in range(0, tamanhoDicionario):
        dicionario[str(chr(i))] = i

    for c in tqdm(entrada):
        temp2 = temp + str(chr(c))
        if temp2 in dicionario.keys():
            temp = temp2
        else:
            resultado.append(dicionario[temp])
            dicionario[temp2] = tamanhoDicionario
            tamanhoDicionario += 1
            temp = "" + str(chr(c))

    if temp != "":
        resultado.append(dicionario[temp])

    print('Ficheiro Comprimido')
    return resultado


def descompressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}
    resultado = []

    for i in range(0, tamanhoDicionario):
        dicionario[i] = str(chr(i))

    anterior = chr(entrada[0])
    entrada = entrada[1:]
    resultado.append(anterior)

    for bit in tqdm(entrada):
        aux = ""
        if bit in dicionario.keys():
            aux = dicionario[bit]
        else:
            aux = anterior + anterior[0]

        resultado.append(aux)

        dicionario[tamanhoDicionario] = anterior + aux[0]
        tamanhoDicionario += 1
        anterior = aux
    print('Ficheiro Descomprimido')
    return resultado


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compressor e descompressor de texto.')

    parser.add_argument('acao', choices={"encode", "decode"}, help="Definir ação a ser realizada.")
    parser.add_argument('-i', action='store', dest='input', required=True,
                        help='Arquivo de entrada.')
    parser.add_argument('-o', action='store', dest='output', required=True,
                        help='Arquivo de saída.')
    arguments = parser.parse_args()

    ABSOLUTE_PATH = os.getcwd()

    if arguments.acao == 'encode':
        entrada = open(ABSOLUTE_PATH + "//" + arguments.input, "rb").read()
        saida = open(ABSOLUTE_PATH + "//" + arguments.output, "wb")

        comprimido = compressao(entrada)
        pickle.dump(comprimido, saida)
    else:
        entrada = pickle.load(open(ABSOLUTE_PATH + "//" + arguments.input, "rb"))
        saida = open(ABSOLUTE_PATH + "//" + arguments.output, "w")

        descomprimido = descompressao(entrada)
        for l in descomprimido:
            saida.write(l)
        saida.close()
