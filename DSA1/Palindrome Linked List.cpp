class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *slow = head;
        ListNode *fast = head;
        
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode *prev = NULL;
        ListNode *temp;
        while(slow){
            temp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = temp;
        }
        ListNode *left = head;
        ListNode *right = prev;
        while(right){
            if(left->val != right->val){
                return false;
            }
            left = left->next;
            right = right->next;
        }
        return true;
        
    }
};
