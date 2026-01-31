# Задача 4: Функция, която изтрива от списък всички елементи
# със стойности, попадащи в интервала (a, b)

defmodule ListFilter do
  # Изтрива елементи в отворения интервал (a, b)
  def remove_in_interval(list, a, b) do
    Enum.filter(list, fn x -> x <= a or x >= b end)
  end

  # Рекурсивна версия без Enum
  def remove_in_interval_rec([], _a, _b), do: []
  def remove_in_interval_rec([head | tail], a, b) when head > a and head < b do
    remove_in_interval_rec(tail, a, b)
  end
  def remove_in_interval_rec([head | tail], a, b) do
    [head | remove_in_interval_rec(tail, a, b)]
  end
end

# Примери 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

IO.puts("Оригинален списък: #{inspect(list)}")
IO.puts("След премахване на елементи в (3, 7): #{inspect(ListFilter.remove_in_interval(list, 3, 7))}")
IO.puts("Рекурсивна версия: #{inspect(ListFilter.remove_in_interval_rec(list, 3, 7))}")

# Примери 2
IO.puts("\nПримери 2:")
IO.puts("Списък [1,2,3,4,5], интервал (1,4): #{inspect(ListFilter.remove_in_interval([1,2,3,4,5], 1, 4))}")
IO.puts("Списък [10,20,30,40,50], интервал (15,45): #{inspect(ListFilter.remove_in_interval([10,20,30,40,50], 15, 45))}")
