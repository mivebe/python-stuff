# 1.	Да се дефинира функция, която връща като резултат квадранта,
# в който се намира дадена точка с координати x и у. 
# Функцията връща 0 ако точката е в центъра на координатната система.

defmodule Quadrant do
  def get_quadrant(0, 0), do: 0
  def get_quadrant(x, y) when x > 0 and y > 0, do: 1
  def get_quadrant(x, y) when x < 0 and y > 0, do: 2
  def get_quadrant(x, y) when x < 0 and y < 0, do: 3
  def get_quadrant(x, y) when x > 0 and y < 0, do: 4
  def get_quadrant(_, _), do: :on_axis  # точката е върху една от осите

end

# Примери за използване:
IO.puts("Точка (3, 4): Квадрант #{Quadrant.get_quadrant(3, 4)}")
IO.puts("Точка (-2, 5): Квадрант #{Quadrant.get_quadrant(-2, 5)}")
IO.puts("Точка (-1, -1): Квадрант #{Quadrant.get_quadrant(-1, -1)}")
IO.puts("Точка (4, -2): Квадрант #{Quadrant.get_quadrant(4, -2)}")
IO.puts("Точка (0, 0): #{Quadrant.get_quadrant(0, 0)}")
IO.puts("Точка (0, 5): #{Quadrant.get_quadrant(0, 5)}")
