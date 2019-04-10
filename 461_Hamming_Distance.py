# TODO : 속도 개선
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = "{0:b}".format(x).zfill(31)
        bin_y = "{0:b}".format(y).zfill(31)

        zip_x_y = zip(bin_x, bin_y)

        # diff_count = len([_x for _x, _y in zip_x_y if _x != _y])
        diff_count = 0

        for i in range(0, 31):
            if bin_x[i] != bin_y[i]:
                diff_count += 1

        return diff_count