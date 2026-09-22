try:
    import spacy
    nlp_en = spacy.load('en_core_web_sm')
except:
    nlp_en = None

try:
    import spacy
    nlp_fr = spacy.load('fr_core_news_sm')
except:
    nlp_fr = None

RULES = {
    'English': [
        # BRAKES
        (['brake', 'squeak'], ('Brake pad wear', 'Inspect brake pads & discs. Squeaking usually means pads are thin and need replacement.')),
        (['brake', 'grind'], ('Severe brake pad/rotor wear', 'Stop driving ASAP. Check brake pads and rotors — metal-on-metal grinding means pads are gone. Inspect caliper on the noisy side.')),
        (['brake', 'noise'], ('Brake system issue', 'Inspect brake pads, discs, calipers, and hardware. Noise can mean wear, debris, or lack of lubrication on slide pins.')),
        (['brake', 'pull'], ('Brake caliper issue', 'Car pulling during braking means uneven pad wear or a stuck caliper. Inspect left vs right brake components.')),
        (['brake', 'soft'], ('Brake fluid issue or air in lines', 'Check brake fluid level and condition. Soft pedal = air in lines or leak. Bleed brakes and inspect for leaks.')),
        (['brake', 'vibrat'], ('Warped brake rotor', 'Brake pedal vibration = warped rotor. Resurface or replace rotors. Check for uneven pad deposits.')),
        (['brake', 'pedal'], ('Brake pedal issue', 'Check brake fluid level, master cylinder, and brake lines. Soft/hard/spongy pedal each indicate different problems.')),
        (['brake', 'fluid'], ('Brake fluid leak', 'Inspect all brake lines, calipers, wheel cylinders, and master cylinder for leaks. Top up fluid and find the leak source.')),

        # ENGINE
        (['engine', 'noise'], ('Engine noise issue', 'Check oil level first. Noises can be: ticking (low oil/lifter), knocking (bearing wear), squealing (belts). Inspect belts, oil, and listen for location.')),
        (['engine', 'overheat'], ('Engine overheating', 'Check coolant level, thermostat, radiator, and water pump. Never open hot radiator cap. Check for leaks in hoses and radiator.')),
        (['engine', 'smoke'], ('Engine smoke', 'Blue smoke = burning oil. White smoke = coolant leak (head gasket). Black smoke = rich fuel mixture. Check oil, coolant, and fuel system.')),
        (['engine', 'stall'], ('Engine stalling', 'Check fuel pump, air filter, spark plugs, and idle control valve. Also check for vacuum leaks and sensor issues (MAF, MAP, TPS).')),
        (['engine', 'miss'], ('Engine misfire', 'Check spark plugs, ignition coils, and fuel injectors. A misfire code (P0300-P0312) will point to the specific cylinder.')),
        (['engine', 'oil'], ('Oil warning light/pressure', 'Check oil level immediately. Low oil pressure can mean: low oil, worn bearings, faulty oil pump, or clogged pickup. Do NOT drive with low oil pressure.')),
        (['engine', 'check', 'light'], ('Check engine light (CEL)', 'Read OBD2 codes with a scanner. Common causes: O2 sensor, catalytic converter, mass airflow sensor, loose gas cap, or misfire.')),
        (['engine', 'belt'], ('Serpentine/drive belt issue', 'Inspect belt for cracks, fraying, or glazing. Squealing on startup = worn belt or loose tensioner. Replace belt every 60-100k km.')),
        (['engine', 'start'], ('Engine cranks but wont start', 'Check fuel pump (listen for hum), spark (pull a plug and test), and compression. Also check battery, starter, and immobilizer.')),
        (['engine', 'knock'], ('Engine knocking/pinging', 'Could be: detonation (use higher octane fuel), rod knock (serious — bearing failure), or piston slap. Check timing and oil level.')),
        (['engine', 'idle'], ('Rough/unstable idle', 'Check for vacuum leaks, dirty throttle body, bad idle air control valve, or worn spark plugs. Clean throttle body and MAF sensor.')),

        # BATTERY / ELECTRICAL
        (['battery', 'dead'], ('Dead battery', 'Jump-start or replace battery. Check alternator output (should be 13.5-14.5V while running). Clean terminals and check for parasitic drain.')),
        (['battery', 'drain'], ('Parasitic battery drain', 'Use a multimeter in series to find current draw. Check: interior lights, trunk light, aftermarket accessories, stuck relays.')),
        (['battery', 'charge'], ('Battery not charging', 'Check alternator voltage (13.5-14.5V running). Check alternator belt tension, wiring, and battery age (replace every 4-5 years).')),
        (['battery', 'warning'], ('Battery warning light', 'Alternator failing, loose belt, bad voltage regulator, or corroded connections. Test alternator output immediately.')),
        (['battery', 'terminal'], ('Corroded battery terminals', 'Clean terminals with baking soda + wire brush. Apply dielectric grease. Check cable condition and tightness.')),

        # STEERING
        (['steering', 'vibrat'], ('Steering vibration', 'Usually wheel balance issue — get wheels balanced. Could also be: warped rotors (if vibrate when braking), bent wheel, worn tie rods, or bad ball joints.')),
        (['steering', 'pull'], ('Car pulling to one side', 'Check tire pressure (unequal), wheel alignment, brake caliper sticking, or suspension wear. Rotate tires and get alignment check.')),
        (['steering', 'hard'], ('Hard/heavy steering', 'Check power steering fluid level and condition. Could be: failing power steering pump, bad rack, or leak in system.')),
        (['steering', 'noise'], ('Steering noise', 'Clicking when turning = CV joint (front). Clunking = tie rod or ball joint. Whining = power steering pump low on fluid.')),
        (['steering', 'play'], ('Excessive steering play', 'Check tie rod ends, steering rack bushings, ball joints, and idler arm. Worn components cause loose steering feel.')),

        # TRANSMISSION
        (['transmission', 'slip'], ('Transmission slipping', 'Check transmission fluid level and condition (should be red/pink, not brown/burnt). May need adjustment, new fluid, or rebuild.')),
        (['transmission', 'shift'], ('Hard/rough shifting', 'Check transmission fluid. Could be: low fluid, worn clutch (manual), solenoid issues (automatic), or TCM problem.')),
        (['transmission', 'noise'], ('Transmission noise', 'Whining in neutral = input shaft bearing. Clunking = U-joint or output shaft. Grinding = worn synchronizers (manual).')),
        (['transmission', 'fluid'], ('Transmission fluid leak', 'Check pan gasket, cooler lines, axle seals, and drain plug. Red fluid = transmission. Brown/burnt = old fluid needs changing.')),

        # TIRES
        (['tire', 'wear'], ('Uneven tire wear', 'Get alignment checked. Uneven wear pattern tells: center = overinflated, edges = underinflated, one side = alignment, cupping = suspension/shocks.')),
        (['tire', 'punctur'], ('Punctured/flat tire', 'Use spare tire or repair kit. Inspect tire for damage. Plug/patch if repairable, replace if sidewall is damaged.')),
        (['tire', 'pressure'], ('Low tire pressure', 'Check for puncture (nails, screws). Inflate to spec (door sticker). TPMS sensor may need battery replacement.')),
        (['tire', 'vibrat'], ('Tire vibration', 'Get wheels balanced. Check for: uneven tread wear, bent rim, separated tire cord, or loose lug nuts.')),

        # COOLING SYSTEM
        (['coolant', 'leak'], ('Coolant leak', 'Check radiator, hoses, water pump, and heater core for leaks. Use UV dye to find hidden leaks. Never open hot system.')),
        (['coolant', 'low'], ('Low coolant level', 'Top up with correct coolant mix. Check for leaks. If recurring, check head gasket (exhaust bubbles in coolant, milky oil).')),
        (['heater', 'not', 'work'], ('Heater not working', 'Check coolant level, thermostat (stuck open = no heat), heater core (clogged/airlocked), and blend door actuator.')),
        (['ac', 'not', 'cold'], ('AC not blowing cold', 'Check refrigerant level, compressor operation, condenser, and expansion valve. Look for leaks with UV dye. Recharge system.')),
        (['ac', 'smell'], ('Bad AC smell', 'Replace cabin air filter. Clean/replace evaporator. Use AC disinfectant spray. Mold/bacteria growth in the system.')),

        # EXHAUST / EMISSIONS
        (['exhaust', 'smoke'], ('Exhaust smoke issue', 'White = coolant (head gasket). Blue = oil (rings/seals). Black = rich fuel. Get compression test and check gaskets.')),
        (['exhaust', 'smell'], ('Exhaust smell in cabin', 'Check for exhaust leaks under car. Leaking manifold, cracked pipe, or bad gasket. CO is deadly — fix immediately.')),
        (['catalytic', 'converter'], ('Catalytic converter issue', 'Check O2 sensor readings. Code P0420 = converter efficiency low. May be clogged or poisoned by bad fuel/oil.')),

        # SUSPENSION
        (['suspension', 'noise'], ('Suspension noise', 'Clunking over bumps = bad shocks/struts or bushings. Squeaking = dry bushings or worn ball joints. Bounce test: push fender, should settle in 1-2 bounces.')),
        (['suspension', 'bounce'], ('Excessive bouncing', 'Worn shocks/struts. Replace in pairs. Bounce test: car should settle within 2 bounces. More = worn dampers.')),
        (['shock', 'strut'], ('Worn shocks/struts', 'Replace when: excessive body roll, nose dive under braking, bouncing, or leaking fluid. Do wheel alignment after replacement.')),

        # FUEL SYSTEM
        (['fuel', 'pump'], ('Fuel pump issue', 'Listen for pump hum when key turns to ON (2 sec prime). No hum = bad pump/fuse/relay. Check fuel pressure with gauge.')),
        (['fuel', 'filter'], ('Clogged fuel filter', 'Replace fuel filter (every 30-50k km). Symptoms: hesitation, loss of power, hard starting, rough idle.')),
        (['fuel', 'economy'], ('Poor fuel economy', 'Check tire pressure, air filter, spark plugs, oxygen sensors, and driving habits. Clean MAF sensor and throttle body.')),
        (['fuel', 'injector'], ('Fuel injector issue', 'Clean or replace injectors. Symptoms: misfire, rough idle, poor MPG. Use fuel injector cleaner or professional cleaning.')),

        # STARTER / IGNITION
        (['starter', 'click'], ('Starter clicking', 'Low battery, bad starter solenoid, or corroded connections. Check battery voltage first. Tap starter gently as temporary fix.')),
        (['starter', 'not', 'work'], ('Starter not working', 'Check battery, starter relay, ignition switch, neutral safety switch (auto), and starter motor. Test with jumper wire.')),
        (['key', 'not', 'start'], ('Key wont start car', 'Check: key battery (keyless), immobilizer, brake pedal position (push-start), gear selector (auto), and starter system.')),

        # SMOKE / SMELL
        (['smoke', 'under', 'hood'], ('Smoke from under hood', 'Pull over safely and turn off engine. Check for: coolant leak on hot engine, oil leak on exhaust, electrical fire. Let cool before inspecting.')),
        (['burning', 'smell'], ('Burning smell', 'Burning rubber = belt/hose touching hot surface. Burning oil = leak on exhaust. Burning plastic = electrical. Find source and fix.')),

        # VIBRATION
        (['vibrat', 'wheel'], ('Wheel vibration', 'Get wheels balanced first. If persists: check tire for bulge/separation, bent rim, warped rotor, or worn suspension parts.')),
        (['vibrat', 'steering', 'wheel'], ('Steering wheel vibration', 'Front wheel balance issue or warped front brake rotors. Get balance done first, then check rotors if vibration occurs during braking.')),

        # GENERAL
        (['car', 'pull'], ('Car pulling to one side', 'Check: tire pressure, alignment, brake caliper sticking, suspension wear, and tire size mismatch. Start with tire pressure check.')),
        (['warning', 'light'], ('Dashboard warning light', 'Identify the light symbol. Common: check engine (red/yellow engine), ABS, oil pressure, battery, temp. Read OBD2 codes for check engine light.')),
        (['odometer', 'light'], ('Odometer/trip light', 'Usually a bulb or LED replacement behind the instrument cluster. Some cars need cluster removal. Check fuse first.')),
        (['car', 'shake'], ('Car shaking/vibrating', 'Check: wheel balance, engine mounts, spark plugs (misfire), warped rotors, or suspension issues. Note when it happens (acceleration, braking, idle).')),
        (['car', 'rust'], ('Rust/corrosion', 'Treat surface rust with converter + paint. Structural rust needs professional inspection. Prevent: undercoat, wash undercarriage in winter.')),
    ],
    'Francais': [
        # FREINS
        (['frein', 'grincement'], ('Usure de freins', "Contrôlez plaquettes et disques. Un grincement métallique = plaquettes usées. Vérifiez aussi l'étrier du côté bruyant.")),
        (['frein', 'bruit'], ('Problème de frein', "Inspectez plaquettes, disiques et étriers. Le bruit vient de l'usure, de débris ou de manque de lubrification.")),
        (['frein', 'frotte'], ('Frottement des freins', "Vérifiez plaquettes et disques. Si la voiture tire d\\'un côté, inspectez l\\'étrie bloqué.")),
        (['frein', 'tire'], ('Déséquilibre au freinage', "Vérifiez les étriers/pistons, flexibles et plaquettes droite/gauche. L'étrier peut être grippé.")),
        (['frein', 'mou'], ('Frein mou/pédale molle', "Vérifiez le niveau de liquide de frein. Pédale molle = air dans les circuits ou fuite. Purgez et inspectez les fuites.")),
        (['frein', 'vibrat'], ('Disque de frein voilé', "Vibration au freinage = disque voilé. Rectifiez ou remplacez les disques. Vérifiez le dépôt inégal de plaquettes.")),
        (['frein', 'liquide'], ('Fuite de liquide de frein', "Inspectez flexibles, étriers, maître-cylindre et durées. Relevez le niveau et trouvez la source de la fuite.")),
        (['frein', 'pied'], ('Problème de pédale de frein', "Vérifiez niveau liquide, maître-cylindre et circuits. Pédale dure/molle = problèmes différents.")),

        # MOTEUR
        (['moteur', 'bruit'], ('Problème de bruit moteur', "Vérifiez le niveau d'huile en premier. Cliquetis = huile basse/culbuteurs. cogner = roulements. Siffler = courroies.")),
        (['moteur', 'chauffe'], ('Surchauffe moteur', "Vérifiez niveau liquide, thermostat, radiateur, pompe à eau. Ne jamais ouvrir le bouchon chaud. Cherchez les fuites.")),
        (['moteur', 'fumee'], ('Fumée du moteur', "Bleue = huile. Blanche = liquide de refroidissement (joint de culasse). Noire = mélange riche. Faites un test de compression.")),
        (['moteur', 'calé'], ('Moteur qui cale', "Vérifiez pompe à essence, filtre à air, bougies et valve de ralenti. Cherchez les fuites d'air et capteurs défectueux.")),
        (['moteur', 'rate'], ('Moteur qui rate', "Vérifiez bougies, bobines d'allumage et injecteurs. Un code de raté (P0300-P0312) indique le cylindre défaillant.")),
        (['moteur', 'huile'], ('Témoin de pression huile', "Vérifiez le niveau d'huile IMMÉDIATEMENT. Pression basse = usure, pompe défaillante ou carter bouché. NE CONDUISEZ PAS.")),
        (['moteur', 'voyant'], ('Témoin moteur allumé', "Lisez les codes OBD2 avec un scanner. Causes courantes : capteur O2, catalyseur, MAF, bouchon essence ou raté.")),
        (['moteur', 'courroie'], ('Problème de courroie', "Inspectez la courroie : craquelures, effilochage. Sifflement au démarrage = courroie usée ou tendeur défaillant. Remplacez tous les 60-100k km.")),
        (['moteur', 'demarr'], ('Moteur tourne mais ne démarre pas', "Vérifiez pompe à essence (écoutez le bourdonnement), étincelle (sortez une bougie) et compression. Aussi: batterie, démarreur, immobilisateur.")),
        (['moteur', 'cogner'], ('Cognement/cliquetis moteur', "Cognement de détonation (utilisez essence 95/98). Coups de bielle (sérieux - usure roulements). Vérifiez calage et niveau huile.")),
        (['moteur', 'ralenti'], ('Ralenti irrégulier', "Vérifiez fuites d'air, papier dessementé, valve de ralenti, bougies. Nettoyez papillon et capteur MAF.")),

        # BATTERIE / ELECTRICITE
        (['batterie', 'morte'], ('Batterie à plat', "Démarrez avec câbles ou remplacez la batterie. Vérifiez alternateur (13.5-14.5V en marche). Nettoyez bornes.")),
        (['batterie', 'defaut'], ('Décharge de batterie', "Utilisez un multimètre en série pour trouver le courant parasite. Vérifiez: éclairage intérieur, accessoires, relais bloqués.")),
        (['batterie', 'charge'], ('Batterie ne charge pas', "Vérifiez tension alternateur (13.5-14.5V en marche). Vérifiez courroie, câblage et âge batterie (remplacez tous les 4-5 ans).")),
        (['batterie', 'voyant'], ('Témoin batterie allumé', "Alternateur défaillant, courroie lâche, régulateur défaillant ou connexions corrodées. Testez l'alternateur immédiatement.")),
        (['batterie', 'borne'], ('Bornes de batterie corrodées', "Nettoyez avec bicarbonate de soude + brosse métallique. Appliquez graisse diélectrique. Vérifiez câbles et serrage.")),

        # DIRECTION
        (['direction', 'vibrat'], ('Vibration de direction', "Problème d'équilibrage des roues — faites équilibrer. Aussi: disques voilés, roue tordue, rotules usées.")),
        (['direction', 'tire'], ("Voiture tire d'un côté", "Vérifiez pression pneus (inégale), parallélisme, étrier frein bloqué, suspension usée. Faites tourner les pneus et parallélisme.")),
        (['direction', 'dure'], ('Direction dure/lourde', "Vérifiez niveau liquide de direction assistée. Pompe défaillante, crémaillère, ou fuite dans le système.")),
        (['direction', 'bruit'], ('Bruit de direction', "Claquement en tournant = joint CV (avant). Bruit sourd = rotule ou tige de direction. Whining = pompe de direction basse.")),
        (['direction', 'jeu'], ('Jeu excessif direction', "Vérifiez tirants, silentblocs crémaillère, rotules et bras de suspension. Jeu = composants usés.")),

        # BOITE DE VITESSES
        (['boite', 'patinage'], ('Boite qui patine', "Vérifiez niveau et état huile de boite (rouge/rose, pas marron). Peut nécessiter réglage, vidange ou réfection.")),
        (['boite', 'vitesse'], ('Vitesses difficiles', "Vérifiez huile boite. Peut être: niveau bas, embrayage usé (manuel), solénoïdes (automatique) ou calculateur.")),
        (['boite', 'bruit'], ('Bruit de boite', "Whining en point mort = roulement arbre d'entrée. Claquement = cardan/arbres. Grincement = synchros usées (manuelle).")),
        (['boite', 'huile'], ('Fuite huile de boite', "Vérifiez joint de carter, durées, joints d'essieu et bouchon de vidange. Rouge = transmission. Marron = vieux fluide.")),

        # PNEUS
        (['pneu', 'usure'], ('Usure inégale des pneus', "Faites vérifier le parallélisme. Motif d'usure: centre = trop gonflé, bords = pas assez, un côté = parallélisme, cupules = amortisseurs.")),
        (['pneu', 'crevaison'], ('Pneu crevé/plat', "Utilisez roue de secours ou kit de réparation. Inspectez pneu. Bouchon/réparation si réparable, remplacez si flanc endommagé.")),
        (['pneu', 'pression'], ('Basse pression pneu', "Cherchez crevaison (clous, vis). Gonflez selon spec (étiquette portière). Capteur TPMS peut nécessiter remplacement batterie.")),
        (['pneu', 'vibrat'], ('Vibration de pneu', "Faites équilibrer les roues. Vérifiez: usure irrégulière, jante tordue, cordage décollé ou boulons desserrés.")),

        # SYSTEME DE REFROIDISSEMENT
        (['liquide', 'refroidissement'], ('Fuite de liquide de refroidissement', "Vérifiez radiateur, durées, pompe à eau et chauffage. Utilisez colorant UV pour les fuites cachées.")),
        (['liquide', 'bas'], ('Niveau liquide de refroidissement bas', "Remplissez avec le bon mélange. Vérifiez les fuites. Si récurrent = joint de culasse (bulles d'échappement, huile laiteuse).")),
        (['chauffage', 'marche'], ('Chauffage ne fonctionne pas', "Vérifiez niveau liquide, thermostat (ouvert = pas de chaleur), chauffage bouché ou actuateur de volet défaillant.")),
        (['climatisation', 'froid'], ('Climatisation ne refroidit pas', "Vérifiez niveau fluide frigorigène, compresseur, condenseur et détendeur. Cherchez fuites avec UV. Rechargez.")),
        (['climatisation', 'odeur'], ('Mauvaise odeur climatisation', "Remplacez filtre d'habitacle. Nettoyez/remplacez évaporateur. Utilisez spray désinfectant. Moisissure/bactéries dans le système.")),

        # ECHAPPEMENT
        (['echappement', 'fumee'], ('Fumée d\'échappement', "Blanche = liquide (joint culasse). Bleue = huile (joints segments). Noire = mélange riche. Faites test compression.")),
        (['echappement', 'odeur'], ("Odeur d'échappement dans l'habitacle", "Vérifiez fuites d'échappement sous la voiture. Collecteur fissuré, tube craquelé ou joint défaillant. CO est mortel — réparez vite.")),

        # SUSPENSION
        (['suspension', 'bruit'], ('Bruit de suspension', "Claquement sur dosserets = amortisseurs/rotules. Siffltement = silentblocs. Test rebond: poussez l'aile, doit se stabiliser en 1-2 rebonds.")),
        (['suspension', 'rebond'], ('Rebonds excessifs', "Amortisseurs/struts usés. Remplacez en paire. Test rebond: voiture doit se stabiliser en 2 rebonds. Plus = amortisseurs morts.")),
        (['amortisseur', 'strut'], ('Amortisseurs/struts usés', "Remplacez si: roulis excessif, plongée au freinage, rebonds, ou fuite de liquide. Faites parallélisme après.")),

        # SYSTEME DE CARBURANT
        (['pompe', 'essence'], ('Pompe à essence défaillante', "Écoutez le bruit de la pompe à la clé (2 sec amorce). Pas de bruit = pompe/fusible/relais défaillant. Mesurez pression.")),
        (['filtre', 'essence'], ('Filtre à essence bouché', "Remplacez filtre (tous les 30-50k km). Symptômes: hésitation, perte de puissance, démarrage difficile.")),
        (['consommation'], ('Consommation excessive', "Vérifiez pression pneus, filtre à air, bougies, capteurs O2 et conduite. Nettoyez MAF et papillon.")),
        (['injecteur'], ('Problème d\'injecteur', "Nettoyez ou remplacez. Symptômes: raté, ralenti irrégulier, conso élevée. Nettoyant injecteur ou nettoyage pro.")),

        # DEMARREUR / ALLUMAGE
        (['demarreur', 'claquement'], ('Claquement de démarreur', "Batterie faible, solénoïde défaillant ou connexions corrodées. Vérifiez tension batterie en premier.")),
        (['demarreur', 'marche'], ('Démarreur ne fonctionne pas', "Vérifiez batterie, relais, contacteur, sélecteur de vitesse (auto) et moteur démarreur. Testez avec fil jumper.")),
        (['cle', 'demarrage'], ('Clé ne démarre pas la voiture', "Vérifiez: batterie clé (sans contact), immobilisateur, pédale frein (démarrage bouton), sélecteur vitesse (auto) et démarreur.")),

        # FUMEE / ODEUR
        (['fumee', 'capot'], ("Fumée sous le capot", "Arrêtez-vous et coupez le moteur. Vérifiez: fuite liquide sur moteur chaud, huile sur échappement, court-circuit. Laissez refroidir.")),
        (['odeur', 'brulage'], ('Odeur de brûlé', "Caoutchouu = courroie/durée sur pièce chaude. Huile = fuite sur échappement. Plastique = électrique. Trouvez la source.")),

        # VIBRATION
        (['vibration', 'roue'], ('Vibration de roue', "Faites équilibrer les roues en premier. Aussi: bourrage de pneu, jante tordue, disque voilé, suspension usée.")),
        (['vibration', 'volant'], ('Vibration au volant', "Problème d'équilibrage roues AV ou disques frein AV voilés. Équilibrage d'abord, puis vérifiez disques si au freinage.")),

        # GENERAL
        (['voiture', 'tire'], ('Voiture tire d\'un côté', "Vérifiez: pression pneus, parallélisme, étrier frein bloqué, suspension usée, taille pneu inégale. Commencez par pression.")),
        (['voyant', 'tableau'], ('Témoin tableau de bord', "Identifiez le symbole. Courants: moteur (jaune/rouge), ABS, huile, batterie, température. Lisez codes OBD2.")),
        (['voiture', 'tremble'], ('Voiture qui tremble', "Vérifiez: équilibrage roues, silentblocs moteur, bougies (raté), disques voilés ou suspension. Notez quand ça arrive.")),
        (['voiture', 'rouille'], ('Rouille/corrosion', "Traitez la rouille surface avec convertisseur + peinture. Rouille structurelle = inspection pro. Prévention: sous-couche, laver sous caisse l'hiver.")),
    ]
}


def diagnose_issue(text, lang):
    text_lower = text.lower()
    matches = []
    for keywords, (diag, solution) in RULES.get(lang, []):
        keyword_hits = sum(1 for word in keywords if word in text_lower)
        if keyword_hits == len(keywords):
            matches.append((10 + keyword_hits, diag, solution))
        elif keyword_hits > 0:
            matches.append((keyword_hits, diag, solution))

    if matches:
        matches.sort(key=lambda x: (-x[0]))
        return matches[0][1], matches[0][2]

    return ('Unknown issue', 'Please provide more details or consult a professional.')
