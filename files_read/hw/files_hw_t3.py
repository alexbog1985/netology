import os


class File:
    def __init__(self, path_file):
        self.path_file = path_file
        self.file_name = path_file.split('/')[-1]
        self.count_lines = 0
        self.text = self.get_text_from_file()

    def get_text_from_file(self):
        with open(self.path_file, 'r', encoding='utf8') as f:
            text = ''
            for line in f:
                text += line
                self.count_lines += 1
            return text


class NewText:
    def __init__(self, files, new_file):
        self.files = files
        self.new_text = ''
        self.new_file = new_file

    def get_new_text(self):
        text_list = []
        for file in self.files:
            text_list.append([file.file_name, str(file.count_lines), file.text + '\n'])
        text_list.sort(key=lambda x: x[1])
        for text in text_list:
            self.new_text += '\n'.join(text)

    def save_to_file(self):
        print(self.new_file)
        path_to_dir = os.path.join(os.getcwd(), os.sep.join(self.new_file.split('/')[1:-1]))
        print(path_to_dir)
        if os.path.exists(path_to_dir):
            with open(self.new_file, 'w', encoding='utf8') as f:
                f.write(self.new_text)
                print(f'Текст сохранен в файле: {os.path.join(os.getcwd(), os.sep.join(self.new_file.split('/')[1:]))}')
        else:
            os.makedirs(path_to_dir)
            with open(self.new_file, 'w', encoding='utf8') as f:
                f.write(self.new_text)
                print(f'Текст сохранен в файле: {os.path.join(os.getcwd(), os.sep.join(self.new_file.split('/')[1:]))}')


file1 = File('./sorted/1.txt')
file2 = File('./sorted/2.txt')
file3 = File('./sorted/3.txt')

new_t = NewText([file1, file2, file3], './export/new_text.txt')
new_t.save_to_file()
