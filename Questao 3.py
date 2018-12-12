class Fila:
  def __init__(self):
    self.lista = []
  
  def Agendamento(self,item):
    if(self.lenght()>20):
        self.lista.append(item)

  def Atendimento(self):
    if not (self.isEmpty()):
      self.lista.pop(0)
  
  def Lenght(self):
    return len(self.lista)
  
  def IsEmpty(self):
    return len(self.lista) == 0
