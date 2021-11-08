class Pokemon():
    def __init__(self, starter, starter_type, starter_weakness, starter_health, starter_hit_points):
            self.starter = starter
            self.starter_type = starter_type
            self.starter_weakness = starter_weakness
            self.starter_health = starter_health
            self.starter_hit_points = starter_hit_points




class Player():
    def __init__(self, fpath):
      
        with open(fpath, "r", encoding="utf-8") as f:  
            self.pokemon = {}
            for line in f:
                x = line.strip().split(",")
                starter = x[0]
                starter_type = x[1]
                starter_weakness = x[2]
                starter_health = x[3]
                starter_hit_points = x[4]
                self.pokemon[starter] = starter_type, starter_weakness, starter_health, starter_hit_points
               