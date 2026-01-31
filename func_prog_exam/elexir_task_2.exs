# 2.	Да се дефинира функция, която по дадено естествено число n изчислява:
# F(n) = 1.2 + 2.3.4 + 3.4.5.6 + … + n.(n+1). … .2n

defmodule Task2 do
  # Изчислява произведението k * (k+1) * ... * 2k
  defp product(k) do
    Enum.reduce(k..(2 * k), 1, &*/2)
  end

  # F(n) = сума от всички членове от 1 до n
  def f(n) when n < 1, do: 0

  def f(n) do
    1..n
    |> Enum.map(&product/1)
    |> Enum.sum()
  end
end

# Примери:
# F(1) = 1*2 = 2
# F(2) = 1*2 + 2*3*4 = 2 + 24 = 26
# F(3) = 1*2 + 2*3*4 + 3*4*5*6 = 2 + 24 + 360 = 386

IO.puts("F(1) = #{Task2.f(1)}")
IO.puts("F(2) = #{Task2.f(2)}")
IO.puts("F(3) = #{Task2.f(3)}")
IO.puts("F(4) = #{Task2.f(4)}")
