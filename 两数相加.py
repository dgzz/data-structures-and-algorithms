# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add_list = []
        l1_int = self.changeList(l1)
        l2_int = self.changeList(l2)
        add = l1_int + l2_int
        add = str(add)
        for i in add:
            i = int(i)
            add_list.append(i)
        return add_list

    def changeList(self,lists):
        list1 = list(reversed(lists))
        str_list = []
        for i in list1:
            i = str(i)
            str_list.append(i)
        str1 = "".join(str_list)
        str1 = int(str1)
        return str1

solution = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
print(solution.addTwoNumbers(l1, l2))