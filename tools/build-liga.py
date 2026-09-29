"""Build data/liga.json: the capitulations of the Holy League, Rome, May 1571.

Source: J. Dumont, Corps universel diplomatique du droit des gens, vol. V,
part 1 (Amsterdam/The Hague, 1728), no. XCV, pp. 203-205, printing a
Spanish manuscript copy of the treaty (Internet Archive
corpsuniverseldi05dumo, leaves 245-247). Public domain.

Transcribed by eye from the page images: the OCR confuses the long s and
the italic p with f throughout. The long s is resolved; spelling,
accents and the copyist's Italianisms ("nostro", "Cattolico", "l'Armada")
are kept as printed. The print does not number the articles; the site
numbers its units. The English is this site's working translation (CC0).
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "liga.json"

HEAD_ES = ("Trattado, celebrado en Roma entre el sumo Pontifice Pio V., el Rey de España, y la Serenissima "
           "Republica de Venetia, contra el Turco y Moros de la Berberia en virtud de los Poderes que los "
           "respectivos Embaxadores tenian de su Principales, siendo los de su Magestad Catholica en fecha de "
           "12. de Mayo 1571, y los de la Serenissima Republica a 8 del mes de Decembre de 1570. años. "
           "[Copie manuscrite.]")
HEAD_EN = ("Treaty concluded in Rome between the supreme Pontiff Pius V, the King of Spain and the Most Serene "
           "Republic of Venice, against the Turk and the Moors of Barbary, by virtue of the powers the respective "
           "ambassadors held from their principals: those of His Catholic Majesty dated 12 May 1571, those of the "
           "Most Serene Republic 8 December 1570. [Manuscript copy.]")

CARDINALS = """CRISTOVAL, Ovispo Portuense, llamado de Trento,
OTTON, Obispo de Perneste llamado de Augusta,
ALESSANDRO, Obispo Jusculano, llamado Farnes, de la S. Romana Eclesia, Vice Canceller.
SCIPION, Titulo de Sta. Ma. en Trastibor, Clerico llamado de Pisis,
JACOBO, Titulo de Santa Maria Cosmedin Clerigo llamado de Sabello,
ALUIS, Titulo de San Marco, Clerigo, llamado Cornaro de la Santa Romana Eclesia Camerlengo,
FRANCISCO Titulo de Santa Crus, en Hierusalem, llamado Pacheco,
MARCO ANTONIO, Titulo de San Marcelo, Clerigo llamado Amuleo,
JUAN FRANCISCO, Titulo de Santa Prisee, Clerigo llamado de Sambara,
ALFONSO, Titulo de Sta. Cicilia, Clerigo, llamado Gesualdo,
NICOLAO, Titulo de Sto. Eustaschio, Clerigo llamado Sermoneta,
INIGO, Titulo de Sto. Lorenço in Lucina, Clerigo llamado de Arragon,
PROSPERO, Titulo de Sta. Maria de los Angeles, Clerigo llamado de Santa Crus,
FLAVIO, Titulo de San Pedro y Marcelino, Clerigo llamado de Ursino,
ALESSANDRO, Titulo de Sta. Maria de Araceli, Clerigo llamado Crivelo,
BENDITTO, Titulo de Sta. Sabina, Clerigo llamado Lomelin,
Frayle MIQUEL, Titulo de Sta. Maria sobre la Minerva, Clerigo, llamado Alessandrino,
GUILLERMO, Titulo de San Lorenço en Palisperna, Clerigo, llamado Cirleto,
FRANCISCO, Titulo de Santa Maria en Portico, Clerigo llamado Alciato,
Io. PAULO, Titulo de San Pancracio, Clerigo llamado Gusia,
MARCO ANTONIO, Titulo de San Calisto, Clerigo llamado Mafeo,
GASPAR, Titulo de San Martin in Monte, Clerigo llamado Urvante,
JULIO ANTONIO, Titulo de San Bartolomeo en la Isla, Clerigo llamado de Santa Severina,
PEDRO DONATO, Titulo de San Vital, Clerigo llamado de Cesis,
CARLOS, Titulo de Sta. Eufania, Clerigo llamado Bamboleto,
Frayle ARCANGEL, Titulo de Santa Cesarea, Clerigo llamado de Irane,
Frayle FELIX, Titulo de San Hironimo de los Esclavones, Clerigo llamado de Montalto,
PAULO, Titulo de Santa Potenciana, Clerigo llamado de Placencia,
JUAN, Titulo de San Simeon, Clerigo llamado Aldobrandin,
Frayle VINCENCIO, Titulo de San Germano en las Imagines Clerigo llamado Justiniano,
GERONIMO, Titulo de Santa Susanna, Clerigo llamado Rusticuso,
JOAN GERONIMO, Titulo de San Julio ante Puerta Latina, Clerigo llamado de Albano,
FERDINANDO, Titulo de Santa Maria in Dominica, Diacono llamado de Medicis,
JULIO, Titulo de San Teodoro, Diacono llamado de Aqua Viba."""

# (section, title or None, Spanish, English, note or None)
UNITS = [
 ("publication", None,
  "Primeramente despues de haver invocado el Nombre de Dios Padre, Hijo, y Espirito Santo, y de la Natividad de Nuestro Señor Jesu Christo, Mil y quiencentos y settenta y uno, en el Pontificado de Nuestro muy Santo Padre Papa Pio deste Nombre quinto, & Año sesto, a XXVI. del Mes de Mayo, en Roma, en el Palacio Apostolico, en la Sala del Sacro Consistoro, en presencia de sobredicho Nostro Santo Padre, y de los infrascrittos Reverendissimos Cardenales de la S. R. E. de los quales los nombres son los siguientes;",
  "First, after invoking the Name of God the Father, the Son and the Holy Spirit: in the year of the Nativity of our Lord Jesus Christ one thousand five hundred and seventy-one, in the pontificate of our most holy Father Pope Pius, fifth of that name, in his sixth year, on the twenty-sixth day of the month of May, in Rome, in the Apostolic Palace, in the hall of the Sacred Consistory, in the presence of our said Holy Father and of the most reverend Cardinals of the Holy Roman Church named below, whose names are these:",
  "The copy dates the publication 26 May, and Dumont's margin says the same; modern accounts give 20 May for the signing and 25 May for the publication in consistory."),
 ("publication", None, CARDINALS,
  "Thirty-four cardinals are named by title and by the name they were known by. Among them: Cristoforo Madruzzo ('of Trent'), Otto Truchsess ('of Augsburg'), Alessandro Farnese, vice-chancellor, Luigi Cornaro, camerlengo, Francisco Pacheco, Michele Bonelli ('Alessandrino', the Pope's great-nephew), Guglielmo Sirleto, Felice Peretti ('of Montalto', the future Sixtus V), Giovanni Aldobrandini and Ferdinando de' Medici. The list as printed is in the Spanish column.",
  "Names are given as the copyist wrote them, often Hispanicised or garbled; the identifications in the English column are this site's."),
 ("publication", None,
  "Fue publicado esta Santa Liga, allandose presentes los Procuradores del Serenissimo Rey Catolico, y de la Señoria de Venecia, Prometiendo cada uno, en Nombre los unos de su Rey, y los otros de su Republica, por ellos y su Sucesores que seria esta Confedracion inviolable, los Capitulos que en ella se han de observar son los siguientes:",
  "This holy League was published in the presence of the procurators of the most serene Catholic King and of the Signoria of Venice, each promising, the ones in the name of their King and the others of their Republic, for themselves and their successors, that this confederation would be inviolable. The articles to be observed in it are these:", None),

 ("forces", "Perpetual, and offensive",
  "Primeramente de baxo, de la gracia y favor de Dios para destrucion y ruina del Turco quieren y quedan de concierto, que esta Liga sea perpetua y no solamente, por defensa de los Reynos, y Señorias de los Confedrados, y de sus Susditos y Aliados, contra las fuerças del Turco, mas tambien para yr a sus daños del, tanto por Mar, como por Tierra, en las quales Impresas se comprenden Argel, Tunes, y Tripoli de Berberia.",
  "First: under the grace and favour of God, for the destruction and ruin of the Turk, they will and agree that this League shall be perpetual; and not only for the defence of the kingdoms and lordships of the confederates, and of their subjects and allies, against the forces of the Turk, but also to go and do him harm, by sea as well as by land; and among these enterprises Algiers, Tunis and Tripoli of Barbary are included.",
  "Barbary is Spain's price: the Venetian ambassador fought its inclusion through the negotiations of 1570."),
 ("forces", "Two hundred galleys",
  "Y para essecucion, y osservacion desta Confedracion fue entrellos acordado que las fuerças, tanto de Mar, como de Tierra de los quales pensavan valerse en esta Empresa, llegasen al numero de dozientas Galeras, y cien Naves de Cargo, y en quanto al numero de la Gente de Guerra, assi Italianos, como Españoles, Alemanes, y Borgonones, que llegase al numero de cinquanta Mil Infantes, quatro Mil y quinientos Cavallos, y l'Artilleria que fuesse necessaria con todas suertes de Moniciones abastantemente.",
  "And for the execution and observance of this confederation it was agreed among them that the forces by sea as by land which they meant to use in this enterprise should reach the number of two hundred galleys and one hundred cargo ships; and as to the men of war, Italians as well as Spaniards, Germans and Burgundians, the number of fifty thousand foot and four thousand five hundred horse, with the artillery needed and ample munitions of every kind.", None),
 ("forces", "Every spring, in the Levant",
  "Y que cada Año por el Mes de Março, o a lo mas tarde por Abril, l'Armada de la Liga se ha de allar en el Mar de Oriente, y que los Principales desta Armada li saran toda la diligencia possible, y conforme a como el tiempo se lo consentira, para ensalçamiento de los Confedrados y para dañar al Enemigo, con gloria, y provecho de los Principes, y Republica Cristiana.",
  "And that every year, in the month of March or at the latest in April, the fleet of the League is to be in the Eastern sea; and that the commanders of this fleet shall use all possible diligence, as far as the season allows, for the exaltation of the confederates and to harm the enemy, with glory and profit to the princes and the Christian commonwealth.",
  "In 1571 the fleet was not united until late August at Messina."),
 ("forces", "Relief before every other enterprise",
  "Y porque podria suceder que mientres que l'Armada y Potencias Confedradas estuviessen occupadas en alguna parte contra el Turco, que el por otra parte o por Mar, o por Tierra diesse sobre alguna Plaça de los Confedrados, en tal caso el General ha de embiar al soccoro de d[ich]a Plaça parte de las fuerças comunes, y si esto no bastara, yr con todo el Poder de la Liga a defender, y dar soccorro a la Tierra de los Enemigos acometida, dexando qualquiera otra Empresa.",
  "And because it might happen that while the fleet and the confederate powers were engaged against the Turk in one place, he might fall upon some town of the confederates elsewhere, by sea or by land, in that case the General is to send part of the common forces to relieve that town; and if that should not suffice, to go with the whole power of the League to defend and relieve the land attacked by the enemy, leaving any other enterprise.",
  "Famagusta was such a town, under siege while these articles were read out; it surrendered in August, before the fleet had sailed."),

 ("money", "Planning in the autumn",
  "Que los Principes Confedrados tengan en Roma sus Embaxadores acerca de la Persona de su Santidad, para que en el Autuno se trate de la Impresa que el Año siguente se hauria de hazer, y tratar si seran necessario mayores, o menores fuerças segun las Impresas que se havran de hazer.",
  "That the confederate princes keep their ambassadors in Rome near the person of His Holiness, so that in the autumn the enterprise to be made the following year may be discussed, and whether greater or smaller forces will be needed for the enterprises to be made.", None),
 ("money", "The Pope's share",
  "En quanto a la Contribucion del Gasto comun fue acordado entre ellos, y el Papa en su nombre y de todo el Sacro Colegio de Cardinales, daria para esta Guerra, tanta para offender, quanto para defender, doze Galeras armadas, y demas daria para el Exercito de Tierra, tres mil Infantes, y dozientos y settenta Cavallos.",
  "As to the contribution to the common cost, it was agreed among them that the Pope, in his own name and that of the whole Sacred College of Cardinals, would give for this war, for attack as well as for defence, twelve armed galleys, and besides, for the army on land, three thousand foot and two hundred and seventy horse.", None),
 ("money", "Three parts, two parts, and the poverty of Rome",
  "Los sobredichos Procuradores del Rey Catolico prometieron en nombre del Rey Don Filippo, que al presente Rey nuestro, y de los que a su Magestad succederan en los Reynos de España, y otros Reynos a su Magestad sugetos, que el pagaria las tres partes de los Gastos que se harian en esta Guerra, como asi mismo los Procuradores Venecianos de parte de su Principe, y Sucesores, y de toda la Señoria prometieron de contribuyr para esta Guerra, con las dos sestas partes del Gasto, y en quanto a la otra sesta parte que quedava del Gasto para esta Empresa, los Deputados Confedrados, en nombre de sus Principes que por causa de estar la Santa Sede Apostolica muy pobre a causa de las Heresias y travajos que havia tenido, por lo qual el Papa no podria complir el concierto hecho en la Liga del Año 1537, para lo qual querian partir a quella parte, en cinco partes de las quales el Rey pagaria las tres partes, y Venecianos las dos, desta manera que armassen veynte y quatro Galeras por estas dos partes de cinco, y si armando estas veynte y quatro Galeras no se gastava la suma destas dos partes, eran obligados a suplir en otra cosa, y si gastavan mas, se obligava el de rehazerselo en otra cosa.",
  "The said procurators of the Catholic King promised, in the name of King Don Philip, our present king, and of those who shall succeed His Majesty in the kingdoms of Spain and the other kingdoms subject to him, that he would pay three parts of the costs of this war; and likewise the Venetian procurators, on behalf of their prince and successors and of the whole Signoria, promised to contribute two sixth parts of the cost. As to the remaining sixth part of the cost of this enterprise, the confederate deputies, in the name of their princes, since the Holy Apostolic See was very poor on account of the heresies and troubles it had suffered, so that the Pope could not fulfil the agreement made in the League of the year 1537, wished to divide that part into five, of which the King would pay three and the Venetians two; in such manner that for these two parts of five they should fit out twenty-four galleys; and if in fitting out these twenty-four galleys the sum of these two parts was not spent, they were bound to make it up in something else, and if they spent more, he was bound to make it good to them in something else.",
  "Three sixths for Spain, two for Venice, one for the Pope, and the Pope's sixth passed on to the other two. 'The League of 1537' is the Holy League against Süleyman concluded in February 1538, which Venice, whose year began on 1 March, dated 1537."),
 ("money", "Twelve galleys lent to the Pope",
  "Tambien los Procuradores Venecianos en nombre de su Duque y Señoria dixeron que si el Papa y sus Successores fuessen dello servidos que le darian las dichas doze Galeras armadas de todo lo necessario; las quales doze Galeras su Santidad se obligaria de volverlas de la misma manera que se las daran.",
  "The Venetian procurators also said, in the name of their Doge and Signoria, that if the Pope and his successors so wished, they would give him the said twelve galleys, armed with all that is needed; which twelve galleys His Holiness would be bound to return in the same condition as they were given.",
  "The Pope had no fleet of his own: his twelve galleys in 1571 were fitted out by Cosimo de' Medici of Tuscany and commanded by Colonna."),
 ("money", "Accounts between King and Republic",
  "Y mas que tanto en el numero de las Galeras, como de las Naves, y otras cosas necessarias para la Empresa que se havian de proveer por la parte del Rey y de la Republica de Venecia, con condicion qu'el que gastaxe mas de lo que le toccava, fuesse obligado l'otro a rehazerselo.",
  "And further, as to the number of galleys and ships and the other things needed for the enterprise that were to be provided by the King and by the Republic of Venice: on condition that whichever spent more than his share, the other should be bound to make it good to him.", None),
 ("money", "Grain at an honest price",
  "Y mas que si las Vittuallas que cada dia se gastan venian a faltar, a qualquiera de las Partes confedradas, que las pudiessen comprar en qualquiera plaça que se allaren a honesto precio, y que haya el trato abiecto para beneficio comun, y que ningun de los Confedrados vede al otro hazer esta provision tan necessaria sin muy justa causa y que no se pueda retirar de las partes adonde haviere Vittuallas, hasta que los Confedrados sean proveeydos, con esta condicion toda via que el Rey de España pueda prover del Reyno de Napoles y Sisilia, la Goleta y Malta y su Armada,",
  "And further, if the victuals consumed every day should run short for any of the confederate parties, they may buy them in any place where they are found, at an honest price, and the trade shall be open for the common good; and no confederate shall forbid another to make this so necessary provision without very just cause, nor may victuals be withdrawn from the places where they are to be had until the confederates are supplied; with this condition, however, that the King of Spain may supply from the kingdoms of Naples and Sicily La Goleta, Malta and his fleet.",
  "Venice fed its galleys with Spanish grain from Sicily and Apulia: the article that bound Philip's granaries to the League."),
 ("money", "No new tolls",
  "Y mas que en quanto a las partes adonde se havia de pagar Peajes y Direchos que por trapasar de una parte a otra las cosas necessarias a las Armadas que no se ereyesen ny enovasen imposiciones que redondasen en perjuizio de los Confedrados,",
  "And further, as to the places where tolls and dues were to be paid for carrying from one place to another the things the fleets needed, that no new impositions be created or renewed that would redound to the prejudice of the confederates.", None),
 ("money", "No exports before the League is fed",
  "Y que esta Obligacion no se pueda escusar sino con pura necescidad que ninguna de las Potencias Confedradas dexe sacar de sus Dominios quantidad de Vittuallas hasta tanto que los Confedrados sean proveydos de los mismos Lugares para su Gente de Guerra tan de Mar como de Tierra reservando pero que al Rey Cattolico sea en su mano poder proveer de Napoles y Sisilia la Goleta, Malta y su Armada primero.",
  "And that this obligation may not be excused except by pure necessity: none of the confederate powers shall let any quantity of victuals be taken out of its dominions until the confederates are supplied from the same places for their men of war, by sea as by land; reserving, however, to the Catholic King the power to supply first, from Naples and Sicily, La Goleta, Malta and his fleet.", None),

 ("command", "Fifty galleys for Barbary, fifty for the Adriatic",
  "Y mas que si en tiempo que los Confedrados no hiziesen Empresa alguna, y el Rey Cattolico fuesse acometido d'el Turco, por las partes de Argel, Tunes, o Tripoli de Berberia, que en tal caso la Señoria de Venecia sea obligada de embiar en socorro del Rey cinquenta Galeras bien armadas, artilladas, y con todos los Adreços convenientes, Asi como su Magestad el Año passado embio en socorro desta Señoria, y que si a la Señoria sucediere el mismo caso que sea su Magestad Cattolica obligado a hazer otro tanto, como se contiene en el Capitulo primero.",
  "And further, if at a time when the confederates were making no enterprise the Catholic King were attacked by the Turk in the parts of Algiers, Tunis or Tripoli of Barbary, in that case the Signoria of Venice shall be bound to send to the King's help fifty galleys, well armed, with artillery and all fitting gear, as His Majesty sent last year to the help of this Signoria; and if the same case befell the Signoria, His Catholic Majesty shall be bound to do as much, as is contained in the first article.",
  "'Last year': the Spanish squadron under Giovanni Andrea Doria that joined the relief fleet of 1570."),
 ("command", None,
  "Y si acaecera que no teniendo los Confedrados Empresa entre manos, y que el Rey Cattolico quiera hazerla, o de Tunes, o de Argel, o de Tripoli de Berberia, que sea obligada la Señoria de Venecia de socorrer al Rey con cinquenta Galeras muy bien armadas, y de todo lo necessario bien proveydas, asi como embio su Magestad el Año passado en socorro de la dicha Señoria, y lo mismo sea tenido de hazer el Rey si a la Señoria de Venecia le sucedera Empresa en el Mar Adriatico, comencando de la Velona, hasta Venecia.",
  "And if it should happen that, the confederates having no enterprise in hand, the Catholic King wished to make one against Tunis, Algiers or Tripoli of Barbary, the Signoria of Venice shall be bound to help the King with fifty galleys very well armed and provided with everything needed, as His Majesty sent last year to the help of the said Signoria; and the King shall be held to do the same if the Signoria of Venice undertakes an enterprise in the Adriatic Sea, from Valona to Venice.", None),
 ("command", "The lands of the Church",
  "Y que si en las Tierras de su Santidad sucediere qualquiera necesidad o peligro que los Confedrados sean obligados de defenderlas con todas sus fuerças dexada a parte l'obligacion que a su Santidad tienen, y a la Santa Sede Apostolica.",
  "And that if any need or danger befell the lands of His Holiness, the confederates shall be bound to defend them with all their forces, quite apart from the obligation they already owe to His Holiness and to the Holy Apostolic See.", None),
 ("command", "Three generals, and the majority",
  "Y que en la administracion de la Guerra Consejos y deliberaciones que se hazan, hayan de entretenir en ellos tres Capitanes Generales de los Confedrados, y de todos tres lo que la mayor parte aprobara, que aquello se esequte y se ponga por obra por el Capitan General de toda l'Armada de la Sta. Liga, y si el General fuere uno de los tres lo ponga por effeto.",
  "And that in the conduct of the war, in the councils and deliberations to be held, the three captains-general of the confederates shall take part; and what the greater part of the three approves shall be carried out and put into effect by the captain-general of the whole fleet of the Holy League; and if the General is one of the three, he shall put it into effect.",
  "The council of three (Don John, Colonna, Venier) is the command the game measures as Unity."),
 ("command", "Don John of Austria, and Colonna",
  "Que el General de toda l'Armada, y Exercitos de la Santa Liga sera el Illustrissimo Señor Don Juan de Austria, el qual juntamente con el de su Santidad, y el de la Señoria de Venecia vendra a jusgar y decidir lo que la mayor parte acordara, como se contiene en el precedente Capitulo, y que si estando l'Armada aparejada, y apunto de todo para hazer Empresa, estuviesse ausente por algun accidente, que en tal caso el Illustrissimo Señor Marco Antonio Colona Duque de Paliano sea Capitan General ya nombrado por el Rey Cattolico, y aprobado de los otros Confedrados, y que el que sera General trayga el Estendarte que sea conosido ser de los tres Confedrados comunemente.",
  "That the General of the whole fleet and armies of the Holy League shall be the most illustrious Lord Don John of Austria, who together with the General of His Holiness and that of the Signoria of Venice shall judge and decide what the greater part agrees, as is contained in the preceding article; and that if, the fleet being equipped and ready in every respect to make an enterprise, he should be absent by some accident, in that case the most illustrious Lord Marcantonio Colonna, Duke of Paliano, shall be captain-general, already named by the Catholic King and approved by the other confederates; and that whoever is General shall bear the standard known to be the common standard of the three confederates.", None),

 ("faith", "A place kept for Emperor, France and Portugal",
  "A si mismo se reserva lugar onradissimo para poder en esta Confedracion, al Serenissimo Maximiliano elegido Emperador, al Christianissimo Rey de los Franceses, y al Rey de Portugal, los quales si entraren contribuiran a la Rata, y concorreran en los gastos para crecer las fuerças,",
  "Likewise a most honourable place is reserved in this confederation for the most serene Maximilian, Emperor elect, the most Christian King of the French and the King of Portugal, who, if they enter, shall contribute in proportion and share in the costs, to increase the forces.",
  "None of the three joined. France was allied to the Porte."),
 ("faith", None,
  "Que nostro Santo Padre sea obligado como Padre y Pastor Universal de essortar a los sobredichos Reyes, y a los otros Principes que tienen nombre de Cristianos para que entren en esta santa Union y la hayuden para que pase adelante en beneficio de la Republica Cristiana en la qual el Rey Cattolico y Señoria de Venecia tendra la mano en quanto a ellos sera possible.",
  "That our Holy Father shall be bound, as Father and universal Shepherd, to exhort the said kings and the other princes who bear the name of Christians to enter this holy union and help it forward, for the benefit of the Christian commonwealth; to which end the Catholic King and the Signoria of Venice shall lend a hand as far as they are able.", None),
 ("faith", "The division of conquests",
  "Y mas que las Tierras que los Confedrados ganaran se hayan departir segun la Convencion hecha l'Año de 1537, eccetuado Argel, Tunes y Tripoli de Berberia, las quales Plaças seran libres del Rey Cattolico, la Artilleria, y Moniciones se partiran a la Rata entre los Confedrados.",
  "And further, that the lands the confederates win shall be divided according to the convention made in the year 1537, except Algiers, Tunis and Tripoli of Barbary, which places shall belong to the Catholic King free; the artillery and munitions shall be divided among the confederates in proportion.", None),
 ("faith", "Ragusa spared",
  "Y mas que la Ciudad de Raguza, y su Territorio no sera molestado ni de l'Armada de Mar, ni Exercito de Tierra de los Confedrados; porque asi lo promete el Papa por el y sus Sucesores por justa causa, y legitima raçon y occasion.",
  "And further, that the city of Ragusa and its territory shall not be molested by the confederates' fleet at sea or army on land; for so the Pope promises, for himself and his successors, for just cause and legitimate reason and occasion.",
  "Ragusa (Dubrovnik), a Catholic republic paying tribute to the sultan, was the channel of news between the two worlds."),
 ("faith", "The Pope as judge and arbiter",
  "Y que no pueda nacer entre los Confedrados querella o Controversia que sea bastante a deshazer esta Confedracion y a que l'Empresa no passe adelante, y que no haya acavadamente effeto, y de las quales querellas o debates qualesquiera que sean y de qualquiera condicion y importancia, tocara a ser Juez y Arbitre dellas el Papa, que entonces sera o a su Sucesor por el avenir.",
  "And that no quarrel or controversy may arise among the confederates sufficient to undo this confederation, or to keep the enterprise from going forward and taking full effect; and of such quarrels or disputes, whatever they be and of whatever kind and importance, the Pope then reigning, or his successor in future, shall be judge and arbiter.",
  "The player's office in the game La más alta ocasión."),
 ("faith", "No separate peace",
  "Y mas que no sea prometido que uno de los Confedrados pueda hazer Treguas, Conciertos, o qualquiera otra Convencion con el Turco, ni por fee, ni por otra via sin dar dello primero aviso a sus Confedrados, y sin que elles consientan en ello, y que todo lo osservaran como Cristianos y como Principes Cattolicos, sin faltar en nada de lo que esta dicho y declarado azian, y sin yr en contrario de todo ny de parte alguna de los dichos Capitulos.",
  "And further, that it is not permitted for one of the confederates to make truces, agreements or any other convention with the Turk, whether by pledge of faith or in any other way, without first giving notice of it to his confederates and without their consent; and that they will observe all this as Christians and as Catholic princes, failing in nothing of what is said and declared, and doing nothing contrary to the whole or to any part of the said articles.",
  "Venice signed its separate peace with the Porte on 7 March 1573, giving up Cyprus."),
 ("faith", "The oath",
  "Todos estes Capitulos, y Convenciones, y cada una dellas en particular nostro Santo Padre el Papa en su nombre y de los suios, los Procuradores y Embaxadores en nombre de sus Principes, los quales para este effeto los havian embiado, y representaron sus Personas, prometieron y juraron solenemente de guardar inviolablemente la buena fee dada, sin usar fraude o circonvencion alguna, y sin jamas yr contra ella.",
  "All these articles and conventions, and each of them in particular, our Holy Father the Pope in his own name and that of his own, and the procurators and ambassadors in the name of their princes, who had sent them for this purpose and whose persons they represented, promised and solemnly swore to keep inviolably the good faith given, without using any fraud or circumvention, and never to go against it.", None),
 ("faith", None,
  "Y para Confirmacion dello el Papa quiso que en su nombre y de todo el Sacro Collegio de Cardenales, que todos los Bienes de la Santa Sede, asi Temporales como Espirituales, Muebles, y Rayzes havidos y por haver fuessen obligados a la sostencion de la dicha Liga.",
  "And in confirmation of this the Pope willed that, in his name and that of the whole Sacred College of Cardinals, all the goods of the Holy See, temporal as well as spiritual, movable and immovable, present and to come, should be bound to the upkeep of the said League.", None),
 ("faith", "Hand on breast",
  "Ny mas ni menos el Cardenal Pacheco, y Don Julio de Cunigro, Miguel Soriano, y Julio Superancio, con la mano al pecho juraron en mano de su Santidad, en nombre de sus Principes, y obligaron a ello sus Reynos y Señorias, y por sus Sucesores, y para mayor certitud cada uno de los Procuradores firmaron los dichos Capitulos con todo el Sacro Collegio de Cardenales, y los sellaron de sus sellos de modo que sirven de fee publica, y da fuerça al Contrato solene, y de osservarse inviolablemente. Sobre lo qual cada uno de los dichos Procuradores por si y todos juntos pidieron a mi Antonio Marchesano Datario de su Santidad que les diesse Copia de los infrascrittos Capitulos a los quales fueron presentes y Testigos dellos los siguientes en la sala del Sacro Colegio de Cardenales primero el Reverendissimo Monte Valente Governador de la Ciudad de Roma, Alessandro Riario Electo Patriarca de Alessandria y Auditor de la Camera Apostolica, Luiz de Torres Clerigo de la Camera Apostolica, Alessandro Casal Maestro de la Camera del Papa, Teodosio Florentino Cubiculario secreto de su Santidad, Antonio Barbarosio, Secretario de l'Embaxada del Rey Cattolico cerca la persona de su Santidad, Marco Antonio Dovilo, y Francisco Bravelo, Secretarios Venecianos, y Cornelio, y Ludovico Fernani, Maestros de Cerimonias de la Corte Romana, fueron presentes y Testigos, a todo lo que ambo contiene y rogado.",
  "In the same manner Cardinal Pacheco, Don Julio de Cunigro, Miguel Soriano and Julio Superancio swore with hand on breast in the hands of His Holiness, in the name of their princes, and bound to it their kingdoms and lordships and their successors; and for greater certainty each of the procurators signed the said articles with the whole Sacred College of Cardinals and sealed them with their seals, so that they serve as public faith and give force to the solemn contract, to be observed inviolably. Whereupon each of the said procurators, singly and all together, asked me, Antonio Marchesano, Datary of His Holiness, to give them a copy of the articles written below; present as witnesses in the hall of the Sacred College of Cardinals were: first the most reverend Monte Valente, governor of the city of Rome; Alessandro Riario, patriarch-elect of Alexandria and auditor of the Apostolic Chamber; Luis de Torres, cleric of the Apostolic Chamber; Alessandro Casal, master of the Pope's chamber; Teodosio Florentino, privy chamberlain of His Holiness; Antonio Barbarosio, secretary of the Catholic King's embassy to His Holiness; Marco Antonio Dovilo and Francisco Bravelo, Venetian secretaries; and Cornelio and Ludovico Fernani, masters of ceremonies of the Roman court; who were present and witnesses to all that the whole contains, and were asked to be.",
  "The procurators as the copyist wrote them: Cardinal Francisco Pacheco and Juan de Zúñiga for Spain ('Don Julio de Cunigro'), Michele Surian and Giacomo Soranzo for Venice ('Miguel Soriano', 'Julio Superancio')."),
 ("faith", None,
  "Demas de todo lo escrito presentaron los Procuradores las Cartas de Procura de sus Principes en aquella mas ample forma que fuesse possible.",
  "Besides all that is written, the procurators presented the letters of procuration of their princes in the fullest form possible.", None),
 ("faith", None,
  "La del Rey era la data de Sevilla a los XII. de Mayo 1571. firmado yo Rey, refrendada Antonino Perez, con el sello Real.",
  "The King's was dated at Seville, 12 May 1571, signed 'I the King', countersigned by Antonio Pérez, with the royal seal.", None),
 ("faith", None,
  "La de Venecianos era de Alonzo Mocenigo Duque de Venecia del Año de 1570. a 8. del Mes de Deziembre, con sello de plomo colgado con una cuerdelilla de cana nero.",
  "The Venetians' was from Alvise ('Alonzo') Mocenigo, Doge of Venice, of the year 1570, 8 December, with a lead seal hanging from a little black cord.",
  "'cana nero' as printed."),
]

SECTIONS = [
  ("publication", "The publication in consistory", "Liga Publ.",
   "Rome, the Apostolic Palace, the hall of the consistory: the invocation, the thirty-four cardinals present, and the promise of the procurators that the confederation would be inviolable."),
  ("forces", "Forces and the annual fleet", "Liga Forces",
   "What the League is for and what it will field: perpetual and offensive, two hundred galleys, fifty thousand foot, the fleet in the Levant every March or April, and every other enterprise to be dropped when a confederate town is attacked."),
  ("money", "Money and victuals", "Liga Money",
   "Who pays: three sixths for Spain, two for Venice, one for a papacy too poor to pay it; grain at an honest price, no new tolls, no exports before the League is fed."),
  ("command", "Mutual help and the command", "Liga Cmd.",
   "Fifty galleys each way for Barbary and the Adriatic, the lands of the Church defended, three captains-general deciding by majority, and Don John of Austria as captain-general, with Colonna in reserve."),
  ("faith", "Conquests, quarrels and faith kept", "Liga Faith",
   "A place kept for the Emperor, France and Portugal; conquests divided as in 1538, Barbary for Spain; Ragusa spared; the Pope as judge of every quarrel; no confederate to treat with the Turk alone; the oath, the seals and the witnesses."),
]


def main():
    sections = []
    for sid, titel, zk, blurb in SECTIONS:
        units = []
        if sid == "publication":
            units.append({"n": 1, "orig": HEAD_ES, "en": HEAD_EN, "label": True})
        for s, label, es, en, note in UNITS:
            if s != sid:
                continue
            u = {"n": len(units) + 1, "orig": es, "en": en}
            if label:
                u["titel"] = label
            if note:
                u["note"] = note
            if es is CARDINALS:
                u["list"] = True
            units.append(u)
        sections.append({"id": sid, "titel": titel, "zk": zk, "blurb": blurb, "units": units})
    doc = {
        "id": "liga",
        "titel": "The Capitulations of the Holy League, 1571",
        "autor": "Pius V, Philip II and the Republic of Venice",
        "jahr": "1571",
        "sprache": "en",
        "orig_sprache": "es",
        "zk": "Liga",
        "quelle": "Trattado, celebrado en Roma entre el sumo Pontifice Pio V., el Rey de España, y la Serenissima Republica de Venetia, contra el Turco y Moros de la Berberia (Rome, May 1571), from a Spanish manuscript copy printed in J. Dumont, Corps universel diplomatique du droit des gens, vol. V, part 1 (Amsterdam, 1728), no. XCV, pp. 203–205; Internet Archive corpsuniverseldi05dumo, leaves 245–247.",
        "hinweis": "The treaty was concluded in Latin; Dumont prints a Spanish copy, whose copyist writes with Italian habits ('nostro', 'Cattolico', 'l'Armada'), which suggests it was made in Rome. Transcribed by eye from the page images, since the OCR misreads the long s and the italic p as f; the long s is resolved, the spelling is kept as printed, and one abbreviation (d[ich]a) is expanded in brackets. The articles are unnumbered in the print; the site numbers its units and gives them short titles. The English is this site's working translation (CC0). The Latin text, and the Venetian account of the negotiations of 1570 printed just before it by Dumont (no. XCI), are named as future modules.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"liga.json: {len(sections)} sections, {sum(len(s['units']) for s in sections)} units")
    for s in sections:
        print(" ", s["id"], len(s["units"]))


if __name__ == "__main__":
    main()
