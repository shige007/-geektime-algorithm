# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = [0]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics 数组 
#  👍 709 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 列表digits从后向前访问，range()函数左闭右开
        for i in range(len(digits) - 1, -1, -1):
            # 末尾元素加1
            digits[i] += 1
            # 末尾元素取余
            digits[i] = digits[i] % 10
            # 余数为0，继续执行for循环；余数不为0，直接返回digits
            if digits[i] != 0:
                return digits
        # 碰到元素都为9，申请一个列表res，元素都为0,长度是len(digits) + 1
        # digits = [9, 9]
        # [9, 9 + 1] => [9, 10] =>[9 + 1, 10] => [10, 10] => [1, 0, 0]
        res = [0] * (len(digits) + 1)
        # res第一个值设为1
        res[0] = 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
