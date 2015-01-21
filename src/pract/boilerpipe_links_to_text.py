from boilerpipe.extract import Extractor
import ast, os, sys

""" Read a dict file mapping, get the urls, 

extract the text, send a mapping of the text 
and the associated url, close the file
01/19/2015
"""

def buildMapping(someDictFile):
    somedata = open(someDictFile).read()
    result = ast.literal_eval(somedata)
    keySize = len(result.keys())
    successRatio = 0
    linksLeft = 0
    target = open('content_link_mapping.txt','w')
    for key in result.keys():
    
        try:
            extractor = Extractor(extractor='ArticleSentencesExtractor',url=str(key))
            print("got the extractor")
            #target.write(str(result[key])+"|||"+extractor.getText().encode('utf-8')+'\n\n\n')
            target.write(result[key].encode('utf-8') + " ||| "+extractor.getText().replace("\n","").encode('utf-8')+"\n") #
            print("wrote data")
            successRatio += 1
            linksLeft += 1
            print("[+] SUCCESS    " + str(keySize - linksLeft))
        except Exception, e:
            linksLeft += 1
            print("[-] FAILURE - " + str(e)+ " --- " + str(keySize - linksLeft)) 

    target.close()
    print("Success Ratio : "+str(successRatio)+"/"+str(keySize))

if __name__=="__main__":
    buildMapping(sys.argv[1])

        
