class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = list()
        for i in range(len(matrix[0])):
            row = list()
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            ans.append(row)
        return ans
