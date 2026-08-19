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
    #if memories == None or memories == []:
    if not memories:
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


def delete_memory(memories, keyword):
    matching_memories = search_memories(memories, keyword)
    if len(matching_memories) == 1:
        memories.remove(matching_memories[0])
        print(f"This memory {matching_memories[0]} has been erased")
    elif len(matching_memories) > 1:
        ###DISPLAYS MEMORIES THAT MATCHES THE KEYWORD###
        display_memories(matching_memories)
        ###USER SELECTS THE MEMORY TO BE ERASED###
        option_to_delete = int(input(f" Pick any of these memories to erase: {matching_memories}\n1")) - 1
        memories.remove(matching_memories[option_to_delete])
        print(f"This memory {matching_memories[option_to_delete]} has been erased")
    return memories

capture_memory()

#display_memories(memories)

# search_key = input("What do you wish to recollect...? ")
# result = search_memories(memories, search_key)
# if result:
#     display_memories(result)


keyword = input(f" Search for a memory to delete: ")
delete_memory(memories, keyword)
display_memories(memories)

