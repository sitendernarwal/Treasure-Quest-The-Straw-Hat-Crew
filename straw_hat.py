import crewmate
import heap
import treasure 

def comp(a, b):
    return a.current_load < b.current_load

class StrawHatTreasury:
    def __init__(self, m):
        mates_we_have = [crewmate.CrewMate() for _ in range(m)]
        self.mates = heap.Heap(comp, mates_we_have)
        self.t_count = 0
        self.m_count = m
        self.temp_t = []

    def add_treasure(self, treasure:treasure.Treasure):
        crew_mate_with_least_load = self.mates.extract()
        self.t_count += 1
        self.temp_t.append(treasure)
        crew_mate_with_least_load.add_tresure_to_crewMate(treasure)
        self.mates.insert(crew_mate_with_least_load)

    def get_completion_time(self):
        ans = []
        if self.t_count <= self.m_count:
            for t in self.temp_t:
                t.completion_time = t.size + t.arrival_time
                ans.append(t)
        else:
            for crewmaets in self.mates.arr:
                treasures = crewmaets.get_tresures_complition_time()
                ans.extend(treasures) 
        def comparator(x):
            return x.id
        ans=sorted(ans, key=comparator)
        return ans