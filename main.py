import colorama
import inspect

colorama.init()

print("=" * 50)
print("ІНТРОСПЕКЦІЯ БІБЛІОТЕКИ COLORAMA")
print("=" * 50)

print("\n1. Інформація про бібліотеку:")
print("Назва:", colorama.__name__)
print("Версія:", colorama.__version__)
print("Розташування:", colorama.__file__)

print("\n2. Основні атрибути:")

attributes = ["Fore", "Back", "Style", "init",
              "deinit", "reinit", "just_fix_windows_console"]

for attribute in attributes:
    print(attribute, ":", getattr(colorama, attribute))

print("\n3. Атрибути Fore:")
print("RED - червоний колір")
print("GREEN - зелений колір")
print("BLUE - синій колір")
print("YELLOW - жовтий колір")

print(colorama.Fore.RED + "Це червоний текст")
print(colorama.Fore.GREEN + "Це зелений текст")
print(colorama.Fore.BLUE + "Це синій текст")

print("\n4. Атрибути Style:")
print("BRIGHT - яскравий текст")
print("DIM - тьмяний текст")
print("NORMAL - звичайний текст")
print("RESET_ALL - скидання форматування")

print("\n5. Основні методи:")

methods = ["init", "deinit", "reinit",
           "just_fix_windows_console"]

for method in methods:
    function = getattr(colorama, method)
    print("\nМетод:", method)
    print("Опис:", inspect.getdoc(function))
    print("Сигнатура:", inspect.signature(function))

# 6. Отримання всіх атрибутів бібліотеки
print("\n6. Усі доступні атрибути:")
print(dir(colorama))

colorama.deinit()

print("\nІнтроспекцію завершено!")
