import unittest
from commits import Commit

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.commits = Commit()

    def test_commit_max(self):
        result = self.commits.max([1,2,3,4])
        self.assertEqual(4, result)        

    def test_commit_min(self):
        result = self.commits.min([1,2,3,4])
        self.assertEqual(1, result)
        
    def test_commit_convert_date(self):
        result = self.commits.convert_date('20171201')
        self.assertEqual('2017-12-01 00:00:00', str(result))
      
    def test_commit_days_between(self):
        date1 = self.commits.convert_date('20171201')
        date2 = self.commits.convert_date('20171231')
        result = self.commits.days_between(date1, date2)
        self.assertEqual(30, result)

    def test_commit_store_authors(self):
        result = self.commits.store_authors( 'Freddie')
        self.assertEqual(1, result)

    def test_commit_store_dates(self):
        result = self.commits.store_dates( '20161210')
        self.assertEqual(1, result)

    def test_commit_count_commit_types(self):           
        result = self.commits.count_commit_types({'A ...', 'B...', 'D bbb' , 'M odify'})
        self.assertEqual(1, result)        


if __name__ == '__main__':
    unittest.main()
