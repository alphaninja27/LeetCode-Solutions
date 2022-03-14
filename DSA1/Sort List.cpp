class Solution {
public:
    ListNode* sortList(ListNode* head) {
        return merge_sort(head);
    }
    ListNode* merge_sort(ListNode* head){
        if(!head || !head->next){
            return head;
        }
        if(!head->next->next){
            if(head->next->val < head->val){
                ListNode* next_node = head->next;
                next_node->next = head;
                head->next=NULL;
                head=next_node;
            }
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* node2 = merge_sort(slow->next);
        slow->next=NULL;
        ListNode* node1 = merge_sort(head);
        return merge(node1,node2);
    }
    ListNode* merge(ListNode* l, ListNode* r){
        if(l && r){
            if(l->val <= r->val){
                l->next=merge(l->next,r);
                return l;
            }
            else{
                r->next=merge(r->next,l);
                return r;
            }
        }
        return (!l ? r:l);
    }
};
