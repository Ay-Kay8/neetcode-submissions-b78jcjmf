class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            print(f"n = {n}")
            new_perms = []

            print(f"perms = {perms}")
            for p in perms:
                print(f"\tFinding permutations for {p} by inserting {n} everywhere")
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)

                print(f"\tnew_perms = {new_perms}")
            perms = new_perms

        return perms