# -*- coding: utf-8 -*-
from termcolor import colored
from scipy import stats
import numpy as np
from collections import Counter

itemwid = 30
outputwid = 40

def DescriptiveStatistics(the_list):
    """
    Obtain the descriptive statistics for the ages (in years) of five
    teenagers
    """
    mean = np.mean(the_list)
    median = np.median(the_list)

    range = np.ptp(the_list)
    variance = np.var(the_list)
    #ddof-Means Delta Degrees of Freedom
    #http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html#numpy.std
    mode = __getMode(the_list)
    stdDeviation = np.std(the_list,  ddof=1)
    __printBlock(('Mean', mean), ('Median', median), ('Mode', mode), ('Range', range), ('Variance', variance), ('Standard Deviation', stdDeviation))


def __printLeftRightAdj(l, r):
    #rjust and rjust is used to alignment
    print colored(l.ljust(itemwid), 'blue'), colored(str(r).rjust(outputwid), 'yellow')


def __drawOneLine():
    __printLeftRightAdj(itemwid * '-', outputwid * '-')


def __printBlock(*paraList):
    __drawOneLine()
    for a in paraList:
        __printLeftRightAdj(a[0], a[1])
    __drawOneLine()
    print ''


def __getMode(the_list):
    data = Counter(the_list)
    if data.most_common(1)[0][1] == data.most_common(2)[1][1]:
        return 'no mode'
    else:
        return data.most_common(1)[0][0]


def IntervalEstimation(the_list, ci=0.95):
    """
    constrct a 95% C.I for the ...
    """
    stats.bayes_mvs(the_list,  ci)
    #mean = np.mean(the_list)
    #stdDeviation = np.std(the_list, ddof=1)
    lower,  upper = stats.bayes_mvs(the_list,  ci)[0][1]
    __printBlock(('constrct a ' + str(ci), '$(' + str(lower.round(3)) + ', ' + str(upper.round(3)) + ')'))


def SimpleCorrelationAnalysis(xarray, yarray):
    """
    Compute the correlation coefficient,first input all x value in an array,then input    y value as an array
    """
    linregress = stats.linregress(xarray, yarray)
    r = linregress[2].round(3)
    p = linregress[3].round(3)
    __printBlock(('correlation coefficient', str(r)), ('Specify H' + '₀' + ' and ' + 'H' + '₀', 'H' + '₀'), ('Determine the p-value', 'P= ' + str(p) + ' > α = 0.05'))


def __showUsage(fun, *args):
    print colored('方法示例', 'red')
    argsStr = ', '.join(map(str, args))
    print colored(fun.__name__, 'cyan'), colored('(' + str(argsStr) + ')', 'green')
    print colored('打印显示', 'red')
    fun(*args)


def stathelp():
    __showUsage(DescriptiveStatistics, [14, 20, 18, 17, 15])
    __showUsage(IntervalEstimation, [110.6, 111.2, 110.4, 112.2, 111.3, 110.2, 110.3, 112.5])
    __showUsage(SimpleCorrelationAnalysis, [35, 90, 37], [34, 54, 64])
#DescriptiveStatistics([14,  20,  18,  17,  15])
#print 'IntervalEstimation([110.6, 111.2, 110.4, 112.2, 111.3, 110.2, 110.3,112.5], ci=0.95)'
#IntervalEstimation([110.6, 111.2, 110.4, 112.2, 111.3, 110.2, 110.3, 112.5], ci=0.95)
#stathelp()
