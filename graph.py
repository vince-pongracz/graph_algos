

class Edge:
  def __init__(self, p1: int, p2: int, w: float):
    self.p1 = p1
    self.p2 = p2
    self.w = w
    
class DijkstraUtil:
  def __init__(self, p: int, d: float, final: bool):
    self.p = p
    self.d = d
    self.final = final
    self.prevNode: int = None
  def __str__(self):
     return f"p: {self.p}, d: {self.d}, f: {self.final}, prevNode: {self.prevNode}"