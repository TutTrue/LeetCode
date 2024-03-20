/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (!list1) return list2;
    if (!list2) return list1;
    if (list1->val > list2->val) {
        struct ListNode *temp = list1;
        list1 = list2;
        list2 = temp;
    }
    list1->next = mergeTwoLists(list1->next, list2);
    return list1;
}
