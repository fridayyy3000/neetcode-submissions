class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            # Skip spaces and punctuation from left
            if not s[i].isalnum():
                i += 1
                continue

            # Skip spaces and punctuation from right
            if not s[j].isalnum():
                j -= 1
                continue

            # Compare characters ignoring case
            if s[i].lower() != s[j].lower():
                return False

            # Move both pointers inward
            i += 1
            j -= 1

        return True