def find_common_participants(group1, group2, raz=","):
    list1 = group1.split(raz)
    list2 = group2.split(raz)
    list1_clean = [name.strip() for name in list1]
    list2_clean = [name.strip() for name in list2]
    participants_first_group = "Иванов|Петров|Сидоров"
    participants_second_group = "Петров|Сидоров|Смирнов"
    common = set(list1_clean) & set(list2_clean)
    return sorted(common)
# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов | Петров | Сидоров"
participants_second_group = "Петров | Сидоров | Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, raz=" | ")
print("Общие участники (разделитель ' | '):", common_participants)