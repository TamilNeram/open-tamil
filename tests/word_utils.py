# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
# 
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from __future__ import print_function
from opentamiltests import *
from tamil import wordutils

import math

class TestWordUtils(unittest.TestCase):
    def test_perms( self ):
        res = [u'123',u'132',u'213',u'231',u'312',u'321']
        self.assertEqual( list(wordutils.permutations(u'1 2 3'.split(u' '))),res)
        
    def test_perms_length(self):
        count = 0
        for perm in wordutils.permutations('1 2 3 4 5 6'.split(' ')):
            count += 1
        self.assertEqual(count,math.factorial(6))
        
    def test_tamil_perms( self ):
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.permutations([u'த',u'மி',u'ழ்'])),res)
     
    def test_tamil_perms2( self ):
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.tamil_permutations(res[0])),res)
    
    @skip_python2_6
    def test_anagram_xception(self):
        mtObj = wordutils.DictionaryWithPredicate( False )
        with self.assertRaises(Exception):
            list( wordutils.anagrams( u'உபயொகிக்க!',mtObj) )
    
    def test_anagram_all_or_nothing(self):
        # all words are in dictionary..
        dictPred = wordutils.DictionaryWithPredicate(lambda x: True)
        self.assertTrue( dictPred.isWord('not a word but OK to slack off!') )
        
        res = [u'தமிழ்',u'தழ்மி',u'மிதழ்',u'மிழ்த',u'ழ்தமி',u'ழ்மித']
        self.assertEqual( list(wordutils.anagrams(u'தமிழ்',dictPred)), res )
        
        # none of words match
        negDictPred = wordutils.DictionaryWithPredicate(lambda x: False)
        self.assertEqual( list(wordutils.anagrams(res[0],negDictPred)),[] )
        
    def test_perms_as_string_is_OK(self):
        actual = list( wordutils.permutations( u'அதுசரம்' ) )
        self.assertEqual(len(actual),math.factorial(5))
    
    def test_combinations(self):
        word = u"சவால்";
        self.assertEqual( len(list(filter(len,list(wordutils.combinations(word))))), 8-1 )

    def test_palindrome(self):
        words = [u"a",u"abba","xkcd","vinavi","1001",u"அதுஅ",u"சரம்ரச"]
        expected = [u"a",u"abba","1001",u"அதுஅ",u"சரம்ரச"]
        actual = list(filter(wordutils.palindrome,words))
        self.assertEqual(actual,expected)
    
    def test_palindrome_false(self):
        words = [u"ab",u"abbax","xxkcd","xvinavi","103_301","10010",u"அxதுஅ",u"சரxம்xxரச"]
        expected = ['103_301']
        actual = list(filter(wordutils.palindrome,words))
        self.assertEqual(actual,expected)
    
    def test_ispalindrome(self):
        expected = [u"a",u"abba","1001",u"அதுஅ",u"சரம்ரச"]
        self.assertTrue( all(list(map(wordutils.is_palindrome,expected))) )
    
    def test_isanagram(self):
        w1 = u'சவால்'
        w2 = u'வாசல்'
        self.assertTrue( wordutils.is_anagram(w1,w2) )
        
        w3 = '123'
        w4 = '213'
        self.assertTrue( wordutils.is_anagram(w3,w4) )

        self.assertFalse( wordutils.is_anagram(w3,w1) )
        self.assertFalse( wordutils.is_anagram(w2,w4) )
        
if __name__ == '__main__':
    unittest.main()