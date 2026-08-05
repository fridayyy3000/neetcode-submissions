class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        max_area = 0
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            if max_area < area:
                max_area = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area