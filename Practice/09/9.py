def meeting_search():
 
        t = input_time()
        time1 = t[0] * 60 + t[1]

        t = input_time()
        time2 = t[0] * 60 + t[1]

        meeting = (('Встреча состоится', 'Встреча не состоится')
                  [time1 > time2 + 15],
                  ('Встреча состоится', 'Встреча не состоится')
                  [time2 > time1 + 15])[time1 < time2]
        print(meeting)

        
def input_time():
    t = input("Введите время: ")
    numbers = t.split(':')
    numbers = list(filter(None, numbers))
    numbers = list(map(int, numbers))
meeting_search()