'''
Created on 19 avr. 2018

@author: ddegar25
'''
import re
from datetime import datetime

def substring(string, textBegin, textEnd, useRightFind = False):
    '''
    Substring method that will analyze a given string and look for both other string:
    begin and and and, if both are found, will return everything wich is between begin
    and end
    :param string: the string to analyze
    :param textBegin: string that represents the begin of the text for substring.
    Substring will start at the end of this given string, so you have to provide the
    whole begin text
    :param textEnd: string that represents the end of the text for substring
    :param useRightFind: (optional) boolean, if true, we will use the rfind method when
    looking for the end (useful if the end text is also present in the begin text
    :raises Exception if either begin text or end text cannot be found in the given string
    :return: text extracted between the given texts (begin and end)
    '''
    indexBegin = string.find(textBegin)
    if useRightFind:
        indexEnd = string.rfind(textEnd, indexBegin)
    else:
        indexEnd = string.find(textEnd, indexBegin)
    if (indexBegin > -1 and indexEnd > -1):
        return string[indexBegin + len(textBegin):indexEnd]
    else:
        raise Exception("Text begin " + textBegin + " or text end " + textEnd + " not found in given string (" + string + ")")
    
def formatStartDate(string):
    # input: Apr 26, 2018 1:59:36 PM
    # output: 2018-04-26 13:59:36.19
    dt = datetime.strptime(string, '%b %d, %Y %I:%M:%S %p')
    return str(dt)

def extractHistory(response, startTime):
    '''
    Given HTML page and a known start time in this format (Apr 26, 2018 1:59:36) => returns an HTML extract from the given string
    '''
    # input: <tr class="even"><td>evx4406410.cube.ntt.preprod.org+STG01</td><td>2018-04-26 13:59:36.19</td><td>2018-04-26 14:09:13.26</td><td>0:09:37</td><td>COMPLETE</td><td>true</td></tr>
    # output: <td>2018-04-26 16:03:10.027</td> <td>0:09:16</td> <td>COMPLETE</td> <td>true</td>
    textToFind = '<td>' + formatStartDate(startTime)
    history = substring(response, textToFind, '</tr>')
    substr = '</td> '
    idx = history.find(substr)
    return history[idx + len(substr):]
    
def removeBlankLinesAndWhiteSpaces(string):
    '''
    Remove blank lines and keep only 1 whitespace in the given string
    '''
    return re.sub( '\s+', ' ', string.replace('\n', '')).strip()