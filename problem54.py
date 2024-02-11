with open('0054_poker.txt', 'r') as handle:
    data = handle.read()
    data = data.split('\n')
    data = data[:-1]

hand1 = 0
hand2 = 0

class Poker:
    def __init__(self, line):
        self.vals = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14}
        self.line = line
        self.player1 = self.line.split(' ')[0:5]
        self.player2 = self.line.split(' ')[5:]
        self.player1_suits = {x[1] for x in self.player1}
        self.player2_suits = {x[1] for x in self.player2}
        self.player1_values = sorted([self.vals[x[0]] for x in self.player1])
        self.player2_values = sorted([self.vals[x[0]] for x in self.player2])
        self.player1_uniq_v = set(self.player1_values)
        self.player2_uniq_v = set(self.player2_values)
    
    def royal_flush(self):
        royal_flush_values = [10, 11, 12, 13, 14]
        if len(self.player1_suits) == 1 and self.player1_values == royal_flush_values:
            return 1, 0
        if len(self.player2_suits) == 1 and self.player2_values == royal_flush_values:
            return 0, 1
        return 0, 0
    
    def straight_flush(self):
        p1, p2 = 0, 0
        if len(self.player1_suits) == 1:
            if len(self.player1_uniq_v) == 5 and self.player1_values[-1] - self.player1_values[0] == 4:
                p1 = 1
        if len(self.player2_suits) == 1:
            if len(self.player2_uniq_v) == 5 and self.player2_values[-1] - self.player1_values[0] == 4:
                p2 = 1
        return p1, p2
    
    def four_of_a_kind(self):
        p1, p2 = 0, 0
        if self.player1_values.count(self.player1_values[2]) == 4:
            a = self.player1_values[2]
            p1 = 1
        if self.player2_values.count(self.player2_values[2]) == 4:
            b = self.player2_values[2]
            p2 = 1
        if p1 == 1 and p2 == 1:
            if a > b:
                return 1,0
            else: 
                return 0,1
        return p1, p2
    
    def full_house(self):
        p1, p2 = 0, 0
        if len(self.player1_uniq_v) == 2 and self.player1_values.count(self.player1_values[2]) == 3:
            a = self.player1_values[2]
            p1 = 1
        if len(self.player2_uniq_v) == 2 and self.player2_values.count(self.player2_values[2]) == 3:
            b = self.player2_values[2]
            p2 = 1
        if (p1 == 1) and (p2 == 1):
            if a > b:
                return 1, 0
            else: 
                return 0,1
        return p1, p2
    
    def flush(self):
        p1, p2 = 0, 0
        if len(self.player1_suits) == 1:
            p1 = 1
        if len(self.player2_suits) == 1:
            p2 = 1
        return p1, p2
    
    def straight(self):
        p1, p2 = 0, 0
        if len(self.player1_uniq_v) == 5 and self.player1_values[-1] - self.player1_values[0] == 4:
            p1 = 1
        if len(self.player2_uniq_v) == 5 and self.player2_values[-1] - self.player2_values[0] == 4:
            p2 = 1
        return p1, p2
    
    def three_of_a_kind(self):
        p1, p2 = 0, 0
        if self.player1_values.count(self.player1_values[2]) == 3:
            a = self.player1_values[2]
            p1 = 1
        if self.player2_values.count(self.player2_values[2]) == 3:
            b = self.player2_values[2]
            p2 = 1
        if p1 == 1 and p2 == 1:
            if a > b:
                return 1, 0
            else: 
                return 0,1
        return p1, p2
    
    def two_pairs(self):
        p1, p2 = 0, 0
        if len(self.player1_uniq_v) == 3:
            if self.player1_values.count(self.player1_values[1]) == 2:
                p1 = 1
                a = [self.player1_values[1], self.player1_values[3]]
        if len(self.player2_uniq_v) == 3:
            if self.player2_values.count(self.player2_values[1]) == 2:
                p2 = 1
                b = [self.player2_values[1], self.player2_values[3]]
        if p1 == 1 and p2 == 1:
            if max(a) > max(b):
                return 1, 0
            if max(b) > max(a):
                return 0, 1
            if min(a) > min(b):
                return 1, 0
            if min(b) > min(a):
                return 0, 1
        return p1, p2
    
    def one_pair(self):
        p1, p2 = 0, 0
        if len(self.player1_uniq_v) == 4:
            p1 = 1
        if len(self.player2_uniq_v) == 4:
            p2 = 1
        if p1 == 1 and p2 == 1:
            for i in range(4):
                if self.player1_values.count(self.player1_values[i]) == 2:
                    a = self.player1_values[i]
                if self.player2_values.count(self.player2_values[i]) == 2:
                    b = self.player2_values[i]
            if a > b:
                return 1, 0
            if b > a:
                return 0, 1
        return p1, p2
    
    def high_card(self):
        p1, p2 = 0, 0
        vals1 = sorted(self.player1_values, reverse=True)
        vals2 = sorted(self.player2_values, reverse=True)
        for i in range(5):
            if vals1[i] != vals2[i]:
                if vals1[i] > vals2[i]:
                    return 1, 0
                else:
                    return 0, 1
        return p1, p2
    
    def solver(self):
        global hand1
        global hand2
        list_of_methods = [self.royal_flush(), 
                           self.straight_flush(), 
                           self.four_of_a_kind(), 
                           self.full_house(),
                           self.flush(),
                           self.straight(),
                           self.three_of_a_kind(),
                           self.two_pairs(),
                           self.one_pair(),
                           self.high_card()]
                           
        for method in list_of_methods:
            if method[0] != method[1]:
                hand1 += method[0]
                hand2 += method[1]
                return method[0], method[1]
        return 0
    
for line in data:
    a = Poker(line)
    b = a.solver()
 
print(hand1, hand2)