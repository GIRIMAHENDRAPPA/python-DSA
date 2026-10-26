def majority(nums):
    cand1, cand2 =None, None
    cnt1, cnt2 =0, 0

    for num in nums:
        if num == cand1:
            cnt1 += 1
        elif num == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1 = num
            cnt1 = 1
        elif cnt2 == 0:
            cand2 = num
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1
            
        res = []
        n = len(nums)
        if nums.count(cand1) > n // 3:
            res.append(cand1)
        if cand2 !=cand1 and nums.count(cand2) > n // 3:
            res.append(cand2)
        return res
print(majority([2,2,1,1,1,2,2]))