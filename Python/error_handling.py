def get_days_alive(person):
    try:
        days = person['age']*365
        print(f'{person["name"]} has been alive for {days} days')
    except KeyError as exc:
        print('Missing key: ',exc)
    except TypeError:
        print('Person is not a dictionary')
    except:
        print('something else went wrong')

# {'name': 'jenn', 'age': 10}


# Raise your own exception

