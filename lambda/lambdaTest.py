import unittest
import lambdaLib



class TestStringMethods(unittest.TestCase):
    # def setUp(self):
    #     self.txt = lambdaLib.getData()

    def test_get_data(self):
        txt = lambdaLib.getData()
        self.assertEqual(txt[0:6], '[info]')

    def test_time_ranges(self):
        text = "21:51:02.668 [sca-execon-co aramers$-ihu}!2]*21:51:12.082 [scal21:51:24.950"
        timeRanges = lambdaLib.findTimePeriod(text)
        self.assertEqual(timeRanges, ['21:51:02.668', '21:51:12.082', '21:51:24.950'])

    def test_datetime_convert(self):
        time = lambdaLib.datetime_convert("21:51:02")
        self.assertEqual(time.hour, 21)
        self.assertEqual(time.minute, 51)
        self.assertEqual(time.second, 2)

    def test_datetime_c(self):
        t1 = lambdaLib.datetime_convert("19:51:22")
        t2 = lambdaLib.datetime_convert("21:48:03")
        self.assertTrue(lambdaLib.is_in_range(t1, t2))
        self.assertFalse(lambdaLib.is_in_range(t2, t1))

    def test_split(self):
        ta = ["[info]","[warn]","21:51:01.824","[success]"]
        size = len(lambdaLib.remove_front_nonlog(ta))
        self.assertEqual(size, 2)


if __name__ == '__main__':
    unittest.main()

