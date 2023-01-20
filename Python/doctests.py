def get_days_alive(person):
    '''
    accepts a dictionary with a name and age of a person, and tells you how many days the number of years equates to

    >>> get_days_alive({'name': 'jenn', 'age': 10})
    jenn has been alive for 3650 days

    >>> get_days_alive({'age': 10})
    Missing key: 'name'

    >>> get_days_alive({'name': 'jenn'})
    Missing key: 'age'

    >>> get_days_alive('hi')
    Person is not a dictionary
    '''
    try:
        days = person['age']*365
        print(f'{person["name"]} has been alive for {days} days')
    except KeyError as exc:
        print('Missing key:',exc)
    except TypeError:
        print('Person is not a dictionary')
    except:
        print('something else went wrong')

# {'name': 'jenn', 'age': 10}