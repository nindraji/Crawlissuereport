#CRAWL ISSUE REPORT
import urllib
import re

crawlreport = ["Details","Description"]

i=0
while i<len(crawlreport):
    # see the https://issues.apache.org/jira/browse/CAMEL- comments for the issue report
   url = "https://issues.apache.org/jira/browse/CAMEL-" + crawlreport[i]+ "10597"
   htmlfile =urllib.urlopen(url)
   htmltext=htmlfile.read()
   regex = '<span title="2.18.0 planned for after summer 2016'+crawlreport[i]+'">2.18.0</span>'                                                                              
   pattern = re.compile(regex)
   details = re.findall(pattern,htmltext)
   print "The",crawlreport[i]," is " ,details 
   i+=1
