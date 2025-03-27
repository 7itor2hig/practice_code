class GameNightPlanner:
    def __init__(self, game_title):
        self.game_title = game_title
        self.gamers = []

    def add_gamer(self, gamer):
        if 'name' not in gamer or 'availability' not in gamer:
            print("Invalid dictionary input")
            return
        self.gamers.append(gamer)

    def build_daily_frequency_table(self):
        daily_frequency_table = {
            'Monday': 0, 'Tuesday': 0, 'Wednesday': 0,
            'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0
        }

        for gamer in self.gamers:
            for day in gamer['availability']:
                daily_frequency_table[day] += 1

        return daily_frequency_table

    def find_best_night(self, availability_table):
        return max(availability_table.items(), key=lambda item: item[1])

    def find_second_best_night(self, first_game_night, availability_table):
        second_best = ("", 0)
        for day, count in availability_table.items():
            if day == first_game_night[0]:
                continue
            if count > second_best[1]:
                second_best = (day, count)
        return second_best

    def available_on_night(self, night):
        return [g['name'] for g in self.gamers if night in g['availability']]

    def send_email(self, gamers_list, day):
        for gamer in gamers_list:
            print(f"Hello {gamer}, we will be playing {self.game_title} on {day}. Hope to see you there!\n")

    def run_planning(self):
        availability_table = self.build_daily_frequency_table()

        first_night = self.find_best_night(availability_table)
        second_night = self.find_second_best_night(first_night, availability_table)

        attendees_first = self.available_on_night(first_night[0])
        attendees_second = self.available_on_night(second_night[0])

        print(f"\nPrimary Game Night: {first_night[0]} ({first_night[1]} players)")
        self.send_email(attendees_first, first_night[0])

        print(f"\nSecondary Game Night: {second_night[0]} ({second_night[1]} players)")
        self.send_email(attendees_second, second_night[0])
