class Solution {
public:
    ListNode* reverseList(ListNode* head) {
      //iterative method  
      /*if(!head || !head->next){
            return head;
        }
        ListNode *prev=NULL, *curr=head, *next=head->next;
        while(next){
            curr->next=prev;
            prev=curr;
            curr=next;
            next=next->next;
        }
        curr->next=prev;
        return curr;*/
      
      //recursive method
      /*if(!head || !head->next){
            return head;
        }
        auto ans =reverseList(head->next);
        head->next->next=head;
        head->next=NULL;
        return ans;*/
    }
};
