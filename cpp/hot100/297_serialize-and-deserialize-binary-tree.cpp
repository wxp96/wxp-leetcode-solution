#include <iostream>
#include <vector>
#include <queue> 

using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Codec {
public:
    void reserialize(TreeNode* root,string &str){
        if (! root){
            str+="#,";
        }else{
            str+=to_string(root->val);
            str+=",";
            reserialize(root->left,str);
            reserialize(root->right,str);
        }
        
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string str;
        reserialize(root,str);
        return str;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        queue q;
    }
};