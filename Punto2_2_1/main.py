# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Parseador

parse = Parseador

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    texto = parse.obtenerTextoParseado("..\king_lear.txt")
    parse.mostrarResultados(texto)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/