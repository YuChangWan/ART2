class Cluster:
    def __init__(self, first_member):
        self.members = [first_member]
        self.size = 1
        self.weight = first_member

    def append(self, new_member):
        self.members.append(new_member)
        new_w0 = (new_member[0] + self.weight[0]*self.size)/(self.size+1)
        new_w1 = (new_member[1] + self.weight[1]*self.size)/(self.size+1)
        self.weight = (new_w0, new_w1)
        self.size += 1
        
    def distance(self, pattern):
        return abs(pattern[0]-self.weight[0]) + abs(pattern[1]-self.weight[1])


if __name__ == '__main__':
    patterns = [(1.5, 1.3),
                (1.9, 1.4),
                (0.7, 0.4),
                (1.5, 1.9),
                (0.6, 1.2),
                (0.0, 1.4),
                (1.5, 0.5),
                (1.4, 1.8),
                (1.3, 0.8),
                (1.0, 0.1)]

    threshold = 1.5
    clusters = []
    first_pattern = patterns.pop(0)
    clusters.append(Cluster(first_pattern))

    for p in patterns:
        distances = []
        for c in clusters:
            distances.append(c.distance(p))
            
        min_distance = min(distances)
        winner = distances.index(min_distance)
        if min_distance < threshold:
            clusters[winner].append(p)
        else:
            clusters.append(Cluster(p))

    for c in clusters:
        print(c.members)
        print(c.weight)
        print()
