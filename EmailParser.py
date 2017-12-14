###
### Email parser for Outlook files
### Andrew Sommer
### Created on 12/11/17
### Version 1.2
### Last edited on 12/14



class EmailParser:
    s = "Andrew Yamin 19 <ayamin19@amherst.edu>, Blaine Fox 20 <bfox20@amherst.edu>, Drew Bryant 18 <dbryant18@amherst.edu>, Elijah Zabludoff 18 <ezabludoff18@amherst.edu>, Trey Jarmon 20 <tjarmon20@amherst.edu>, John Hickey 19 <jhickey19@amherst.edu>, Kyle Obana 18E <kobana18@amherst.edu>, Michael Immerman 21 <mimmerman21@amherst.edu>, James O'Regan 20 <joregan20@amherst.edu>, Brendan Coleman 20 <bcoleman20@amherst.edu>, Matthew Albino 21 <malbino21@amherst.edu>, Robert Monachello 21 <rmonachello21@amherst.edu>, Mitchell Arthur 18 <marthur18@amherst.edu>, Hasani Figueroa 18 <hfigueroa18@amherst.edu>, jack faulstick <jfaulstick20@amherst.edu>, Andrew Dorogi 18 <adorogi18@amherst.edu>, Jack Barrett 19 <jbarrett19@amherst.edu>, Craig Carmilani 18 <ccarmilani18@amherst.edu>, David Perdoni 20 <dperdoni20@amherst.edu>, John Callahan 19 <jcallahan19@amherst.edu>, Tristan Andrzejewski 21 <tandrzejewski21@amherst.edu>, Henry Atkeson 20 <hatkeson20@amherst.edu>, Zachary Allen 19E <zallen19@amherst.edu>, Andrew Ferrero 19 <aferrero19@amherst.edu>, Jacob Ayyub 21 <jayyub21@amherst.edu>, Robert Needham 19 <rneedham19@amherst.edu>, Nathaniel Tyrell 19 <ntyrell19@amherst.edu>, Beau Santero 18 <bsantero18@amherst.edu>, Hunter Voegele 18 <hvoegele18@amherst.edu>, John Griffiths 19 <jgriffiths19@amherst.edu>, Nicholas Tighe 20 <ntighe20@amherst.edu>, Jake Hines 18 <jhines18@amherst.edu>, Reece Foy 18 <rfoy18@amherst.edu>, Andrew DeNoble 19 <adenoble19@amherst.edu>, William Rotella 19 <wrotella19@amherst.edu>, Brantley Mayers 19 <bmayers19@amherst.edu>, Brendan Morrison 21 <bmorrison21@amherst.edu>, Langston Puller 21 <lpuller21@amherst.edu>, Kevin Sheehan 18 <ksheehan18@amherst.edu>, Gregory Franklin 20 <gfranklin20@amherst.edu>, John Tyrrell 19 <jtyrrell19@amherst.edu>, Cole Stephens 19 <cstephens19@amherst.edu>, Harrison Boeschenstein 20 <hboeschenstein20@amherst.edu>, Alexander Katchadurian 20 <akatchadurian20@amherst.edu>, Avery Saffold 20 <asaffold20@amherst.edu>, Bennett Fagan 20 <bfagan20@amherst.edu>, Brendan Popovich 20 <bpopovich20@amherst.edu>, Carson Glazier 20 <cglazier20@amherst.edu>, Collin Rissolo 19 <crissolo19@amherst.edu>, Daniel Papa 20 <dpapa20@amherst.edu>, Elijah Ngbokoli 20 <engbokoli20@amherst.edu>, Harry Thompson 19 <hthompson19@amherst.edu>, Jack Griffin 20 <jgriffin20@amherst.edu>, Jacob Drwila 18 <jdrwila18@amherst.edu>, John Ballard 20 <jballard20@amherst.edu>, John Rak 19 <jrak19@amherst.edu>, Justin Berry 20 <jberry20@amherst.edu>, Matthew Rusk-Kosa 18 <mruskkosa18@amherst.edu>, Michael Amicucci 18 <mamicucci18@amherst.edu>, Nathaniel Silvea 20 <nsilvea20@amherst.edu>, Ndukwo Okoronkwo 20 <nokoronkwo20@amherst.edu>, Nicholas Gill 20 <ngill20@amherst.edu>, Nicholas Morales 19 <nmorales19@amherst.edu>, Oliver Eberth 20 <oeberth20@amherst.edu>, Peter Jerome 20 <pjerome20@amherst.edu>, Robert Berluti 19 <rberluti19@amherst.edu>, William Kelsch 19 <wkelsch19@amherst.edu>, Arman Azad 21 <aazad21@amherst.edu>, Brett Bates 21 <bbates21@amherst.edu>, Elijah Blomquist 21 <eblomquist21@amherst.edu>, Graycen Carter 21 <gcarter21@amherst.edu>, Matthew Durborow 21 <mdurborow21@amherst.edu>, Kevin Durkin 21 <kdurkin21@amherst.edu>, Turner Garland 21 <tgarland21@amherst.edu>, Frederick Goodson 21 <fgoodson21@amherst.edu>, Noah John 21 <njohn21@amherst.edu>, Jared Jones 21 <jjones21@amherst.edu>, Eric Jung 21 <ejung21@amherst.edu>, Joseph Kelly 21 <jakelly21@amherst.edu>, Joseph Masterson 21 <jmasterson21@amherst.edu>, Samuel Mendenhall 21 <smendenhall21@amherst.edu>, Oliver Michaud 21 <omichaud21@amherst.edu>, Chase Trunnell 21 <ctrunnell21@amherst.edu>, Hunter Lampson 21 <hlampson21@amherst.edu>, Michael Odenwaelder 18E <modenwaelder16@amherst.edu>, Kellen Field 21 <kfield21@amherst.edu>"

    names = open("names.txt", "w+")
    emails = open("emails.txt", "w")
    for str in s.split(","):
        name, email = str.split("<")
        names.write(name +"\n")
        email = email.strip(">")
        emails.write(email + "\n")


    names.close()
    emails.close()
