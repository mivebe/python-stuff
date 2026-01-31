defmodule Points do
  # Проверява дали точка е в първи квадрант
  def in_first_quadrant?({x, y}) when x > 0 and y > 0, do: true
  def in_first_quadrant?(_), do: false

  # Брои точките в първи квадрант
  def count_first_quadrant(points) do
    points
    |> Enum.filter(&in_first_quadrant?/1)
    |> length()
  end

  # Алтернативен вариант с Enum.count
  def count_first_quadrant_v2(points) do
    Enum.count(points, fn {x, y} -> x > 0 and y > 0 end)
  end
end

# Примери за използване:
points = [{1, 2}, {-3, 4}, {5, -1}, {2, 3}, {-1, -1}, {0, 5}]

IO.puts("Точки: #{inspect(points)}")
IO.puts("Брой точки в 1-ви квадрант: #{Points.count_first_quadrant(points)}")
