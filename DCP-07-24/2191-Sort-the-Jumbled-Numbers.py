class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_dict = {i: mapping[i] for i in range(10)}

        def map_with_mapping(num):
            return int(''.join(str(mapping_dict[int(digit)]) for digit in str(num)))

        nums.sort(key=lambda x: map_with_mapping(x))
        return nums