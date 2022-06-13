class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(!head || !head->next || k == 1){
            return head;
        }
        int count = 0;
        ListNode* curr = head;
        while(curr){
            count++;
            curr = curr->next;
        }
        ListNode* prev = NULL;
        ListNode* next = NULL;
        ListNode* newHead = NULL;
        ListNode* x = NULL;
        ListNode* y;
        curr = head;
        while(count>=k){
            for(int i = 0; i<k; i++){
                next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
            if(!newHead){
                newHead = prev;
            }
            if(x){
                x->next = prev;
            }
            y->next = curr;
            x = y;
            y = curr;
            prev = NULL;
            count -= k;
        }
        return newHead;
    }
    
};
