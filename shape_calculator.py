class Rectangle:
  def __init__(self, width, heigth):
    self.width = width
    self.heigth = heigth

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.heigth})"

  def set_width(self, width):
    self.width = width

  def set_height(self, heigth):
    self.heigth = heigth

  def get_area(self):
    area = self.width * self.heigth
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.heigth
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.heigth ** 2) ** .5
    return diagonal

  def get_picture(self):
    if self.heigth > 50 or self.width > 50:
        return 'Too big for picture.'

    picture = (('*' * self.width) + '\n') * self.heigth
    return picture

  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())
    

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.heigth = side

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, side):
    self.width = side
    self.heigth = side 