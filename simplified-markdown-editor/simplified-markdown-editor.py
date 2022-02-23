
class Markdown:
    def __init__(self, commands, formatting, text, choose_format):
        self.commands = commands
        self.formatting = formatting
        self.text = text
        self.choose_format = choose_format

    def start(self):
        try:
            choose = str(input("Special commands: !help, !done"))
            if choose in self.commands:
                if choose == self.commands[0]:
                    print("Available formatters:")
                    for i in self.formatting.keys():
                        print(i)
                    self.choose()
                else:
                    exit()
            else:
                print("Unknown formatting type or command")
                self.start()

        except TypeError:
            print("Unknown formatting type or command")

    def choose(self):
        try:
            self.choose_format = str(input("Choose a formatter:"))
            if self.choose_format in self.formatting.keys():
                rows = int(input("Number of rows:"))
                for j in range(rows):
                    if self.choose_format == "header":
                        self.header(j)
                    elif self.choose_format == "new-line":
                        self.new_line()
                    elif self.choose_format == "link":
                        self.link(j)
                    else:
                        self.process_default(j)
                self.save()
            else:
                print("Unknown formatting type or command")
                self.choose()
        except TypeError or ValueError:
            self.choose()

    def process_default(self, j):
        text = str(input(f"Row #{j + 1}"))
        self.text = f"{self.formatting[self.choose_format][0]}{text}" \
                    f"{self.formatting[self.choose_format][1]}"
        print(self.text)

    def header(self, j):
        while True:
            level = int(input("level:"))
            if 7 > level > 0:
                break
        text = str(input(f"Row #{j + 1}"))
        self.text += f"{self.formatting[self.choose_format][0] * level}{text}{self.formatting[self.choose_format][1]}\n"
        print(self.text)

    def link(self, j):
        print(f"Row #{j + 1}")
        label = str(input("label:"))
        url = str(input("url:"))
        self.text = f"[{label}]{self.formatting[self.choose_format][0]}{url}{self.formatting[self.choose_format][1]}"
        print(self.text)

    def new_line(self):
        self.text = self.formatting[self.choose_format]
        print(self.text)

    def save(self):
        with open('try.md', 'w') as file:
            file.write(f'{self.text}')


markdown = Markdown(["!help", "!done"], {"plain": ["", ""], "bold": ["**", "**"], "italic": ["*", "*"],
                                         "header": ["#", ""], "link": ["(", ")"], "inline-code": ["(", ")"],
                                         "ordered-list": ["1. ", ""], "unordered-list": ["* ", ""],
                                         "new-line": ""}, '', '')

markdown.start()
