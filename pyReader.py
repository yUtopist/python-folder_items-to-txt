import os
import codecs

path = r'F:\WEB\Nebrosco\public\svg\icons'
listArray = os.listdir(path)


def writeFunction():
    fileOperation = open('file.txt', 'w')

    for i in range(len(listArray)):
        localArray = list(listArray[i])

        localArray = localArray[:-4]

        for _i in range(len(localArray)):
            if localArray[_i] == '-':
                fileOperation.write('')
            elif localArray[_i - 1] == '-':
                fileOperation.write(localArray[_i].upper())
            else:
                fileOperation.write(localArray[_i])

        fileOperation.write('\n')

    fileOperation.close()


def makeItVariable(string):
    _list = list(string)
    _returnString = ''

    for i in range(len(_list)):
        if _list[i] == '-':
            _returnString += ''
        elif _list[i - 1] == '-':
            _returnString += _list[i].upper()
        else:
            _returnString += _list[i]

    return _returnString


def convertHTMLtoArray():
    htmlFile = codecs.open('myArray.txt', encoding='utf8')
    initialString = htmlFile.read()
    htmlFile.close()

    initialList = initialString.split()

    fileOperation = open('file.txt', 'w')

    listOfNames = []
    listOfValues = []

    for i in range(len(initialList)):
        if 'icon-' in initialList[i]:
            string = initialList[i]
            listOfNames.append(string)
        elif 'value=' in initialList[i]:
            string = initialList[i]
            listOfValues.append(string)

    for i in range(len(listOfNames)):
        nameString = listOfNames[i]
        nameIndex = nameString.index('icon')
        nameStringToWrite = ''
        valueStringToWrite = ''

        valueString = listOfValues[i]

        if '"' in nameString:
            _index = nameString.index('"')
            nameStringToWrite = makeItVariable(nameString[nameIndex + 5:-14])

        if i % 2 == 0:
            valueStringToWrite = valueString[7:-1]

        if nameStringToWrite != '' and valueStringToWrite != '':
            fileOperation.write(nameStringToWrite + ': ' + r"'\u" +
                                valueStringToWrite + "',\n")

    fileOperation.close()


convertHTMLtoArray()
