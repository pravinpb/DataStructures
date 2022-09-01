class Kangaroo:
  def __init__(self):
    self.pouch_contents = []

  def put_in_pouch(self,data):
    self.pouch_contents.append(data)
    print(self.poch_contents)

obj = Kangaroo()
a = obj.put_in_pouch(90)
b = obj.put_in_pouch(92)

print(a+b)
