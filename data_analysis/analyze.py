# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:10:12 2017

@author: rajat
"""

import pandas as pd
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print 'The train has %d rows' % train.shape[0]
print 'The test has %d rows' % test.shape[0]


print pd.crosstab(train.education, train.target, margins=True)/train.shape[0]

