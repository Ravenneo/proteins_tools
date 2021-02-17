__author__ = 'Jose Jesus Gallego-Parrilla'

__license__ = "GPL"

__maintainer__ = "Jose Jesus Gallego-Parrilla"

__email__ = "J.J.Gallego-Parrilla2@newcastle.ac.uk"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countWords(address, word):
    logfile = open(address, "r")
    wordcount = 0
    for lines in logfile:
        if word in lines.split():
            wordcount += 1
    return wordcount

import re

with open("chandra.html") as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bhydrogenase", contents))
    print("Hidrogenases:", count)
    
    count = sum(1 for match in re.finditer(r"\bdehydrogenase", contents))
    print("Dehydrogenases:", count)
    
    count = sum(1 for match in re.finditer(r"\bmembrane", contents))
    print("Membrane proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bcystathionine", contents))
    print("Cystathionine beta-lyase:", count)

    count = sum(1 for match in re.finditer(r"\bhypothetical\sprotein.", contents))
    print("Hypothetical proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bexported\shypothetical\sprotein", contents))
    print("Exported hypothetical proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bprotease", contents))
    print("Proteases:", count)
    
    count = sum(1 for match in re.finditer(r"\bchaperone", contents))
    print("Chaperones:", count)
    
    count = sum(1 for match in re.finditer(r"\bTat\spathway", contents))
    print("Tat pathway protein signal:", count)

    count = sum(1 for match in re.finditer(r"\bcapsule", contents))
    print("Capsule related proteins:", count)

    count = sum(1 for match in re.finditer(r"\bexopolysaccharide", contents))
    print("Exopolysaccharide biosynthesis protein:", count)

    count = sum(1 for match in re.finditer(r"\bcellulose.", contents))
    print("Cellulose related proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\blipoprotein", contents))
    print("Lipoproteins:", count)
    
    count = sum(1 for match in re.finditer(r"\blipoprotein-releasing", contents))
    print("lipoproteins releasing systems:", count)
    
    count = sum(1 for match in re.finditer(r"\bDUF445", contents))
    print("DUF445 domain-containing protein:", count)
    
    count = sum(1 for match in re.finditer(r"\bSurfeit", contents))
    print("Surfeit locus 1 family protein:", count)
    
    count = sum(1 for match in re.finditer(r"\btwin-arginine", contents))
    print("twin-arginine translocation pathway signal:", count)
    
    count = sum(1 for match in re.finditer(r"\btat", contents))
    print("Tat related:", count)
    
    count = sum(1 for match in re.finditer(r"\bapolipoprotein", contents))
    print("Apoproteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bcarboxypeptidase", contents))
    print("Carboxypeptidases:", count)
    
    count = sum(1 for match in re.finditer(r"\boxidoreductase", contents))
    print("Oxidoreductases:", count)
    
    count = sum(1 for match in re.finditer(r"\btRNA.", contents))
    print("tRNA:", count)
    
    count = sum(1 for match in re.finditer(r"\bphospholipase", contents))
    print("Phospholipases:", count)
    
    count = sum(1 for match in re.finditer(r"\bphosphatase", contents))
    print("Phosphatases:", count)
    
    count = sum(1 for match in re.finditer(r"\bphosphodiesterase", contents))
    print("Phosphodiesterase:", count)
    
    count = sum(1 for match in re.finditer(r"\bmetallophosphatase.", contents))
    print("Metallophosphatase:", count)
    
    count = sum(1 for match in re.finditer(r"\bphosphorylmutase", contents))
    print("vincarboxyyl carboxyphosphonate phosphorylmutase:", count)
    
    count = sum(1 for match in re.finditer(r"\bdehalogenase", contents))
    print("Dehalogenases:", count)
    
    count = sum(1 for match in re.finditer(r"\bsortase.", contents))
    print("Sortases:", count)
    
    count = sum(1 for match in re.finditer(r"\bferredoxin.", contents))
    print("Ferredoxins:", count)
    
    count = sum(1 for match in re.finditer(r"\bABC.", contents))
    print("ABC transporter substrate-binding protein:", count)
    
    count = sum(1 for match in re.finditer(r"\binhibition\sof\smorphological", contents))
    print("Inhibition of morphological differentiation proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bLPS\sbiosynthesis\sprotein", contents))
    print("LPS biosynthesis proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bphosphate\sacyltransferase", contents))
    print("Phosphate acyltransferases:", count)
    
    count = sum(1 for match in re.finditer(r"\btype\s1\sfimbrial\sprotein", contents))
    print("Type 1 fimbrial protein:", count)
    
    count = sum(1 for match in re.finditer(r"\btype\sII\ssecretion.", contents))
    print("Type II secretion:", count)
    
    count = sum(1 for match in re.finditer(r"\btype\sIII\ssecretion.", contents))
    print("Type III secretion:", count)
    
    count = sum(1 for match in re.finditer(r"\btype\sVII\ssecretion.", contents))
    print("Type VII secretion:", count)

    count = sum(1 for match in re.finditer(r"\bfibronectin\b", contents))
    print("fibronectins:", count)
    
    count = sum(1 for match in re.finditer(r"\bcytochrome.", contents))
    print("cytochromes:", count)
    
    count = sum(1 for match in re.finditer(r"\bzinc\sribbon.", contents))
    print("Zinc ribbon domain:", count)
    
    count = sum(1 for match in re.finditer(r"\bketoacyl", contents))
    print("ketoacyl-ACP synthase III:", count)
    
    count = sum(1 for match in re.finditer(r"\bhydrolase", contents))
    print("Hydrolases:", count)
    
    count = sum(1 for match in re.finditer(r"\bdehydratase", contents))
    print("Dehydratases:", count)
    
    count = sum(1 for match in re.finditer(r"\bpenicillin.binding", contents))
    print("Penicillin-binding proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bcell.wall", contents))
    print("Cell wall related proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bmagnesium\sand\scobalt.", contents))
    print("Magnesium and cobalt transport protein CorA:", count)
    
    count = sum(1 for match in re.finditer(r"\bHAF\srepeat.", contents))
    print("HAF repeat:", count)
    
    count = sum(1 for match in re.finditer(r"\bPEP-CTERM.", contents))
    print("PEP-CTERM:", count)
    
    count = sum(1 for match in re.finditer(r"\bchitin-binding", contents))
    print("chitin-binding protein:", count)
    
    count = sum(1 for match in re.finditer(r"\bVWA\sdomain.containing.", contents))
    print("VWA domain-containing:", count)
    
    count = sum(1 for match in re.finditer(r"\bpilus.", contents))
    print("Pilus related proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bflagellar.", contents))
    print("Flagellar related proteins:", count)
    
    count = sum(1 for match in re.finditer(r"\bdeferrochelatase.peroxidase", contents))
    print("Deferrochelatase/peroxidase EfeB:", count)
    
    count = sum(1 for match in re.finditer(r"\balkyl.", contents))
    print("Balkyl:", count)
    
    count = sum(1 for match in re.finditer(r"\bcopper.", contents))
    print("Copper resistance protein:", count)
     

    