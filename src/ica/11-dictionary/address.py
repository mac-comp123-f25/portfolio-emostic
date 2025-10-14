betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'} ]

print("Original address book is:", address_book)
address_book.append({'Name': 'Harry Potter',
    'Phone': 'x7123',
    'Street': '4 Privet Drive',
    'City': 'Little Whinging',
    'State': 'Surrey',
    'Email': 'hpotter@hogwarts.edu'
})

address_book.append({
    'Name': 'Hermione Granger',
    'Phone': 'x7345',
    'Street': '12 Grimmauld Place',
    'City': 'London',
    'State': 'England',
    'Email': 'hgranger@hogwarts.edu'
})

print("Address book when added with Harry Potter and Hermione Granger:", address_book)

def filter_by_city(city, address_book):
    people = []
    for entry in address_book:
        if entry['City'] == city:
            people.append(entry)

    return people

print(address_book)

print(filter_by_city('Harry Potter', address_book))

print("People who live in Saint Paul:", filter_by_city('Saint Paul', address_book))