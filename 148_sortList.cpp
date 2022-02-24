// 148. Sort List

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {    
public:
    ListNode* getMid(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while(fast!=nullptr and fast->next!=nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
    
    ListNode* merge(ListNode* left, ListNode* right){
        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;
        
        while(left!=nullptr and right!=nullptr){
            if(left->val<=right->val){
                tail->next = left;
                left = left->next;
            }
            else{
                tail->next = right;
                right = right->next;
            }
                
            tail = tail->next;
        }
        
        if(left!=nullptr)
            tail->next = left;
        if(right!=nullptr)
            tail->next = right;
        
        return dummy->next;
        
    }
    
    ListNode* sortList(ListNode* head) {
        
        if(head==nullptr || head->next==nullptr)
            return head;
        
        ListNode* left = head;
        ListNode* right = getMid(head);
        ListNode* temp = right->next;
        right->next = nullptr;
        right = temp;
        
        left = sortList(left);
        right = sortList(right);
        
        return merge(left,right);
        
    }
};
