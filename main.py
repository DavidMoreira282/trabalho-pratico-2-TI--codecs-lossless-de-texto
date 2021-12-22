import os
import pickle
from time import sleep
from LZW import lzw
from Huffman.huffman import HuffmanCoding
from RLE import rle

try:
    from art import *
except ImportError as err:
    os.system('pip install art')
    from art import *


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print("Selecione o metodo de compressão/decompressão: ")
    print("\t1 - Lempel-Ziv-Welch")
    print("\t2 - Huffman Coding")
    print("\t3 - Run Length Coding")
    print("\t0 - Sair")
    return input(f"\t>> ")


def lzwCoding():
    sleep(1)
    clear()
    tprint("LZW")
    file_name = input("Nome do ficheiro: ")
    entrada = open("dataset/" + file_name, "rb")
    saida = open("LZW/Comprimidos/" + file_name.split(".")[0] + ".bin", "wb")
    comprimido = lzw.compressao(entrada.read())
    pickle.dump(comprimido, saida)

    saida = pickle.load(open("LZW/Comprimidos/" + file_name.split(".")[0] + ".bin", "rb"))
    entrada = open("LZW/Descomprimidos/" + file_name, "w")
    descomprimido = lzw.descompressao(saida)
    for l in descomprimido:
        entrada.write(l)
    entrada.close()


def huffmanCoding():
    sleep(1)
    clear()
    tprint("HUFFMAN")
    file_name = input("Nome do ficheiro: ")
    path = "dataset/" + file_name

    h = HuffmanCoding(path)

    output_path = h.compress()
    decom_path = h.decompress(output_path, file_name[-3:])


def runLengthCoding():
    sleep(1)
    clear()
    tprint("RLE")
    file_name = input("Nome do ficheiro: ")
    entrada = open("dataset/" + file_name, "rb")
    saida = open("RLE/Comprimidos/" + file_name.split(".")[0] + ".bin", "w")
    comprimido = rle.encode(entrada.read())
    for l in comprimido:
        saida.write(l)
    saida.close()

    saida = open("RLE/Comprimidos/" + file_name.split(".")[0] + ".bin", "rb")
    entrada = open("RLE/Descomprimidos/" + file_name, "w")
    descomprimido = rle.decode(saida.read())
    for l in descomprimido:
        entrada.write(l)
    entrada.close()


def main():
    os.system('pip install art')
    opt = 1
    while int(opt) != 0:
        clear()
        tprint("CODECS      LOSSLESS")
        opt = menu()
        opts = {1: lzwCoding, 2: huffmanCoding, 3: runLengthCoding}
        if opt.isdigit():
            if int(opt) != 0:
                opts[int(opt)]()
        else:
            print('Escolha errada')


main()
