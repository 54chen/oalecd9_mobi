import sys
import xml.etree.ElementTree as ET

tree = ET.parse('1.xml')
root = tree.getroot()

ns = {'d': 'http://www.apple.com/DTDs/DictionaryService-1.0.rng'}


for left_idx in range(546) :
    left = 100*left_idx;
    right = 100*(left_idx+1);
    
    html = [];
    i = -1;
    for entry in root.findall('d:entry', ns) :
        i = i + 1;
        if i < int(left) or i >= int(right):
            continue;
        
#    if i % 10 == 1: 
#        print(i);
        orth = entry.get('{http://www.apple.com/DTDs/DictionaryService-1.0.rng}title');
        wid  = entry.get('id'); 
        html.append('<idx:entry scriptable="yes" id='+ wid +'>');
        html.append('<idx:orth>' + orth);
        html.append('<idx:infl>');
        for idx in entry.findall('d:index', ns) :
            value = idx.get('{http://www.apple.com/DTDs/DictionaryService-1.0.rng}value');
            html.append('<idx:iform value="'+value+'" />');
        html.append('</idx:infl>');
        html.append('</idx:orth><br />');
    
        for child in entry:
            for cchild in child:
                for xch in cchild:
                    if xch.tag == '{http://www.w3.org/1999/xhtml}h':
                        cchild.remove(xch);
       # for ccc in child.get('{http://www.w3.org/1999/xhtml}h-g'):
       #     print(ccc.tag);


        body = ET.tostring(entry,encoding="unicode").replace('🔊','').replace('<html:pos-blk>','<br /><html:pos-blk>').replace('</html:pos-g>','</html:pos-g> <br />').replace('➡','<br />➡').replace('◆','<br /><br />◆').replace('>NAmE','> NAmE').replace('>BrE','> BrE').replace('>SYN','><br />SYN').replace('html:ul','ul').replace('html:li','li').replace('html:h','h').replace('h-g>','html:h-g>').replace('🔑','');

        html.append(body);
    #body = ET.XML(body);
    #html.append("".join(body.itertext()));
        html.append('</idx:entry>');
        html.append('<mbp:pagebreak/>');

    result = '<html xmlns:math="http://exslt.org/math" xmlns:svg="http://www.w3.org/2000/svg" xmlns:tl="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf" xmlns:saxon="http://saxon.sf.net/" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cx="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:mbp="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf" xmlns:mmc="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf" xmlns:idx="https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>';
    result += "\n".join(html);
    result += '</body></html>';

    f = open('xhtml/'+str(left)+'-'+str(right)+'.xhtml', "w");
    f.write(result);
    f.close();
    print(str(left)+'-'+str(right)+' is ok!');
