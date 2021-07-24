class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_friend_coming_time = times[targetFriend][0]
        coming_dict = {}
        leave_dict = {}
           
        for friend, value in enumerate(times):
            coming, leave = value
            coming_dict.setdefault(coming, friend)
            leave_dict.setdefault(leave, [])
            leave_dict[leave].append(friend)
        
        chair_list = [False] * len(times)
        friend_char_dict = {}
        coming_order_list = sorted(list(coming_dict.keys()))
        time = 0
        while True:
            if time in leave_dict:
                for leave_friend in leave_dict[time]:
                    print(friend_char_dict[leave_friend], "release")
                    chair_list[friend_char_dict[leave_friend]] = False
            if time in coming_dict:
                friend = coming_dict[time]
                min_chair = len(chair_list)
                for i, chair in enumerate(chair_list):
                    if not chair:
                        min_chair = i
                        break
                friend_char_dict[friend] = i
                print(friend_char_dict[friend], "accquire")
                if friend == targetFriend:
                    return i
                chair_list[i] = True
            time+=1
            
            