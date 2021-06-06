class Solution:
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        s_mat = lambda x: sum([sum(l) for l in mat])
        if s_mat(mat) != s_mat(target):
            return False
        
        def rotate(matrix):
            h, w = len(matrix), len(matrix[0]) #矩阵旋转必然是方阵，所以此处可以只求一个
            #沿对角线对称
            for i in range(h):
                for j in range(i, h): #注意此处只对矩阵右半部分操作，否则会重复换位
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            #水平方向翻转

            for i in range(h):
                start = 0
                end = h-1
                while start<end:
                    matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                    start+=1
                    end-=1

        def compare(mat, target):
            for x in range(len(mat)):
                for y in range(len(mat[0])):
                    if mat[x][y] != target[x][y]:
                        return False
            return True
        
        if compare(mat, target):
            return True
        print(mat)
        print(target)
        for _ in range(3):
            rotate(mat)
            print(mat)
            print(target)
            if compare(mat, target):
                return True
        return False
            
        