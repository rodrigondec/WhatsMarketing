class Status:
    list = []

    def __init__(self, num, suceesso):
        self.num = num
        self.sucesso = suceesso
        print("{} para o num {}".format(self.get_msg(), self.num))
        Status.list.append(self)

    def get_msg(self):
        if self.sucesso:
            return "Mensagem enviada com sucesso"
        return "Falha no envio da mensagem"

    def to_csv(self):
        return '{},{}'.format(self.num, self.get_msg())
