from treasure import Treasure
from heap import Heap
class CrewMate:
    def __init__(self) -> None:
        self.current_load = 0
        self.last_update = 0
        self.treasure_jo_abhi_mere_pass_hai = Heap(self.compare, [])
        self.treasure_jo_proccess_ho_chuke = []

    def compare(self, a: Treasure, b: Treasure) -> bool:
        cur_time = self.last_update
        a_w = cur_time - a.arrival_time
        b_w = cur_time - b.arrival_time
        a_priority = a_w - a.size
        b_priority = b_w - b.size
        if a_priority == b_priority:
            return a.id < b.id
        return a_priority > b_priority

    def add_tresure_to_crewMate(self, treasure_to_insert: Treasure):
        in_time = treasure_to_insert.arrival_time
        time_diff = in_time - self.last_update
        

        while time_diff > 0 and not self.treasure_jo_abhi_mere_pass_hai.empty():
            if self.treasure_jo_abhi_mere_pass_hai.arr[0].size > time_diff:
                self.treasure_jo_abhi_mere_pass_hai.arr[0].size -= time_diff
                time_diff = 0
                break
            else:
                treasure_proccessed = self.treasure_jo_abhi_mere_pass_hai.extract()
                treasure_proccessed.completion_time = self.last_update + treasure_proccessed.size
                self.last_update += treasure_proccessed.size
                self.treasure_jo_proccess_ho_chuke.append(treasure_proccessed)
                time_diff -= treasure_proccessed.size
        
        self.last_update = in_time
        self.treasure_jo_abhi_mere_pass_hai.insert(treasure_to_insert)
        if self.current_load > treasure_to_insert.arrival_time:
            self.current_load+=treasure_to_insert.size
        else:
            self.current_load=(treasure_to_insert.size + treasure_to_insert.arrival_time)

    def get_tresures_complition_time(self):
        store_last_update_time = self.last_update
        temp = []
        
        total_treasures = len(self.treasure_jo_abhi_mere_pass_hai.arr)
        
        while not self.treasure_jo_abhi_mere_pass_hai.empty():
            t_jiska_complition_time_update_krna_hai = self.treasure_jo_abhi_mere_pass_hai.extract()
            t_jiska_complition_time_update_krna_hai.completion_time = self.last_update + t_jiska_complition_time_update_krna_hai.size
            self.last_update = t_jiska_complition_time_update_krna_hai.completion_time
            temp.append(t_jiska_complition_time_update_krna_hai)

        self.treasure_jo_abhi_mere_pass_hai = Heap(self.compare, temp)
        helper = temp + self.treasure_jo_proccess_ho_chuke
        self.last_update = store_last_update_time
        helper = sorted(helper, key = lambda a: a.id)

        return helper
