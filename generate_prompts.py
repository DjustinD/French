import json
from pathlib import Path
import sys

# Dictionary mapping image filenames to detailed French prompts
# Each prompt describes the full scene that should appear in the image
prompt_templates = {
    # Objets scolaires
    'cahier.jpg': "Un cahier à spirale ouvert posé sur une surface en bois clair, montrant des pages lignées blanches avec quelques mots écrits au stylo bleu. L'angle de vue est légèrement en plongée, capturant l'ensemble du cahier avec ses bords arrondis et sa couverture colorée visible sur le côté. La lumière naturelle douce venant de la gauche crée des ombres subtiles, donnant une ambiance studieuse et chaleureuse. La palette de couleurs inclut des tons de bleu, blanc et bois naturel.",
    
    # Transports
    'camion.jpg': "Un camion de livraison moderne de taille moyenne stationné sur une route urbaine. Vue de trois-quarts avant montrant la cabine spacieuse avec pare-brise propre et la caisse de chargement rectangulaire. La carrosserie présente une couleur unie (rouge ou blanc) avec des détails métalliques brillants. L'arrière-plan montre un environnement urbain flou avec des bâtiments. Lumière du jour avec ciel légèrement nuageux, créant une ambiance professionnelle et dynamique.",
    
    'camion_pompiers.jpg': "Un camion de pompiers rouge vif moderne stationné devant une caserne, vu de trois-quarts avant. Le véhicule imposant montre tous ses équipements : échelle télescopique pliée sur le toit, tuyaux enroulés visibles, feux clignotants bleus, et compartiments de rangement ouverts révélant du matériel. La carrosserie rouge brillante reflète la lumière du soleil. L'arrière-plan montre les portes ouvertes de la caserne. Palette de couleurs dominée par le rouge pompier, chrome argenté, et touches de jaune.",
    
    # Meubles
    'canape.jpg': "Un canapé confortable à trois places dans un salon moderne et lumineux, vu de face à hauteur normale. Le canapé présente un design contemporain avec coussins moelleux, accoudoirs arrondis, et un tissu uni de couleur neutre (gris ou beige). Quelques coussins décoratifs colorés sont disposés élégamment. L'arrière-plan flou montre une fenêtre avec lumière naturelle et quelques plantes vertes. Ambiance chaleureuse et accueillante avec palette de tons neutres et touches de couleur.",
    
    # Lieux
    'cantine.jpg': "Une cantine scolaire spacieuse et bien éclairée avec plusieurs tables rectangulaires alignées et des chaises colorées. Vue en perspective montrant l'ensemble de l'espace avec le comptoir de service au fond où sont disposés des plateaux et de la nourriture. Les murs sont peints dans des couleurs claires et joyeuses. Quelques élèves sont assis en train de manger, créant une atmosphère conviviale. Éclairage fluorescent doux et lumière naturelle provenant des fenêtres. Palette de couleurs vives et accueillantes.",
    
    # Nature
    'cascade.jpg': "Une cascade naturelle pittoresque dévalant des rochers moussus dans une forêt luxuriante. L'eau cristalline tombe en plusieurs niveaux, créant une brume légère à la base. Vue frontale capturant toute la hauteur de la chute d'eau avec la piscine naturelle en bas. La végétation dense et verte encadre la scène avec des fougères et des arbres. Lumière du jour filtrée par la canopée créant des rayons lumineux. Palette dominée par les verts, bleus de l'eau, et tons de pierre grise.",
    
    'caverne.jpg': "L'intérieur d'une caverne naturelle spectaculaire avec des stalactites et stalagmites imposantes. Vue en perspective montrant la profondeur de la grotte avec des formations rocheuses calcaires éclairées par une lumière douce et mystérieuse. Le sol rocheux humide reflète légèrement la lumière. Des ouvertures naturelles laissent entrer quelques rayons lumineux créant un contraste dramatique. Palette de tons de gris, brun, et touches de lumière dorée.",
    
    # Arbres et plantes
    'cerisier.jpg': "Un cerisier en pleine floraison dans un verger ou un jardin printanier, vu en entier de légère contre-plongée. L'arbre majestueux est couvert de fleurs roses délicates formant une canopée dense et arrondie. Le tronc brun robuste et les branches élégantes sont partiellement visibles. L'arrière-plan montre un ciel bleu clair et une pelouse verte. Quelques pétales tombent doucement. Lumière printanière douce créant une ambiance poétique. Palette rose, vert, bleu ciel.",
    
    # Corps
    'cerveau.jpg': "Une illustration anatomique réaliste mais accessible du cerveau humain vu de trois-quarts, montrant les hémisphères cérébraux avec leurs circonvolutions caractéristiques. Les différentes régions sont légèrement différenciées par des tons subtils de rose et gris. Le cervelet et le tronc cérébral sont visibles à la base. Fond neutre blanc ou gris très clair pour mettre l'accent sur l'organe. Style éducatif clair avec des détails anatomiques précis mais non-intimidants. Palette de roses, gris-beige, et blanc.",
    
    # Meubles
    'chaise.jpg': "Une chaise simple et élégante en bois clair positionnée légèrement de trois-quarts sur un sol en bois ou carrelage clair. La chaise présente un design classique avec quatre pieds droits, une assise plate, et un dossier vertical à barreaux ou plein. La finition du bois est naturelle et lisse. L'arrière-plan est épuré et neutre pour mettre la chaise en valeur. Éclairage naturel doux créant des ombres légères. Palette de tons bois naturel, blanc et beige.",
    
    # Pièces
    'chambre.jpg': "Une chambre à coucher confortable et bien rangée vue depuis l'entrée en perspective. Un lit double avec couette et oreillers colorés occupe le centre contre le mur. Tables de chevet avec lampes de chaque côté. Une armoire ou commode visible, fenêtre avec rideaux légers laissant entrer la lumière naturelle. Tapis doux au sol. Décoration murale simple. Ambiance chaleureuse et reposante. Palette de couleurs douces : blanc, beige, bleu pâle ou rose pastel.",
    
    'champ.jpg': "Un vaste champ agricole en été s'étendant jusqu'à l'horizon, vu en légère plongée depuis un point surélevé. Les rangées de cultures (blé doré ou tournesols) créent des lignes parallèles régulières. Le ciel occupe un tiers supérieur avec quelques nuages blancs. À l'horizon, on aperçoit une ligne d'arbres ou une ferme au loin. Lumière chaude de fin d'après-midi créant des ombres longues. Palette de jaunes dorés, verts, et bleu ciel.",
    
    # Métiers
    'chanteur.jpg': "Un chanteur masculin sur scène tenant un microphone, vu de trois-quarts en plan américain. Il porte des vêtements décontractés mais élégants (chemise ou t-shirt avec veste). Expression concentrée et passionnée pendant la performance. L'arrière-plan flou montre des lumières de scène colorées et des instruments. Éclairage de concert créant des zones de lumière et d'ombre dramatiques. Ambiance énergique de spectacle live. Palette de couleurs vibrantes avec dominante de bleus et violets scéniques.",
    
    'chanteuse.jpg': "Une chanteuse féminine sur scène tenant élégamment un microphone près de sa bouche, vue de trois-quarts en plan américain. Elle porte une tenue de spectacle élégante (robe ou ensemble stylé). Cheveux longs ou mi-longs bien coiffés. Expression émotive pendant la performance. Arrière-plan avec lumières de scène colorées créant une atmosphère de concert. Éclairage professionnel mettant en valeur son visage. Ambiance artistique et captivante. Palette de couleurs chaudes avec accents de lumières scéniques.",
    
    'chauffeur.jpg': "Un chauffeur professionnel masculin assis au volant d'un véhicule, vu de profil ou trois-quarts à travers le pare-brise. Il porte une tenue professionnelle (chemise et cravate ou uniforme). Casquette de chauffeur éventuelle. Mains posées sur le volant, expression concentrée sur la route. Le tableau de bord moderne est visible. Lumière naturelle du jour à travers les vitres. Ambiance professionnelle et sûre. Palette de couleurs sobres : gris, blanc, noir.",
    
    # Arbres
    'chene.jpg': "Un chêne majestueux et centenaire isolé dans un pré, vu en entier de légère contre-plongée. L'arbre imposant montre son tronc épais et rugueux et sa large couronne feuillue formant un dôme généreux. Les branches robustes s'étendent largement. Feuilles vertes denses en été. Le ciel bleu apparaît entre les branches. Herbe verte au pied de l'arbre. Lumière naturelle créant des ombres portées. Symbole de force et longévité. Palette de verts, bruns et bleu ciel.",
    
    # Corps
    'cheveux.jpg': "Une chevelure féminine longue et saine vue de dos ou de côté, capturant la texture, la brillance et le mouvement naturel des cheveux. Les cheveux châtains ou bruns tombent en cascade sur les épaules avec quelques ondulations naturelles. Éclairage doux latéral mettant en valeur les reflets et la brillance. Arrière-plan neutre et flou pour concentrer l'attention sur les cheveux. Style naturel et soigné. Palette de bruns chauds avec reflets dorés ou cuivrés.",
    
    # Nourriture
    'chocolat.jpg': "Une tablette de chocolat noir entamée et plusieurs carrés de chocolat disposés artistiquement sur une surface en bois foncé ou ardoise. La texture lisse et brillante du chocolat contraste avec quelques éclats ou copeaux. Quelques fèves de cacao décoratives et feuilles de menthe ajoutent du contexte. Éclairage dramatique latéral créant des reflets brillants sur le chocolat. Ambiance gourmande et luxueuse. Palette de bruns foncés, noirs et touches de vert.",
    
    'chute_eau.jpg': "Une impressionnante chute d'eau haute dévalant une falaise rocheuse dans un paysage naturel spectaculaire. Vue frontale montrant toute la hauteur de la chute avec l'eau tombant en rideau puissant créant de l'écume blanche à la base. Rochers moussus de chaque côté. Végétation luxuriante encadrant la scène. Ciel visible en haut. Lumière naturelle créant un arc-en-ciel léger dans la brume. Ambiance grandiose. Palette de bleus, verts, gris pierre et blanc d'écume.",
    
    # Nature
    'ciel.jpg': "Un vaste ciel lumineux et dégagé occupant tout le cadre, vu en légère contre-plongée. Le bleu céleste varie graduellement de l'azur profond en haut vers des tons plus clairs près de l'horizon. Quelques nuages blancs cotonneux dispersés ajoutent de la profondeur et du dynamisme. L'horizon montrant une fine ligne de paysage (arbres ou collines) ancre l'image. Lumière naturelle de jour créant une atmosphère sereine et expansive. Palette dominée par le bleu ciel avec blanc pur.",
    
    # Arbres
    'citronnier.jpg': "Un citronnier chargé de fruits mûrs dans un jardin ensoleillé, vu en entier de léger contre-plongée. L'arbre de taille moyenne montre son feuillage vert brillant dense avec de nombreux citrons jaunes vifs visibles parmi les branches. Le tronc grisâtre et les branches sont partiellement visibles. Quelques fleurs blanches peuvent être présentes. Arrière-plan de jardin méditerranéen flou avec ciel bleu. Lumière chaude du sud. Palette de verts, jaunes éclatants et bleu.",
    
    # Lieux
    'classe.jpg': "Une salle de classe moderne et lumineuse vue depuis le fond en perspective. Rangées de bureaux d'élèves avec chaises face à un tableau blanc au mur avant. Bureau du professeur sur le côté. Étagères avec livres, affichages pédagogiques colorés aux murs. Grandes fenêtres laissant entrer la lumière naturelle. Quelques fournitures scolaires visibles. Ambiance studieuse et accueillante. Palette de couleurs claires et éducatives : blanc, bois clair, touches de bleu et rouge.",
    
    # Corps
    'coeur.jpg': "Une illustration anatomique réaliste mais accessible du cœur humain vu de face, montrant ses quatre cavités, les artères principales (aorte, artères pulmonaires) et veines. Les différentes structures sont différenciées par des tons de rouge (sang oxygéné) et bleu (sang désoxygéné). Style éducatif clair avec détails anatomiques précis mais non-effrayants. Fond neutre blanc ou gris très clair. Éclairage uniforme mettant en valeur les formes et structures. Palette de rouges, roses, bleus et blanc.",
    
    # Métiers
    'coiffeur.jpg': "Un coiffeur masculin professionnel en plein travail, vu de trois-quarts en train de couper les cheveux d'un client assis. Il porte une tenue professionnelle moderne (chemise noire ou tablier) et tient des ciseaux et un peigne. Expression concentrée et professionnelle. L'arrière-plan flou montre un salon de coiffure avec miroirs et produits. Éclairage professionnel du salon. Ambiance dynamique et soignée. Palette de couleurs contemporaines : noir, blanc, chrome.",
    
    'coiffeuse.jpg': "Une coiffeuse féminine professionnelle en plein travail, vue de trois-quarts en train de coiffer ou sécher les cheveux d'une cliente assise. Elle porte une tenue professionnelle élégante et moderne. Cheveux attachés, sourire professionnel. Tient un sèche-cheveux ou une brosse. L'arrière-plan flou montre un salon lumineux avec miroirs et produits. Éclairage doux et professionnel. Ambiance chaleureuse et experte. Palette de couleurs douces et modernes.",
    
    # Nature
    'colline.jpg': "Une colline verdoyante ondulante dans un paysage de campagne, vue de loin en perspective. La colline douce présente des pentes couvertes d'herbe verte parsemée de quelques arbres ou bosquets au sommet. Des sentiers serpentent sur les flancs. Ciel bleu avec nuages blancs occupe le tiers supérieur. Lumière naturelle de mi-journée créant des zones d'ombre et de lumière sur les pentes. Ambiance bucolique et paisible. Palette de verts variés, bleu ciel et blanc.",
    
    # Corps
    'cou.jpg': "Vue de profil ou trois-quarts du cou d'une personne adulte, montrant la région entre les épaules et le menton. Peau lisse et saine, muscles du cou subtilement définis sans être exagérés. Angle élégant entre la mâchoire et le cou visible. Arrière-plan neutre et flou. Éclairage doux latéral créant des ombres subtiles pour définir les formes anatomiques. Style photographique naturel et médical à la fois. Palette de tons chair naturels et fond blanc ou gris clair.",
    
    'coude.jpg': "Gros plan du coude d'une personne en position pliée à 90 degrés, montrant l'articulation et la peau légèrement plissée au niveau du pli. Vue latérale ou de trois-quarts. Bras reposant sur une surface neutre. Peau saine et naturelle avec quelques lignes de flexion visibles. Arrière-plan neutre. Éclairage doux et uniforme pour montrer clairement l'anatomie sans ombres dures. Style éducatif et naturel. Palette de tons chair et fond blanc ou gris très clair.",
    
    # Lieux
    'cour.jpg': "Une cour d'école rectangulaire vue d'en haut en légère plongée, entourée de bâtiments scolaires sur les côtés. Le sol est asphalté ou bétonné avec des marquages de jeux au sol (marelles, terrains de basket). Quelques arbres en pots ou plates-bandes apportent de la verdure. Bancs le long des murs. Quelques élèves jouent ou discutent en groupes. Lumière naturelle du jour créant des ombres douces. Ambiance vivante et scolaire. Palette de gris, blanc, vert et touches colorées.",
    
    # Nature
    'courant.jpg': "Une rivière à courant rapide s'écoulant sur des rochers dans un décor naturel, vue en perspective suivant le sens du flux. L'eau turbulente crée de l'écume blanche en contournant les obstacles rocheux. Le mouvement de l'eau est capturé avec un léger flou dynamique. Végétation verte sur les berges. Roches grises et brunes émergent du courant. Lumière naturelle créant des reflets sur l'eau. Ambiance dynamique et sauvage. Palette de bleus-verts, gris pierre et blanc d'écume.",
    
    # Famille
    'cousin.jpg': "Portrait en plan américain d'un jeune garçon (cousin) âgé d'environ 10-15 ans, vu de face ou trois-quarts. Expression amicale et souriante. Vêtements décontractés modernes (t-shirt et jean). Cheveux courts coiffés naturellement. Arrière-plan flou suggérant un environnement familial ou extérieur. Éclairage naturel doux créant une ambiance chaleureuse et familiale. Posture détendue et sympathique. Palette de couleurs naturelles et chaleureuses.",
    
    'cousine.jpg': "Portrait en plan américain d'une jeune fille (cousine) âgée d'environ 10-15 ans, vue de face ou trois-quarts. Expression souriante et joyeuse. Vêtements décontractés modernes (robe ou jean et top coloré). Cheveux longs ou mi-longs naturels. Arrière-plan flou suggérant un environnement familial ou jardin. Éclairage naturel doux créant une ambiance chaleureuse et familiale. Posture confiante et amicale. Palette de couleurs douces et gaies.",
    
    # Objets
    'crayon.jpg': "Un crayon à papier classique en bois naturel et graphite, posé en diagonale sur une surface blanche ou bois clair. Le crayon montre sa pointe taillée finement et sa gomme rose intacte à l'extrémité. Texture du bois visible avec son vernis léger. Vue rapprochée de trois-quarts montrant les détails. Quelques copeaux de taille à proximité. Éclairage doux créant une ombre légère. Ambiance studieuse et simple. Palette de beiges, graphite gris, rose gomme.",
    
    # Pièces
    'cuisine.jpg': "Une cuisine moderne et fonctionnelle vue en perspective depuis l'entrée. Plan de travail en granite ou quartz avec évier intégré. Placard hauts et bas blancs ou bois. Électroménagers intégrés (four, plaque de cuisson, réfrigérateur visible). Quelques ustensiles et bocaux décoratifs. Fenêtre laissant entrer la lumière naturelle. Carrelage au sol. Ambiance propre, lumineuse et accueillante. Palette de blanc, bois clair, inox et touches de couleur.",
    
    # Métiers
    'cuisinier.jpg': "Un cuisinier masculin professionnel en action dans une cuisine, vu de trois-quarts en plan américain. Il porte une veste de cuisine blanche traditionnelle et une toque haute. Expression concentrée en préparant un plat sur un plan de travail inox. Ustensiles de cuisine professionnels visibles autour. Arrière-plan flou montrant une cuisine professionnelle. Éclairage de cuisine professionnel. Ambiance dynamique et experte. Palette de blanc, inox et touches de couleurs alimentaires.",
    
    'cuisiniere.jpg': "Une cuisinière féminine professionnelle en action, vue de trois-quarts en plan américain dans une cuisine moderne. Elle porte une veste de cuisine blanche élégante et un bandana ou toque. Cheveux attachés, expression concentrée et passionnée. En train de préparer ou présenter un plat avec précision. Ustensiles professionnels autour d'elle. Arrière-plan de cuisine professionnelle flou. Éclairage optimal. Ambiance experte et créative. Palette de blanc, couleurs gastronomiques vives.",
    
    # Corps
    'dent.jpg': "Gros plan d'une dent molaire humaine en bonne santé vue sous un angle légèrement élevé, montrant la couronne blanche brillante avec ses cuspides et sillons caractéristiques. La racine peut être partiellement visible. Détails anatomiques clairs mais non-intimidants. Arrière-plan neutre blanc ou gris très clair. Éclairage uniforme et professionnel mettant en valeur la blancheur et la forme. Style éducatif et propre. Palette de blanc éclatant, ivoire et ombres grises subtiles.",
    
    # Métiers
    'dentiste.jpg': "Un dentiste professionnel en blouse blanche examinant un patient, vu de trois-quarts. Le dentiste porte un masque chirurgical, des gants et éventuellement des lunettes de protection. Tient des instruments dentaires (miroir, sonde). Patient assis dans le fauteuil dentaire visible partiellement. Éclairage professionnel du cabinet avec lampe médicale. Équipements dentaires modernes en arrière-plan. Ambiance médicale professionnelle et rassurante. Palette de blanc, bleu médical, acier inoxydable.",
    
    # Nature
    'desert.jpg': "Un vaste paysage désertique aride avec dunes de sable doré s'étendant jusqu'à l'horizon, vu en perspective depuis une hauteur modérée. Les dunes ondulantes créent des ombres et lumières contrastées. Ciel bleu profond occupant un tiers supérieur, possiblement avec soleil bas créant des couleurs chaudes. Peut-être un cactus solitaire ou quelques rochers. Ambiance aride mais majestueuse. Palette dominée par les ocres, jaunes dorés, bleu profond.",
    
    # Corps
    'doigt.jpg': "Gros plan d'un index humain (doigt pointeur) vu latéralement ou de face, montrant les trois phalanges et l'ongle propre et naturel. Peau saine avec plis articulaires visibles aux jointures. Position neutre légèrement fléchie ou droite. Arrière-plan neutre et flou. Éclairage doux et uniforme montrant la texture de la peau sans ombres dures. Style photographique naturel et éducatif. Palette de tons chair naturels avec fond blanc ou gris clair.",
    
    'dos.jpg': "Vue du dos humain d'une personne adulte en bonne santé, vu de face arrière depuis les épaules jusqu'aux hanches. Posture droite montrant la colonne vertébrale centrale subtile, les omoplates symétriques et la musculature dorsale naturelle sans exagération. Peau saine et lisse. Arrière-plan neutre uni. Éclairage doux latéral créant des ombres subtiles définissant la musculature. Style anatomique naturel. Palette de tons chair avec fond blanc ou gris neutre.",
    
    # Salle de bain
    'douche.jpg': "Une douche moderne dans une salle de bain contemporaine, vue légèrement de côté. Paroi de douche en verre transparent ou translucide, carrelage mural blanc ou gris clair. Pommeau de douche chromé fixé au mur avec robinetterie moderne. Sol de douche antidérapant avec évacuation. Quelques produits de douche (shampooing, gel) sur une étagère. Éclairage de salle de bain créant une ambiance propre et fraîche. Palette de blanc, gris clair, chrome brillant.",
    
    # Nourriture
    'eau.jpg': "Un grand verre transparent rempli d'eau pure et cristalline, vu de trois-quarts sur une surface blanche ou en bois clair. L'eau est parfaitement claire avec quelques bulles délicates remontant. Condensation légère sur l'extérieur du verre. Lumière naturelle créant des reflets et une légère causticité sur la surface. Peut-être une tranche de citron sur le bord. Ambiance fraîche et saine. Palette de transparence, bleu très pâle, blanc et reflets lumineux.",
    
    # Nature
    'eclair.jpg': "Un éclair spectaculaire déchirant un ciel d'orage nocturne ou crépusculaire, vu en perspective depuis le sol. La foudre ramifiée en forme d'arbre descendant des nuages sombres jusqu'au sol. Le flash illumine dramatiquement les nuages environnants. Silhouette de paysage (arbres ou collines) en premier plan. Contraste fort entre l'éclair blanc éblouissant et le ciel noir-violet. Ambiance dramatique et puissante. Palette de noirs profonds, violets, blancs éclatants.",
    
    # Lieux
    'ecole.jpg': "Un bâtiment d'école primaire moderne et accueillant vu de face, en légère contre-plongée. Architecture en briques colorées (rouges ou jaunes) avec grandes fenêtres. Deux ou trois étages avec toit visible. Entrée principale avec porte double et peut-être un panneau « École ». Cour avant avec arbres et pelouse verte. Quelques enfants avec cartables visibles. Ciel bleu avec nuages. Ambiance éducative et chaleureuse. Palette de briques colorées, blanc, vert et bleu ciel.",
    
    # Métiers
    'ecrivain.jpg': "Un écrivain concentré assis à un bureau en bois, vu de trois-quarts. Penché sur un ordinateur portable ou écrivant à la main. Porte des vêtements décontractés confortables. Lunettes éventuelles. Livres empilés et tasse de café à proximité. Lumière de lampe de bureau créant une ambiance studieuse. Arrière-plan avec bibliothèque floue. Expression réfléchie et absorbée. Ambiance créative et intellectuelle. Palette de tons chauds : bois, beiges, lumière dorée.",
    
    'electricien.jpg': "Un électricien masculin professionnel travaillant sur un panneau électrique ouvert, vu de trois-quarts. Porte un uniforme de travail (pantalon et chemise bleus) avec outils de ceinture. Casque de sécurité jaune et gants de protection. Tient un tournevis testeur. Expression concentrée et professionnelle. Câbles électriques colorés visibles dans le panneau. Arrière-plan de chantier flou. Éclairage de travail. Ambiance professionnelle et sécuritaire. Palette de bleu travail, jaune, câbles multicolores.",
    
    'electricienne.jpg': "Une électricienne féminine professionnelle travaillant sur une installation électrique, vue de trois-quarts. Porte un uniforme de travail adapté avec ceinture d'outils. Casque de sécurité et gants de protection. Cheveux attachés pour la sécurité. Expression concentrée et compétente. Tient un multimètre ou testeur. Câbles et boîtiers électriques visibles. Arrière-plan de chantier professionnel. Éclairage de travail. Ambiance experte et sécuritaire. Palette de bleu travail, jaune sécurité, couleurs techniques.",
    
    # Objets/Famille
    'eleve.jpg': "Portrait en plan américain d'un élève d'école primaire ou collège (8-12 ans) tenant un livre ou cahier, vu de face ou trois-quarts. Expression attentive et souriante. Vêtements scolaires décontractés propres. Cartable visible sur l'épaule ou posé. Arrière-plan flou suggérant une école (couloirs ou cour). Éclairage naturel créant une ambiance éducative positive. Posture confiante et studieuse. Palette de couleurs scolaires : bleu, blanc, touches colorées des fournitures.",
    
    # Famille
    'enfant.jpg': "Portrait joyeux d'un enfant de 5-8 ans, vu de face ou trois-quarts en plan américain. Expression heureuse et spontanée avec grand sourire naturel. Vêtements colorés et décontractés appropriés à l'âge. Cheveux naturels bien coiffés. Arrière-plan flou suggérant un environnement extérieur lumineux (parc ou jardin). Éclairage naturel doux créant une ambiance chaleureuse et innocente. Posture détendue et enfantine. Palette de couleurs vives et joyeuses.",
    
    # Métiers
    'enseignant.jpg': "Un enseignant masculin debout devant un tableau blanc, vu de face ou trois-quarts en plan américain. Porte une tenue professionnelle décontractée (chemise et pantalon). Tient un marqueur et explique quelque chose avec geste pédagogique. Expression engagée et bienveillante. Tableau avec diagrammes ou notes visibles derrière. Bureaux d'élèves flous au premier plan. Éclairage de classe naturel. Ambiance éducative positive. Palette de couleurs claires et académiques.",
    
    'enseignante.jpg': "Une enseignante féminine debout devant un tableau blanc interactif, vue de face ou trois-quarts. Porte une tenue professionnelle moderne et élégante (blouse et pantalon ou jupe). Cheveux attachés ou mi-longs, sourire engageant. Tient un stylet ou marqueur. Geste explicatif ouvert et accueillant. Élèves partiellement visibles de dos au premier plan. Éclairage de classe lumineux. Ambiance pédagogique chaleureuse. Palette de couleurs douces et professionnelles.",
    
    # Corps
    'epaule.jpg': "Vue rapprochée de l'épaule et du haut du bras d'une personne, montrant l'articulation et la musculature naturelle. Vue de trois-quarts ou latérale. Peau saine et lisse avec définition musculaire subtile (deltoïde). Posture naturelle détendue. Arrière-plan neutre et flou. Éclairage latéral doux créant des ombres subtiles pour définir l'anatomie. Style photographique naturel. Palette de tons chair avec fond blanc ou gris neutre.",
    
    # Famille
    'epouse.jpg': "Portrait en plan américain d'une femme adulte élégante (épouse) de 30-45 ans, vue de face ou trois-quarts. Expression douce et souriante. Vêtements contemporains élégants (robe ou ensemble raffiné). Cheveux bien coiffés. Peut porter une alliance visible. Arrière-plan flou suggérant un intérieur de maison ou jardin. Éclairage naturel doux créant une ambiance chaleureuse et familiale. Posture confiante et gracieuse. Palette de couleurs douces et élégantes.",
    
    'epoux.jpg': "Portrait en plan américain d'un homme adulte distingué (époux) de 30-45 ans, vu de face ou trois-quarts. Expression confiante et souriante. Vêtements contemporains soignés (chemise ou polo). Alliance visible sur la main. Coiffure soignée. Arrière-plan flou suggérant un intérieur de maison moderne. Éclairage naturel doux créant une ambiance chaleureuse et familiale. Posture détendue mais assurée. Palette de couleurs sobres et contemporaines.",
    
    # Arbres
    'erable.jpg': "Un érable majestueux en automne avec son feuillage rouge et orange flamboyant, vu en entier de légère contre-plongée. L'arbre de taille moyenne montre son tronc grisâtre et ses branches élégantes couvertes de feuilles colorées caractéristiques en forme de palme. Quelques feuilles tombent doucement. Pelouse verte en dessous. Ciel bleu visible entre les branches. Lumière automnale dorée. Symbole de l'automne canadien. Palette de rouges, oranges, jaunes et verts.",
    
    # Maison
    'escalier.jpg': "Un escalier intérieur moderne et lumineux vu en perspective de bas en haut. Les marches en bois clair ou blanches avec rampe élégante en métal chromé ou bois. Mur latéral blanc ou peint dans une couleur claire. Lumière naturelle provenant d'une fenêtre haute ou d'un éclairage intégré. Quelques cadres photos ou décoration murale. Ambiance architecturale contemporaine et accueillante. Palette de blanc, bois naturel, tons neutres.",
    
    # Corps
    'estomac.jpg': "Illustration anatomique éducative de l'estomac humain vu légèrement de côté, montrant sa forme en J caractéristique avec l'œsophage entrant en haut et l'intestin grêle sortant en bas. Les différentes parties (cardia, fundus, corps, antre, pylore) sont subtilement indiquées. Texture de la paroi visible. Style éducatif accessible. Fond neutre blanc ou gris clair. Éclairage uniforme. Palette de roses, rouges pâles et blanc.",
    
    # Meubles
    'etagere.jpg': "Une étagère murale moderne et fonctionnelle en bois clair ou blanc, fixée au mur. Plusieurs niveaux (3-5) avec divers objets disposés élégamment : livres alignés, petites plantes en pot, cadres photos, quelques objets décoratifs. Vue frontale légèrement de trois-quarts. Mur de couleur claire en arrière-plan. Éclairage naturel indirect créant une ambiance chaleureuse. Style minimaliste et organisé. Palette de blanc, bois clair, touches de couleur des objets.",
    
    # Nature
    'etang.jpg': "Un petit étang tranquille dans un cadre naturel, vu depuis la berge en perspective. L'eau calme reflète le ciel et la végétation environnante. Quelques nénuphars flottent à la surface. Roseaux et plantes aquatiques en bordure. Arbres et végétation luxuriante encadrent l'étang. Peut-être un canard ou grenouille. Lumière naturelle douce de fin d'après-midi. Ambiance paisible et sereine. Palette de bleus-verts, verts variés et reflets lumineux.",
    
    'etoile.jpg': "Un ciel nocturne profond parsemé d'innombrables étoiles brillantes de différentes intensités. Vue en contre-plongée totale montrant la voûte céleste. Quelques étoiles particulièrement brillantes se détachent. Peut-être une portion de la Voie Lactée visible. Silhouette très sombre de collines ou arbres en bas du cadre pour l'échelle. Pas de pollution lumineuse. Ambiance contemplative et infinie. Palette de bleu-noir profond, argent et blanc scintillant.",
    
    # Famille/Métiers
    'facteur.jpg': "Un facteur masculin en uniforme traditionnel (veste bleue avec liseré jaune, casquette) portant un sac postal en bandoulière, vu de trois-quarts. Tient des lettres et colis à la main ou les range dans le sac. Expression amicale et professionnelle. Arrière-plan flou suggérant une rue résidentielle ou boîtes aux lettres. Lumière naturelle du jour. Posture dynamique en mouvement. Ambiance de service public sympathique. Palette de bleu postal, jaune, beige du sac.",
    
    'factrice.jpg': "Une factrice féminine en uniforme postal moderne (veste bleue avec détails jaunes, pantalon pratique) portant un sac postal, vue de trois-quarts. Cheveux attachés ou courts, sourire amical. Tient des lettres dans une main. Scanner portable ou tablette peut-être visible. Arrière-plan flou de rue résidentielle. Lumière naturelle du jour. Posture professionnelle et dynamique. Ambiance de service public efficace. Palette de bleu postal, jaune, couleurs modernes.",
    
    # Famille
    'famille.jpg': "Portrait de groupe d'une famille heureuse de quatre personnes (parents et deux enfants) debout ensemble, vus de face en plan américain. Parents au centre avec enfants devant ou à côté. Tous sourient naturellement. Vêtements décontractés coordonnés mais pas identiques. Contact physique affectueux (bras autour des épaules). Arrière-plan flou d'extérieur (parc ou jardin). Éclairage naturel doux. Ambiance chaleureuse et aimante. Palette de couleurs harmonieuses et naturelles.",
    
    # Meubles
    'fauteuil.jpg': "Un fauteuil confortable et élégant en tissu uni (gris ou beige), vu de trois-quarts. Design contemporain avec dossier haut, accoudoirs rembourrés, et siège profond. Pieds en bois clair ou métal visible. Un coussin décoratif coloré posé dessus. Plaid léger drapé sur un bras. Arrière-plan flou de salon lumineux. Lumière naturelle créant des ombres douces. Ambiance cosy et accueillante. Palette de tons neutres avec accent de couleur.",
}

# Continue with more templates...
prompts_continued = {
    'femme_epouse.jpg': "Portrait élégant d'une femme mariée de 30-40 ans vue de trois-quarts en plan américain. Expression sereine et confiante avec léger sourire. Vêtements raffinés contemporains (blouse élégante ou robe simple). Alliance bien visible sur l'annulaire gauche. Cheveux bien coiffés. Arrière-plan flou d'intérieur domestique chaleureux. Éclairage naturel doux créant une ambiance familiale. Posture gracieuse et détendue. Palette de couleurs douces et féminines.",
    
    'ferry.jpg': "Un grand ferry moderne naviguant sur l'eau vue de trois-quarts. Le navire blanc et bleu à plusieurs ponts transporte véhicules et passagers. Structure imposante avec cheminée identifiable. Plusieurs fenêtres alignées sur les flancs. L'eau bleu-vert autour crée des vagues. Ciel avec nuages en arrière-plan. Quelques mouettes possibles. Lumière naturelle créant des reflets sur la coque. Ambiance maritime et voyageuse. Palette de blanc, bleu marine, bleu-vert marin.",
    
    'fete.jpg': "Une scène de fête joyeuse et colorée avec plusieurs personnes célébrant. Table décorée avec nappe colorée, ballons attachés, guirlandes suspendues, confettis éparpillés. Gâteau d'anniversaire au centre avec bougies. Chapeaux de fête, cadeaux emballés visibles. Personnes souriantes floues en arrière-plan. Ambiance festive et énergique. Éclairage intérieur chaleureux avec touches de lumières colorées. Palette très colorée : rouge, bleu, jaune, vert, rose.",
    
    'feu_rouge.jpg': "Un feu tricolore de circulation moderne monté sur un poteau métallique, vu de légère contre-plongée. Les trois feux (rouge en haut, orange au milieu, vert en bas) sont visibles avec le rouge allumé brillant. Boîtier noir rectangulaire avec visière anti-reflet. Croisement urbain flou en arrière-plan avec bâtiments. Ciel lumineux. Câbles électriques visibles. Lumière naturelle de jour. Symbole urbain de régulation. Palette de noir, rouge vif, gris urbain.",
    
    'feuille.jpg': "Gros plan d'une belle feuille verte de feuillage caduc (érable ou chêne) vue de dessus, montrant sa forme caractéristique avec nervures principales et secondaires bien visibles. Surface brillante et saine avec quelques gouttes de rosée. Couleur vert vif uniforme. Bordure dentelée. Fond neutre flou ou ciel lumineux. Éclairage naturel créant de la transparence et des reflets. Détails botaniques clairs. Palette de verts éclatants et fond clair.",
    
    'fille.jpg': "Portrait tendre d'une petite fille de 6-10 ans vue de face ou trois-quarts en plan américain. Expression joyeuse avec sourire naturel. Vêtements colorés et enfantins (robe ou jean et t-shirt). Cheveux longs attachés ou détachés. Arrière-plan flou d'environnement familial ou extérieur lumineux. Éclairage naturel doux créant une ambiance innocente et chaleureuse. Posture détendue et confiante. Palette de couleurs douces et gaies.",
    
    'fils.jpg': "Portrait affectueux d'un jeune garçon de 6-10 ans vu de face ou trois-quarts en plan américain. Expression heureuse et espiègle avec sourire franc. Vêtements décontractés colorés (t-shirt et jean). Cheveux courts coiffés naturellement. Arrière-plan flou d'environnement familial ou jardin. Éclairage naturel doux créant une ambiance tendre et familiale. Posture détendue et enfantine. Palette de couleurs vives et naturelles.",
    
    'fleur.jpg': "Gros plan d'une belle fleur épanouie (rose, tulipe ou marguerite) vue légèrement de dessus. Pétales délicats et colorés parfaitement formés autour du cœur de la fleur. Tige verte avec quelques feuilles visibles. Fond naturel flou (jardin verdoyant). Lumière naturelle douce créant des ombres subtiles entre les pétales. Quelques gouttes de rosée éventuelles. Ambiance botanique et printanière. Palette de couleurs florales vives (rose, rouge ou jaune) et vert.",
    
    'fleuve.jpg': "Un large fleuve majestueux s'écoulant calmement à travers un paysage, vu en perspective depuis une berge élevée. L'eau bleu-vert reflète le ciel et la végétation. Les deux rives boisées encadrent le cours d'eau. Peut-être un pont au loin ou un bateau. Ciel avec nuages occupe un tiers supérieur. Lumière naturelle de jour créant des reflets. Ambiance paisible et grandiose. Palette de bleus-verts, verts variés et bleu ciel.",
    
    'foret.jpg': "Une forêt dense et luxuriante vue depuis un sentier au milieu des arbres. Grands troncs d'arbres matures en premier plan, canopée verte formant un toit naturel. Lumière du soleil filtrée créant des rayons lumineux entre les branches. Sol forestier couvert de feuilles mortes, fougères et mousses. Sentier serpentant entre les arbres. Ambiance mystérieuse et sereine. Profondeur et perspective naturelles. Palette de verts variés, bruns et touches dorées de lumière.",
    
    'fougere.jpg': "Une belle plante de fougère verte et luxuriante vue de trois-quarts montrant ses frondes caractéristiques finement découpées. Plusieurs frondes arquées élégamment déployées. Détails des folioles délicates bien visibles. Base de la plante avec nouvelles crosses se déroulant. Fond naturel flou suggérant un sous-bois humide. Lumière filtrée douce créant une ambiance de forêt. Texture fine et répétitive. Palette de verts variés du clair au foncé.",
    
    'four.jpg': "Un four électrique moderne encastré dans une cuisine, vu de face. Porte en verre noir ou foncé avec hublot transparent montrant l'intérieur éclairé. Panneau de commande numérique ou à boutons sur le dessus ou côté. Finition inox ou noire brillante. Intégré dans un meuble de cuisine blanc ou bois. Lumière intérieure du four allumée. Éclairage de cuisine moderne. Ambiance culinaire et technologique. Palette de noir, inox, blanc.",
    
    'frere.jpg': "Portrait amical d'un garçon ou jeune homme (frère) de 8-16 ans vu de face ou trois-quarts. Expression souriante et complice. Vêtements décontractés modernes (t-shirt et jean). Cheveux courts ou mi-longs coiffés naturellement. Arrière-plan flou d'environnement familial. Éclairage naturel doux créant une ambiance fraternelle chaleureuse. Posture détendue et confiante. Palette de couleurs naturelles et contemporaines.",
    
    'fruit.jpg': "Une composition artistique de plusieurs fruits frais variés arrangés ensemble sur une surface en bois ou dans un bol. Pommes rouges, oranges, bananes jaunes, raisins violets, fraises disposés harmonieusement. Couleurs vives et saturées. Peaux brillantes et appétissantes. Quelques feuilles vertes pour décorer. Lumière naturelle créant des reflets et ombres douces. Ambiance saine et gourmande. Palette très colorée de rouges, jaunes, oranges, verts et violets.",
    
    'fusee.jpg': "Une fusée spatiale moderne sur sa plateforme de lancement, vue en légère contre-plongée. La fusée blanche imposante avec bandes colorées se dresse verticalement. Structure de support et échafaudages métalliques autour. Fumée blanche s'échappant de la base. Ciel bleu clair en arrière-plan. Détails techniques visibles sur la carlingue. Ambiance de conquête spatiale et technologique. Palette de blanc brillant, couleurs vives des marquages, gris métallique et bleu ciel.",
    
    'garage.jpg': "Un garage résidentiel moderne pour deux voitures, vu de face. Deux portes sectionnelles blanches ou grises fermées. Structure en briques ou crépi. Toit légèrement en pente. Petite fenêtre sur le côté ou au-dessus. Allée en béton ou pavés devant. Arbustes ou plantes décoratives sur les côtés. Lumière naturelle du jour. Ambiance résidentielle propre et organisée. Palette de gris, blanc, briques naturelles ou beiges.",
    
    'gare.jpg': "Une gare ferroviaire moderne et spacieuse vue depuis le quai en perspective. Quais couverts avec auvent métallique et vitré. Panneaux d'information électroniques affichant horaires. Voies ferrées parallèles avec train visible au loin. Passagers marchant avec bagages. Architecture contemporaine avec structures métalliques apparentes. Lumière naturelle entrant par les verrières. Ambiance de voyage et transit. Palette de gris, blanc, métal, jaune des lignes de sécurité.",
    
    'gateau.jpg': "Un beau gâteau d'anniversaire rond sur un plat, vu légèrement d'en haut. Glaçage blanc ou coloré lisse et brillant décoré avec motifs en pâte à sucre ou crème. Plusieurs bougies colorées plantées sur le dessus allumées. Peut-être des décorations florales comestibles. Surface de table avec quelques confettis. Ambiance festive et gourmande. Éclairage doux créant des reflets sur le glaçage. Palette de couleurs festives vives.",
    
    'gendre.jpg': "Portrait sympathique d'un jeune homme adulte (gendre) de 25-35 ans vu de face ou trois-quarts en plan américain. Expression ouverte et souriante. Vêtements soignés décontractés (chemise ou polo). Coiffure moderne soignée. Alliance visible éventuellement. Arrière-plan flou d'environnement familial ou extérieur. Éclairage naturel doux créant une ambiance familiale accueillante. Posture confiante et amicale. Palette de couleurs contemporaines et chaleureuses.",
    
    'genou.jpg': "Gros plan du genou humain en position légèrement fléchie, vu de face ou de trois-quarts. Peau saine et lisse couvrant l'articulation avec la rotule subtilement visible sous la peau. Partie inférieure du quadriceps et haut du tibia visibles. Arrière-plan neutre. Éclairage doux et uniforme montrant l'anatomie naturellement. Style photographique éducatif. Palette de tons chair naturels avec fond blanc ou gris clair.",
    
    'glace.jpg': "Un cornet de glace artisanale appétissant tenu à la main, vu de légère plongée. Deux ou trois boules de glace de couleurs différentes (vanille, fraise, chocolat) empilées sur un cornet gaufré doré. Surface légèrement fondante brillante. Peut-être un nappage ou des vermicelles. Arrière-plan flou d'été (plage ou parc). Lumière estivale chaude. Ambiance gourmande et rafraîchissante. Palette de couleurs crémeuses et pastels vives.",
    
    'glace_nature.jpg': "Un bloc de glace pure et transparente éclairé dramatiquement, montrant des structures cristallines internes et des bulles d'air emprisonnées. Surface lisse et brillante avec quelques fissures. Reflets et réfractions complexes. Fond neutre foncé ou bleuté pour contraste. Éclairage directionnel créant des éclats lumineux. Ambiance froide et cristalline. Texture transparente visible. Palette de bleus clairs, transparence, et reflets blancs argentés.",
    
    'glacier.jpg': "Un immense glacier montagnard majestueux avec sa langue de glace bleue descendant entre les montagnes. Vue d'ensemble en perspective montrant l'étendue du glacier avec crevasses visibles. Sommets enneigés en arrière-plan. Roches morainiques sombres sur les côtés. Ciel bleu profond. Lumière brillante créant des reflets sur la glace. Ambiance alpine grandiose et froide. Palette de bleus glaciaires, blanc neigeux, gris rocheux et bleu ciel.",
    
    'grand_mere.jpg': "Portrait chaleureux d'une grand-mère souriante de 60-75 ans vue de face ou trois-quarts en plan américain. Expression bienveillante et douce avec ride d'expression. Cheveux gris ou blancs courts ou attachés. Vêtements confortables élégants (pull ou chemisier). Lunettes éventuellement. Arrière-plan flou d'intérieur domestique chaleureux. Éclairage naturel doux créant une ambiance familiale tendre. Posture détendue. Palette de couleurs douces et chaleureuses.",
    
    'grand_pere.jpg': "Portrait affectueux d'un grand-père souriant de 60-75 ans vu de face ou trois-quarts en plan américain. Expression sage et bienveillante. Cheveux gris ou blancs courts. Possiblement des lunettes. Vêtements confortables soignés (chemise ou pull). Arrière-plan flou d'intérieur domestique ou jardin. Éclairage naturel doux créant une ambiance familiale chaleureuse. Posture détendue et digne. Palette de couleurs sobres et chaleureuses.",
    
    'grands_parents.jpg': "Portrait de couple de grands-parents assis ensemble sur un canapé ou banc, vus de face. Homme et femme de 65-75 ans souriant affectueusement. Contact physique tendre (mains jointes ou bras enlacés). Vêtements confortables élégants. Arrière-plan flou d'intérieur domestique chaleureux. Éclairage naturel doux. Ambiance familiale emplie de tendresse et sagesse. Palette de couleurs douces et harmonieuses.",
    
    'grotte.jpg': "L'entrée impressionnante d'une grotte naturelle dans une falaise rocheuse, vue de l'extérieur. Ouverture large et sombre encadrée par des formations rocheuses grises et brunes. Végétation (lierre, mousses) autour de l'entrée. Intérieur mystérieusement sombre avec quelques détails visibles. Lumière naturelle créant un contraste fort entre l'extérieur lumineux et l'intérieur sombre. Ambiance d'exploration et mystère. Palette de gris pierre, verts, et ombres profondes.",
    
    'helicoptere.jpg': "Un hélicoptère moderne en vol stationnaire ou proche du sol, vu de trois-quarts. Rotor principal en rotation (légèrement flouté), rotor de queue visible. Carrosserie généralement blanche ou colorée avec numéros d'identification. Cockpit avec pilote visible à travers les vitres. Ciel bleu en arrière-plan. Atterrissage sur héliport ou paysage flou en dessous. Ambiance dynamique et technologique. Palette de blanc, couleurs vives des marquages, gris métallique et bleu ciel.",
}

# Combine all prompt templates
all_prompts = {**prompt_templates, **prompts_continued}

# Get the list of missing images
with open('missing_images_for_prompts.txt', 'r', encoding='utf-8') as f:
    missing_images = [line.strip() for line in f.readlines()]

# Determine batch start and count from CLI args (defaults: start=0, count=100)
start = 0
count = 100
if len(sys.argv) >= 2:
    try:
        start = int(sys.argv[1])
    except Exception:
        start = 0
if len(sys.argv) >= 3:
    try:
        count = int(sys.argv[2])
    except Exception:
        count = 100

# Create prompt files for the requested batch of missing images
created_files = []
prompts_folder = Path('images/prompts')
prompts_folder.mkdir(parents=True, exist_ok=True)

end = start + count
for img_filename in missing_images[start:end]:
    prompt_filename = img_filename.replace('.jpg', '.prompt')
    prompt_path = prompts_folder / prompt_filename
    
    # Skip if prompt already exists
    if prompt_path.exists():
        continue
    
    # Get or create prompt content
    if img_filename in all_prompts:
        prompt_content = all_prompts[img_filename]
    else:
        # Generate generic prompt for images not in template
        word = img_filename.replace('.jpg', '').replace('_', ' ')
        prompt_content = f"Une image représentant {word} dans un contexte français typique. La composition montre l'élément principal au centre ou légèrement décentré avec un arrière-plan contextuel approprié. L'éclairage naturel crée une ambiance authentique et chaleureuse. Les couleurs sont réalistes et harmonieuses correspondant au sujet. L'angle de vue est optimal pour la reconnaissance et l'apprentissage. Tous les éléments du cadre contribuent à une scène cohérente et culturellement appropriée."
    
    # Write prompt file
    full_content = f"Fichier final: {img_filename}\n\n{prompt_content}\n\nSpécifications : JPEG 400×300 px (4:3), optimiser pour ≈100 KB, pas de texte ni de logos."
    
    with open(prompt_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    created_files.append((prompt_filename, img_filename))

# Generate report
print(f"\n=== RAPPORT DE CRÉATION DES PROMPTS ===\n")
print(f"Batch start: {start}, count: {count}")
print(f"Nombre total d'images manquantes : {len(missing_images)}")
print(f"Nombre de prompts créés : {len(created_files)}\n")
if created_files:
    print("Fichiers .prompt créés:\n")
    for prompt_file, original_img in created_files:
        print(f"  - images/prompts/{prompt_file} (pour {original_img})")
else:
    print("Aucun nouveau fichier .prompt créé pour ce batch (peut-être déjà existants).")
