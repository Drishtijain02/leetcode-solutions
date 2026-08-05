class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count =0
        
        def countPairs(arr: List[int], low: int, mid: int, high: int):
            nonlocal count
            right=mid+1
            for i in range(low,mid+1):
                while(right<= high and arr[i]>2*arr[right]):
                    right+=1
                count = count +(right-(mid+1))
            return count
        def merge_sort(arr: List[int], low: int, high: int):
            if low >= high:
                return
            mid = (low + high) // 2
            merge_sort(arr, low, mid)
            merge_sort(arr, mid + 1, high)
            countPairs(arr,low,mid,high)
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1

            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
            
        merge_sort(nums,0,len(nums)-1)
        return count



        