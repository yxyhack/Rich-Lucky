import numpy as np

class Person:
    def __init__(self, id):
        self.id = id
        self.ability = round(np.random.normal(loc=0.5, scale=0.09), 2)
        self.wealth = 100
        self.x = np.random.randint(200)
        self.y = np.random.randint(200)

class Event:
    def __init__(self):
        self.x = np.random.randint(200)
        self.y = np.random.randint(200)

class WealthDistribution:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.people = []
        self.events = {"wealth": [], "loss": []}
        self.highest_wealth = []
        self.highest_ability = []
        self.lowest_ability = []

    def create_people(self, num_people):
        for i in range(num_people):
            person = Person(i)
            self.people.append(person)

    def create_events(self, num_events):
        for i in range(num_events):
            wealth_event = Event()
            loss_event = Event()
            self.events["wealth"].append(wealth_event)
            self.events["loss"].append(loss_event)

    def run(self):
        for round_num in range(self.total_rounds):
            # 改变事件的位置
            for event in self.events["wealth"]:
                event.x = np.random.randint(200)
                event.y = np.random.randint(200)
            for event in self.events["loss"]:
                event.x = np.random.randint(200)
                event.y = np.random.randint(200)
            # 财富分配
            for person in self.people:
                if person.wealth > 0: # 只有有钱人才参加财富分配（因为所有人都可以参加分配，有钱人已经有很多钱了，所以不会因为分配而变差）
                    for event_type in ["wealth", "loss"]:
                        for event in self.events[event_type]:
                            if person.x == event.x and person.y == event.y:
                                if event_type == "wealth":
                                    if np.random.random() <= person.ability:
                                        person.wealth *= 2
                                elif event_type == "loss":
                                    person.wealth *= 0.75
            # 获取当前最高的财富值、能力值最高的和最低的人
            self.highest_wealth = sorted(self.people, key=lambda x: x.wealth, reverse=True)[:30]
            self.highest_ability = sorted(self.people, key=lambda x: x.ability, reverse=True)[:30]
            self.lowest_ability = sorted(self.people, key=lambda x: x.ability)[:30]
            # 每10轮输出信息
            if round_num % 10 == 0:
                print(f"财富分配轮数： {round_num}")
                print("30个财富值最多的人:")
                for person in self.highest_wealth:
                    print(f"编号: {person.id}, 财富值: {person.wealth}, 能力值: {person.ability} (财富值最高人群)")
                print("30个能力值最低的人:")
                for person in self.lowest_ability:
                    print(f"编号: {person.id}, 财富值: {person.wealth}, 能力值: {person.ability} (能力值最低人群)")
                print("30个能力值最高的人:")
                for person in self.highest_ability:
                    print(f"编号: {person.id}, 财富值: {person.wealth}, 能力值: {person.ability} (能力值最高人群)")
                

total_rounds = input("请输入财富总共需要分配多少轮: ")
simulation = WealthDistribution(int(total_rounds))
simulation.create_people(10000)
simulation.create_events(1000)
simulation.run()
