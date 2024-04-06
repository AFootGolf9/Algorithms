package addTwoNumbers;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode out = l1;

        while(l1 != null && l2 != null){
            l1.val += l2.val;
            if(l1.val >= 10){
                l1.val -= 10;
                if(l1.next == null){
                    l1.next = new ListNode(1);
                }else{
                    l1.next.val++;
                }
            }
            if(l1.next == null && l2.next != null){
                l1.next = new ListNode(0);
            }
            if(l2.next == null && l1.next != null){
                l2.next = new ListNode(0);
            }
            l1 = l1.next;
            l2 = l2.next;
        }

        return out;
    }
}
