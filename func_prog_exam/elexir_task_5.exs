# Задача 5: Рекурсивна процедура за премахване на повтарящи се елементи
# от сортиран във възходящ ред списък

defmodule RemoveDuplicates do
  # Базов случай: празен списък
  def clean([]), do: []

  # Базов случай: списък с един елемент
  def clean([x]), do: [x]

  # Рекурсивен случай: ако първите два елемента са равни, пропускаме първия
  def clean([x, x | tail]), do: clean([x | tail])

  # Рекурсивен случай: ако първите два елемента са различни, запазваме първия
  def clean([x | tail]), do: [x | clean(tail)]
end

# Примери за тестване
IO.puts("Тест 1: [1, 1, 2, 3, 3, 3, 4, 5, 5]")
IO.inspect(RemoveDuplicates.clean([1, 1, 2, 3, 3, 3, 4, 5, 5]))

IO.puts("\nТест 2: [1, 2, 3, 4, 5]")
IO.inspect(RemoveDuplicates.clean([1, 2, 3, 4, 5]))

IO.puts("\nТест 3: [1, 1, 1, 1]")
IO.inspect(RemoveDuplicates.clean([1, 1, 1, 1]))

IO.puts("\nТест 4: []")
IO.inspect(RemoveDuplicates.clean([]))

IO.puts("\nТест 5: [5]")
IO.inspect(RemoveDuplicates.clean([5]))
