# TODO  Напишите функцию count_letters
def count_letters(input_text):
    res_counts = {}
    for char in input_text.lower():
        if char.isalpha():
            res_counts[char] = res_counts.get(char, 0) + 1
    return res_counts
# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_counts_dict):
    total = sum(letter_counts_dict.values())
    freqs = {}
    for char, count in letter_counts_dict.items():
        freqs[char] = round(count / total, 2)
    return freqs
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
counts = count_letters(main_str)
freq_dict = calculate_frequency(counts)
for letter, freq in freq_dict.items():
    print(f"{letter}: {freq:.2f}")