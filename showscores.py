with open('scores.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                        print("Name: {} and Score: {}".format(parts[0].capitalize(),parts[1]))