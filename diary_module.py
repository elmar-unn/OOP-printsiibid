class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, text):
        self.entries.append(text)

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries.pop(index)

    def __str__(self):
        if not self.entries:
            return "Diary is empty."

        result = ""
        for i, entry in enumerate(self.entries, start=1):
            result += f"{i}. {entry}\n"
        return result


class DiaryPersistence:

    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for entry in diary.entries:
                file.write(entry + "\n")

    @staticmethod
    def load_from_file(filename):
        diary = Diary()

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                diary.add_entry(line.strip())

        return diary


class DiaryStatistics:

    @staticmethod
    def print_statistics(diary):
        entry_count = len(diary.entries)

        word_count = 0
        for entry in diary.entries:
            word_count += len(entry.split())

        avg_words = 0
        if entry_count > 0:
            avg_words = word_count / entry_count

        print(f"Sissekandeid: {entry_count}")
        print(f"Sõnu kokku: {word_count}")
        print(f"Keskmiselt sõnu sissekandes: {avg_words:.2f}")