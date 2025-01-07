def findMedianSortedArrays(nums1, nums2):
        total_length = len(nums1) + len(nums2)
        is_even = total_length % 2 == 0
        median = 0
        half = int(total_length/2)
        print("HALF : ",half)
        if not is_even:
            print("IS BOT EVEN")
            if len(nums1) < half:
                print("CHECK 1")
                median = nums1[half-1]
            else:
                print("CHECK 2")
                median = nums2[half-1]    
        else:
            print("IS EVEN")
            if len(nums1) < half:
                print("CHECK 1")
                median = nums1[half] + nums1[half-1]
            elif len(nums1) > half:
                print("CHECK 2")
                median = nums2[half] + nums2[half+1]
            else:
                print("CHECK 3")
                median = nums1[half-1] + nums2[0]   
            median = median / 2       
        return  median  
    
print("RESULT : ", findMedianSortedArrays([1,3],[2]))   