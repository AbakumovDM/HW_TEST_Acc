# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие
def people(document_namber):
  person_id = 0
  # user_input = input('Введите номер документа:')
  for id, person in enumerate(documents):
    if document_namber == person["number"]:
      person_id = id
      return documents[person_id]['name']
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
def shelf(directory):
  # user_input = input('Введите номер документа:')
  for cheak in directories.items():
    if directory in cheak[1]:
      return f'Номер полки {cheak[0]}'
    # else:
    #   return ("Документ введён не верно")
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
def list_():
  doc_list = list()
  for inf in documents:
    doc_list.append((inf["type"], inf["number"], inf["name"]))
  # return (inf["type"], inf["number"], inf["name"])
  # return 'конец списка'
  return doc_list

def add(doc_type, doc_number, full_name, shelf_number):
  new_inf = [doc_type, doc_number, full_name, shelf_number]
  if new_inf[3] not in directories.keys():
    return 'Такой полки не существует'
  else:
    documents.append({"type": new_inf[0], "number": new_inf[1], "name": new_inf[2]})
    directories[new_inf[3]].append(new_inf[1])
    # print (documents)
    # print (directories)
    return f'документ {new_inf[0]} с номером {new_inf[1]} добавлен на полку {new_inf[3]}'

# people(documents)
# shelf(directories)
# list_(documents)
# add(documents, directories)

def main_acc():
  while True:
    user_input = input('Введите команду:')
    if user_input == 'p':
      return(people(documents))
    elif user_input == 's':
      return(shelf(directories))
    elif user_input == 'l':
      return(list_(documents))
    elif user_input == 'a':
      return(add(documents, directories))
    elif user_input == 'q':
      return('До свидания!')
      break
# main_acc()
