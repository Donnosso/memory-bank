memories = []

def capture_memory():
    add_another = "y"
    while add_another == "y":
        title = input("Title: ").lower()
        date = input("Date: ")
        mood = input("Mood: ").lower()
        journal = input("Journal: ").lower()

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
    if not memories == None:
        print("No memories yet. Why don't you create some..")
        return
    for m in memories:
        print(f'\n{m['title']}\n{m['date']}\n{m['mood']}\n{m['journal']}')


def search_memories(memories, keyword):
    searched_result = []
    for m in memories:
        if keyword in m['title'] or keyword in m['journal']:
            searched_result.append(m)
    ###TELLS THE USER IF THE SEARCH_KEY IS NOT AVAILABLE AFTER THE LOOP CHECK###
    if not searched_result:
        print(f"You don't have this '{keyword}' memory yet.")
        return
    ###RETURNS THE SEARCHED MEMORY DICTIONARY AFTER THE LOOP CHECK###
    return searched_result



#capture_memory()

display_memories(memories)

search_key = input("What do you wish to recollect...? ")
result = search_memories(memories, search_key)
if result:
    display_memories(result)
