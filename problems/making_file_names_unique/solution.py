class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        for i in range(len(names)):
            folder = names[i]
            if folder not in seen:
                seen[folder] = 0
            else:
                seen[folder] += 1
                new_folder = f"{folder}({seen[folder]})"
                while new_folder in seen:
                    seen[folder] += 1
                    new_folder = f"{folder}({seen[folder]})"
                seen[new_folder] = 0
                names[i] = new_folder
        return names
            
        
"""
{wano: 5, wano(1): 0, wano(3): 0, wano(2): 0, wano(4): 0, wano(5): 0, wano(3)(1): 0}
"""