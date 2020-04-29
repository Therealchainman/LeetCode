class FirstUnique {
    list<int> queue;
    unordered_map<int, list<int>::iterator> map;
public:
    FirstUnique(vector<int>& nums) {
        for (int num : nums) {
            add(num);
        }
    }
    
    int showFirstUnique() {
        if (queue.size() > 0) {
            return queue.front();
        }
        return -1;
    }
    
    void add(int value) {
        if (map.find(value) == map.end()) {
            queue.push_back(value);
            auto it = queue.end();
            --it;
            map.insert( {value, it} );
        } else {
            auto it = map[value];
            if (it != queue.end()) {
                queue.erase(it);
                map[value] = queue.end();
            }
        }
    }  
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */