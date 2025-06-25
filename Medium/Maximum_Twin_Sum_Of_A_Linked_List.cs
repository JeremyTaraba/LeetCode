/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public int PairSum(ListNode head) {
        int max_sum = 0;
        Stack<int> stack = new Stack<int>();
        ListNode cur = head;
        ListNode runner = head;

        while(runner != null){
            stack.Push(cur.val);
            cur = cur.next;
            runner = runner.next.next;
        }

        while(cur != null){
            max_sum = Math.Max(max_sum, stack.Pop() + cur.val);
            cur = cur.next;
        }




        return max_sum;
    }
}