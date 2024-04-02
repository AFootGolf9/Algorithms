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
        ListNode temp = l1;
        int sum = 0;
        int power = 1;

        while(temp != null){
            sum += temp.val * power;
            power = power * 10;
            temp = temp.next;
        }

        temp = l2;
        power = 1;

        while(temp != null){
            sum += temp.val * power;
            power = power * 10;
            temp = temp.next;
        }

        String numString = Integer.toString(sum);

        for(int i = 0; i < numString.length(); i++){
            temp = new ListNode(numString.charAt(i) - '0', temp);
        }

        return temp;
    }
}
