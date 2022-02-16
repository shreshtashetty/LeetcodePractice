// 24. Swap Nodes in Pairs

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
    ListNode* swapPairs(ListNode* head) {
        if(head==nullptr or head->next==nullptr)
            return head;
        
        ListNode* node1 = head;
        ListNode* node2 = head->next;
        ListNode* node3 = head->next->next;
        node2->next = node1;
        
        ListNode* node4 = swapPairs(node3);
        node1->next = node4;
        
        return node2;
        
    }
};
