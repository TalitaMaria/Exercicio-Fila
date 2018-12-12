class Fila:
  def __init__(self):
    self.queue = []
  
  def Dequeue(self):
    
    if not (self.IsEmpty()):
      self.queue.pop(0)
  
  def Enqueue(self,item):
    self.queue.append(item)

  def lenght(self):
    return len(self.queue)
  
  def IsEmpty(self):
    return len(self.queue) == 0
