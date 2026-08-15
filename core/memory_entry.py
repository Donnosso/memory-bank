memories = []


def capture_memory():
    add_another = "y"
    while add_another == "y":
        title = input("Title: ")
        date = input("Date: ")
        mood = input("Mood: ")
        journal = input("Journal: ")

        memory = {
            'title': title,
            'date': date,
            'mood': mood,
            'journal': journal
        }
        add_another = input("Add another memory(y/n): ")
        memories.append(memory)

    return memory


def display_memories(memories):
    ### PRINTS THE WHOLE MEMORY COLLECTION ###
    for m in memories:
        print(f'\n{m['title']}\n{m['date']}\n{m['mood']}\n{m['journal']}')


capture_memory()
display_memories(memories)

