defmodule PiCalculator do
  @moduledoc """
  Курсова работа: Изчисляване на π чрез три различни числови метода.
  Всеки метод е реализиран рекурсивно и итеративно.
  """

  # Реална стойност на π за сравнение
  @pi :math.pi()

  # ============================================================================
  # 1. ФОРМУЛА НА ЛАЙБНИЦ (Leibniz Formula)
  # π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
  # ============================================================================

  @doc "Лайбниц - рекурсивна реализация"
  def leibniz_recursive(n) do
    4 * leibniz_recursive_helper(0, n)
  end

  defp leibniz_recursive_helper(i, n) when i >= n, do: 0.0

  defp leibniz_recursive_helper(i, n) do
    sign = if rem(i, 2) == 0, do: 1, else: -1
    term = sign / (2 * i + 1)
    term + leibniz_recursive_helper(i + 1, n)
  end

  @doc "Лайбниц - итеративна реализация"
  def leibniz_iterative(n) do
    result =
      Enum.reduce(0..(n - 1), 0.0, fn i, acc ->
        sign = if rem(i, 2) == 0, do: 1, else: -1
        acc + sign / (2 * i + 1)
      end)

    4 * result
  end

  # Лайбниц - опашкова рекурсия (tail recursion)
  @doc "Лайбниц - опашкова рекурсия"
  def leibniz_tail_recursive(n) do
    4 * leibniz_tail_helper(0, n, 0.0)
  end

  defp leibniz_tail_helper(i, n, acc) when i >= n, do: acc

  defp leibniz_tail_helper(i, n, acc) do
    sign = if rem(i, 2) == 0, do: 1, else: -1
    term = sign / (2 * i + 1)
    leibniz_tail_helper(i + 1, n, acc + term)
  end

  # ============================================================================
  # 2. СЕРИЯ НА НИЛАКАНТА (Nilakantha Series)
  # π = 3 + 4/(2·3·4) - 4/(4·5·6) + 4/(6·7·8) - ...
  # ============================================================================

  @doc "Нилаканта - рекурсивна реализация"
  def nilakantha_recursive(n) do
    3 + nilakantha_recursive_helper(0, n)
  end

  defp nilakantha_recursive_helper(i, n) when i >= n, do: 0.0

  defp nilakantha_recursive_helper(i, n) do
    sign = if rem(i, 2) == 0, do: 1, else: -1
    k = 2 + 2 * i
    term = sign * 4 / (k * (k + 1) * (k + 2))
    term + nilakantha_recursive_helper(i + 1, n)
  end

  @doc "Нилаканта - итеративна реализация"
  def nilakantha_iterative(n) do
    result =
      Enum.reduce(0..(n - 1), 0.0, fn i, acc ->
        sign = if rem(i, 2) == 0, do: 1, else: -1
        k = 2 + 2 * i
        acc + sign * 4 / (k * (k + 1) * (k + 2))
      end)

    3 + result
  end

  @doc "Нилаканта - опашкова рекурсия"
  def nilakantha_tail_recursive(n) do
    3 + nilakantha_tail_helper(0, n, 0.0)
  end

  defp nilakantha_tail_helper(i, n, acc) when i >= n, do: acc

  defp nilakantha_tail_helper(i, n, acc) do
    sign = if rem(i, 2) == 0, do: 1, else: -1
    k = 2 + 2 * i
    term = sign * 4 / (k * (k + 1) * (k + 2))
    nilakantha_tail_helper(i + 1, n, acc + term)
  end

  # ============================================================================
  # 3. ПРОИЗВЕДЕНИЕ НА УОЛИС (Wallis Product)
  # π/2 = (2/1)·(2/3)·(4/3)·(4/5)·(6/5)·(6/7)·...
  # ============================================================================

  @doc "Уолис - рекурсивна реализация"
  def wallis_recursive(n) do
    2 * wallis_recursive_helper(1, n)
  end

  defp wallis_recursive_helper(i, n) when i > n, do: 1.0

  defp wallis_recursive_helper(i, n) do
    numerator = 4 * i * i
    denominator = (2 * i - 1) * (2 * i + 1)
    numerator / denominator * wallis_recursive_helper(i + 1, n)
  end

  @doc "Уолис - итеративна реализация"
  def wallis_iterative(n) do
    result =
      Enum.reduce(1..n, 1.0, fn i, acc ->
        numerator = 4 * i * i
        denominator = (2 * i - 1) * (2 * i + 1)
        acc * (numerator / denominator)
      end)

    2 * result
  end

  @doc "Уолис - опашкова рекурсия"
  def wallis_tail_recursive(n) do
    2 * wallis_tail_helper(1, n, 1.0)
  end

  defp wallis_tail_helper(i, n, acc) when i > n, do: acc

  defp wallis_tail_helper(i, n, acc) do
    numerator = 4 * i * i
    denominator = (2 * i - 1) * (2 * i + 1)
    wallis_tail_helper(i + 1, n, acc * (numerator / denominator))
  end

  # ============================================================================
  # ПОМОЩНИ ФУНКЦИИ ЗА ИЗМЕРВАНЕ И СРАВНЕНИЕ
  # ============================================================================

  @doc "Измерване на време за изпълнение в микросекунди"
  def measure_time(fun) do
    {time, result} = :timer.tc(fun)
    {time, result}
  end

  @doc "Изчислява грешката спрямо реалната стойност на π"
  def error(approximation) do
    abs(approximation - @pi)
  end

  @doc "Изчислява броя значещи цифри"
  def significant_digits(approximation) do
    err = error(approximation)

    if err == 0 do
      :infinity
    else
      -:math.log10(err) |> Float.floor() |> trunc()
    end
  end

  @doc "Намира минималния брой итерации за постигане на определена точност"
  def find_iterations_for_precision(method, target_precision, max_iterations \\ 1_000_000) do
    find_iterations_helper(method, target_precision, 1, max_iterations)
  end

  defp find_iterations_helper(_method, _target, current, max) when current > max do
    {:not_found, max}
  end

  defp find_iterations_helper(method, target_precision, current, max) do
    result = apply_method(method, current)
    err = error(result)

    if err <= target_precision do
      {:found, current, result, err}
    else
      # Увеличаваме експоненциално за по-бързо търсене
      next = min(current * 2, max)

      if next == current do
        {:not_found, max}
      else
        find_iterations_helper(method, target_precision, next, max)
      end
    end
  end

  defp apply_method(:leibniz, n), do: leibniz_iterative(n)
  defp apply_method(:nilakantha, n), do: nilakantha_iterative(n)
  defp apply_method(:wallis, n), do: wallis_iterative(n)

  # ============================================================================
  # ОСНОВНИ ТЕСТОВЕ И СРАВНЕНИЯ
  # ============================================================================

  @doc "Изпълнява пълно сравнение на всички методи"
  def run_comparison do
    IO.puts("=" |> String.duplicate(80))
    IO.puts("    КУРСОВА РАБОТА: ИЗЧИСЛЯВАНЕ НА π")
    IO.puts("    Реална стойност на π: #{@pi}")
    IO.puts("=" |> String.duplicate(80))

    iterations_list = [10, 100, 1_000, 10_000, 100_000]

    # Тест 1: Точност при различен брой итерации
    IO.puts("\n" <> "=" |> String.duplicate(80))
    IO.puts("  1. СРАВНЕНИЕ НА ТОЧНОСТТА ПРИ РАЗЛИЧЕН БРОЙ ИТЕРАЦИИ")
    IO.puts("=" |> String.duplicate(80))

    for n <- iterations_list do
      IO.puts("\n--- #{n} итерации ---")
      compare_accuracy(n)
    end

    # Тест 2: Време за изпълнение
    IO.puts("\n" <> "=" |> String.duplicate(80))
    IO.puts("  2. СРАВНЕНИЕ НА ВРЕМЕТО ЗА ИЗПЪЛНЕНИЕ (микросекунди)")
    IO.puts("=" |> String.duplicate(80))

    for n <- [1_000, 10_000, 100_000] do
      IO.puts("\n--- #{n} итерации ---")
      compare_performance(n)
    end

    # Тест 3: Итерации за постигане на точност
    IO.puts("\n" <> "=" |> String.duplicate(80))
    IO.puts("  3. БРОЙ ИТЕРАЦИИ ЗА ПОСТИГАНЕ НА ОПРЕДЕЛЕНА ТОЧНОСТ")
    IO.puts("=" |> String.duplicate(80))

    compare_convergence()

    # Тест 4: Сравнение рекурсия vs итерация
    IO.puts("\n" <> "=" |> String.duplicate(80))
    IO.puts("  4. СРАВНЕНИЕ: РЕКУРСИЯ vs ОПАШКОВА РЕКУРСИЯ vs ИТЕРАЦИЯ")
    IO.puts("=" |> String.duplicate(80))

    compare_implementations()

    IO.puts("\n" <> "=" |> String.duplicate(80))
    IO.puts("  КРАЙ НА СРАВНЕНИЕТО")
    IO.puts("=" |> String.duplicate(80))
  end

  defp compare_accuracy(n) do
    methods = [
      {"Лайбниц", leibniz_iterative(n)},
      {"Нилаканта", nilakantha_iterative(n)},
      {"Уолис", wallis_iterative(n)}
    ]

    IO.puts(
      String.pad_trailing("Метод", 15) <>
        String.pad_trailing("Резултат", 20) <>
        String.pad_trailing("Грешка", 20) <>
        "Значещи цифри"
    )

    IO.puts("-" |> String.duplicate(70))

    for {name, result} <- methods do
      err = error(result)
      digits = significant_digits(result)

      IO.puts(
        String.pad_trailing(name, 15) <>
          String.pad_trailing("#{Float.round(result, 15)}", 20) <>
          String.pad_trailing("#{:erlang.float_to_binary(err, decimals: 15)}", 20) <>
          "#{digits}"
      )
    end
  end

  defp compare_performance(n) do
    methods = [
      {"Лайбниц (итер.)", fn -> leibniz_iterative(n) end},
      {"Лайбниц (tail)", fn -> leibniz_tail_recursive(n) end},
      {"Нилаканта (итер.)", fn -> nilakantha_iterative(n) end},
      {"Нилаканта (tail)", fn -> nilakantha_tail_recursive(n) end},
      {"Уолис (итер.)", fn -> wallis_iterative(n) end},
      {"Уолис (tail)", fn -> wallis_tail_recursive(n) end}
    ]

    IO.puts(String.pad_trailing("Метод", 25) <> "Време (μs)")
    IO.puts("-" |> String.duplicate(40))

    for {name, fun} <- methods do
      # Изпълняваме 3 пъти и вземаме средното
      times =
        for _ <- 1..3 do
          {time, _} = measure_time(fun)
          time
        end

      avg_time = Enum.sum(times) / 3
      IO.puts(String.pad_trailing(name, 25) <> "#{Float.round(avg_time, 2)}")
    end
  end

  defp compare_convergence do
    precisions = [1.0e-3, 1.0e-6, 1.0e-9]

    IO.puts("\nМинимален брой итерации за постигане на точност:")
    IO.puts("-" |> String.duplicate(60))

    for precision <- precisions do
      IO.puts("\nТочност: #{precision}")

      for method <- [:leibniz, :nilakantha, :wallis] do
        case find_iterations_for_precision(method, precision) do
          {:found, n, _result, _err} ->
            IO.puts("  #{method}: #{n} итерации")

          {:not_found, max} ->
            IO.puts("  #{method}: > #{max} итерации (не е постигната)")
        end
      end
    end
  end

  defp compare_implementations do
    n = 10_000

    IO.puts("\nТест с #{n} итерации:")
    IO.puts("-" |> String.duplicate(60))

    # Лайбниц
    IO.puts("\nЛАЙБНИЦ:")
    {t1, r1} = measure_time(fn -> leibniz_iterative(n) end)
    {t2, r2} = measure_time(fn -> leibniz_tail_recursive(n) end)
    IO.puts("  Итеративна:       #{t1} μs, резултат: #{Float.round(r1, 10)}")
    IO.puts("  Опашкова рекурс.: #{t2} μs, резултат: #{Float.round(r2, 10)}")

    # Нилаканта
    IO.puts("\nНИЛАКАНТА:")
    {t1, r1} = measure_time(fn -> nilakantha_iterative(n) end)
    {t2, r2} = measure_time(fn -> nilakantha_tail_recursive(n) end)
    IO.puts("  Итеративна:       #{t1} μs, резултат: #{Float.round(r1, 10)}")
    IO.puts("  Опашкова рекурс.: #{t2} μs, резултат: #{Float.round(r2, 10)}")

    # Уолис
    IO.puts("\nУОЛИС:")
    {t1, r1} = measure_time(fn -> wallis_iterative(n) end)
    {t2, r2} = measure_time(fn -> wallis_tail_recursive(n) end)
    IO.puts("  Итеративна:       #{t1} μs, резултат: #{Float.round(r1, 10)}")
    IO.puts("  Опашкова рекурс.: #{t2} μs, резултат: #{Float.round(r2, 10)}")

    # Тест на обикновена рекурсия (с по-малък брой итерации)
    IO.puts("\n" <> "-" |> String.duplicate(60))
    IO.puts("Тест на ОБИКНОВЕНА рекурсия (1000 итерации - избягваме stack overflow):")

    small_n = 1_000
    {t1, r1} = measure_time(fn -> leibniz_recursive(small_n) end)
    {t2, r2} = measure_time(fn -> nilakantha_recursive(small_n) end)
    {t3, r3} = measure_time(fn -> wallis_recursive(small_n) end)
    IO.puts("  Лайбниц рекурс.:   #{t1} μs, резултат: #{Float.round(r1, 10)}")
    IO.puts("  Нилаканта рекурс.: #{t2} μs, резултат: #{Float.round(r2, 10)}")
    IO.puts("  Уолис рекурс.:     #{t3} μs, резултат: #{Float.round(r3, 10)}")
  end

  @doc "Демонстрация на единични изчисления"
  def demo do
    IO.puts("Демонстрация на изчисляване на π:")
    IO.puts("Реална стойност: #{@pi}\n")

    n = 1000

    IO.puts("С #{n} итерации:")
    IO.puts("  Лайбниц:   #{leibniz_iterative(n)}")
    IO.puts("  Нилаканта: #{nilakantha_iterative(n)}")
    IO.puts("  Уолис:     #{wallis_iterative(n)}")
  end
end

# ============================================================================
# ИЗПЪЛНЕНИЕ НА ПРОГРАМАТА
# ============================================================================

IO.puts("\n")
PiCalculator.run_comparison()
