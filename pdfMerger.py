# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileMerger, PdfFileReader, utils
import os
import glob


log = []
def pdfMerger(outPdfName):
        output_path = r'C:\\pyPDF\\pdfs\\' #куда будут сохраняться пдф
        merger = PdfFileMerger()
        path = output_path + outPdfName.rstrip() + "\\"
        for filename in glob.glob("*/*.pdf"):
            print("Найден пдф файл:" + filename)
            try:
                merger.append(PdfFileReader(filename, 'rb'))
            except KeyError:
                log.append("Cant take page: " + filename + '\n')
                print("SMTHWRONG")
            except utils.PdfReadError:
                log.append("Не могу прочитать файл:" + outPdfName)

        try:
            os.mkdir(path)
        except FileExistsError:
            print("_____________")
        merger.write(path + outPdfName.rstrip() + ".pdf")
        print("Успешно:",  outPdfName)
                
            


def pathCreate(pathInput):
    # path = r"\\10.55.141.10\Archive55$\DoksKD\zu\55\"" --For windows
    path = r'D:\\Archive55\\DoksKD\\zu\\55\\'  # указывается изначальный путь для формирования конечного пути
    path_sum = pathInput[0:5] + '\\' + pathInput[0:8] + '\\' + pathInput[0:12] + '\\' + pathInput.rstrip()
    return path + path_sum


def load_list(listOfNumbers):
    count = 0
    try:
        f = open(listOfNumbers + '.txt')
        while True:
            line = f.readline()
            pc = pathCreate(line)
            if os.path.exists(pc):
                os.chdir(pc)
                pdfMerger(line)
                count = count + 1
                if not line:
                    break
            else:
                log.append("Cant find path" + line)

    except FileNotFoundError:
        print("Проверьте путь к файлу", pc)

    except UnboundLocalError:
        print("Введите корректное имя файла / расположение")
		
    finally:
        print("Всего файлов создано: ", count)
        f = open(r"C:\\pyPDF\\log.txt", 'w')
        f.writelines(log)
        f.close()


load_list(r"C:\\pyPDF\\numbers") #путь до ТХТ файла в котором хранится список папок.

