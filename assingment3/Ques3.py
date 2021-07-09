# Print all the unique elements in the following list
# fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']
fifa = ['Italy', 'Argentina', 'Germany', 'Brazil', 'France',
        'Brazil', 'Italy', 'Spain', 'Germany', 'France']
count = 0
for country in fifa:
    for selected_country in fifa:
        if country == selected_country:
            count += 1
    if count <= 1:
        print(country)
    count = 0
