// 133. Clone Graph

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

*/

class Solution {
public:
    unordered_map<Node*, Node*> oldToNew;
    
    Node* cloneGraph(Node* node) {
        
        if(node!=nullptr)
            return clone(node);
        else
            return node;
    }
    
    Node* clone(Node* node){
            
        if(oldToNew.find(node)!=oldToNew.end())
            return oldToNew[node];

        Node* copy = new Node(node->val);
        oldToNew[node] = copy;

        for(int i=0;i<(node->neighbors).size();i++)
            copy->neighbors.push_back(clone((node->neighbors)[i]));

        return copy;
            
        }
};
