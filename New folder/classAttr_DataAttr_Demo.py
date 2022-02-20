class Counter:
      overall_Total = 0

      def __init__(self):
            self.myTotal = 0

      def increment(self):
            Counter.overall_Total += 1
            self.myTotal += 1
            print("Counter.overall_Total := ", Counter.overall_Total)
            print("self.myTotal := ", self.myTotal )
            
a = Counter()
b = Counter()

a.increment()
b.increment()
b.increment()

c = Counter()
d = Counter()

c.increment()
d.increment()
