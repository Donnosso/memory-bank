memories = []
add_another = "y"

while add_another == "y":
    title = input("Title: ")
    date = input("Date: ")
    mood = input("Mood: ")
    journal = input("Journal: ")

#print (f'\nMemory saved:{title} ({date}) - Mood: {mood}\n{journal}')

    memory = {
        'title': title,
        'date': date,
        'mood': mood,
        'journal': journal
    }

    memories.append(memory)


    add_another = input("Add another memory(y/n): ")

### PRINTS THE WHOLE MEMORY COLLECTION ###
for m in memories:
    print(f'\n{m['title']}\n{m['date']}\n{m['mood']}\n{m['journal']}')
