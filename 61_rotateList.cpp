// 61. Rotate List

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
    ListNode* rotateOnce(ListNode* head){
        ListNode* first = head;
        ListNode* p1 = head->next;
        int temp = head->val;
        int s;
        
        while(p1->next!=nullptr){
            s = p1->val;
            p1->val = temp;
            temp = s;
            p1 = p1->next;
        }
        s = p1->val;
        p1->val = temp;
        first->val = s;
        
        return head;
    }
    
    ListNode* rotateRight(ListNode* head, int k) {
       if(head==nullptr || head->next==nullptr)
           return head;
        
        int l = 0;
        ListNode* p1 = head;
        
        while(p1!=nullptr){
            l+=1;
            p1 = p1->next;
        }
        
        if(k%l==0)
            return head;
        
        k = k%l;
        
        for(int i=0;i<k;i++){
           head = rotateOnce(head); 
        }
        return head;
    }
};
