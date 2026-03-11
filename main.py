from module import Diary, DiaryPersistence, DiaryStatistics


if __name__ == "__main__":

    # Loome Diary objekti
    diary = Diary()

    diary.add_entry("Täna oli ilus ilm.")
    diary.add_entry("Õppisin programmeerimist.")
    diary.add_entry("SRP on tegelikult väga loogiline.")

    print("---- DIARY SISU ----")
    print(diary)
    print()

    # Statistika
    print("---- STATISTIKA ----")
    DiaryStatistics.print_statistics(diary)
    print()

    # Salvestamine faili
    filename = "diary.txt"
    DiaryPersistence.save_to_file(diary, filename)

    print(f"Salvestatud faili: {filename}")
    print()

    # Laeme failist
    loaded_diary = DiaryPersistence.load_from_file(filename)

    print("---- FAILIST LAETUD ----")
    print(loaded_diary)
    print()

    # Kontrollime kas lisamine töötab
    loaded_diary.add_entry("See lisati pärast laadimist.")

    print("---- PÄRAST UUT LISAMIST ----")
    print(loaded_diary)