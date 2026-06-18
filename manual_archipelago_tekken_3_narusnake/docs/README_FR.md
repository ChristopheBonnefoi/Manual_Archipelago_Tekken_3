# Manuel Archipelago pour Tekken 3

## Bienvenue
Bienvenue dans mon Manual Archipelago pour **Tekken 3** sur PlayStation. Utilisez **Tekken 3 (Everything Unlocked)** ou une sauvegarde avec tout d?bloqu?. Une sauvegarde ? 100 % est fortement recommand?e pour pouvoir terminer toutes les seeds sans refaire le d?blocage du jeu ? la main.

## ?tat du projet
Ce projet est actuellement en **b?ta**. Il couvre le jeu complet ainsi que les modes solo repr?sent?s dans ce manual.

## Informations personnages
- **Kuma et Panda** sont consid?r?s comme deux personnages diff?rents m?me s'ils partagent la m?me fin. Pour s?lectionner Panda, utilisez Croix et Rond sur la manette PlayStation.
- **Eddy et Tiger** sont consid?r?s comme deux personnages diff?rents. Pour s?lectionner Tiger, appuyez sur Triangle sur Eddy.
- **Mokujin** est s?par? en **Mokujin (M)** et **Mokujin (F)**. Tous les goals globaux ne demandent pas forc?ment les deux, mais cette s?paration permet des goals par genre et des teams plus propres.

## Informations modes de jeu
- **Arcade Mode** : terminez le mode Arcade avec chaque personnage disponible.
- **Time Attack Mode** : terminez les routes Time Attack avec chaque personnage disponible.
- **Survival Mode** : r?alisez les checks de victoires du mode Survie avec chaque personnage disponible.
- **Team Battle Mode** : gagnez les checks de tailles d'?quipe et les teams th?matiques. Pour le **Full Game Completion**, si Team Battle est activ?, il faut aller jusqu'? la progression de s?lection ? 8 personnages.
- **Tekken Ball Mode** : battez votre adversaire au volley, uniquement avec les personnages jouables que vous avez d?bloqu?s.
- **Tekken Force Mode** : terminez Tekken Force avec chaque personnage. Le mode est maintenant mieux cadr? par les objets **Progressive Tekken Force Stage**.

## Goals
- **King of Iron Fist Tournament Token** : r?cup?rez le nombre requis de **KIFT Emblem**.
- **All Arcade Mode Clear**, avec variantes gar?ons/filles.
- **All Tekken Ball Mode Clear**, avec variantes gar?ons/filles.
- **All Time Attack Mode Clear**, avec variantes gar?ons/filles.
- **All Tekken Force Mode Clear**, avec variantes gar?ons/filles.
- **All Survival Mode Clear**, avec variantes gar?ons/filles.
- **Full Game Completion**, avec variantes gar?ons/filles et variantes avec KIFT Emblems.

## Options YAML
- **Modes de jeu** : Arcade, Time Attack, Survival, Team Battle, Tekken Ball et Tekken Force peuvent ?tre activ?s ou d?sactiv?s. Les goals sp?cifiques forcent leur mode requis pour ?viter un goal impossible.
- **R?glages de gameplay** : les pools **Difficulty**, **Fight Count** et **Round Time** sont optionnels et d?sactiv?s par d?faut.
- **KIFT Emblems requis** : les goals ? tokens peuvent demander entre **1 et 100** KIFT Emblems.

## Objets filler
Les **TEKKEN Points** restent comme fallback technique, mais le filler normal utilise maintenant des objets li?s aux personnages dans la cat?gorie visible **Filler**. Ces objets ont un count de base ? `0`, donc ils sont g?n?r?s uniquement quand Archipelago doit remplir des emplacements libres. Bref, les slips maudits n'envahissent pas le pool tant qu'on ne leur demande pas de travailler.

## Fonctionnalit?s futures
- Nouveaux goals et checks th?matiques.
- Passes d'?quilibrage sur les r?glages optionnels.
- Documentation suppl?mentaire pour les teams et rivalit?s moins ?videntes.

## Notes de version

### Version 1.1.0 - Massive update

**Modifications**
- Ajout des options YAML fa?on Tekken 2 pour activer ou d?sactiver chaque mode de jeu.
- Ajout des pools optionnels **Difficulty**, **Fight Count** et **Round Time**, d?sactiv?s par d?faut.
- Ajout de l'option configurable **KIFT Emblems Required** pour les goals ? tokens.
- Les **KIFT Emblems** sont maintenant ajout?s au pool uniquement si le goal s?lectionn? les demande.
- Ajout du filler dynamique li? aux personnages et retraduction des fillers en anglais en gardant l'humour de la version FR.
- Remplacement du filler g?n?r? **TEKKEN Points** par des fillers dynamiques al?atoires, avec TEKKEN Points conserv? comme fallback.
- Nettoyage des restes de template dans `events.json` et `regions.json`.
- Ajout de cl?s de tri pour am?liorer l'ordre des checks dans le client Manual.
- Mise ? jour du template YAML avec tous les goals actuels.
- Documentation du fait que le **Full Game Completion** avec Team Battle activ? demande la progression Team Battle jusqu'? 8 personnages.

### Version 1.0.0 - Release Update

**Modifications**
- Ajout des checks Survival, Tekken Ball et rivalités pour chaque personnage.
- Correction de l'orthographe de Doctor Bosconovitch.
- Refonte de la logique Tekken Force et Team Battle.
- Ajout des objets de progression Tekken Force Stage, Team Battle et Tekken Ball à la génération de seed.

### Version 0.2.0 - Goal Update

**Modifications**
- Ajout des items de ballons pour le **Mode Tekken Ball**.
- Ajout des niveaux progressifs pour le **Mode Tekken Force**.
- Restructuration des fichiers `items.json` et `locations.json`.
- Ajout de plusieurs goals.

### Version 0.1.1

**Modifications**
- Correction de la logique de **Mokujin** pour pouvoir faire ses checks avec l'une ou l'autre version.
- Correction du goal **All Arcade Mode Clear** pour ne demander qu'une seule version de **Mokujin**.

### Version 0.1.0

**Modifications**
- Cr?ation des objets pour les cat?gories **Characters**, **Game Mode** et **Difficulty**.
- Ajout des premiers goals.
- Ajout des checks pour les modes **Arcade**, **Time Attack**, **Survival**, **Tekken Ball** et **Tekken Force**.

## Comment contribuer
Toutes les contributions sont les bienvenues : retours de jeu, corrections, documentation ou nouvelles id?es de checks.

## Contact
Si vous avez des questions ou si vous ?tes streamer, contactez-nous sur le Discord Archipelago ou ouvrez une issue GitHub. Je r?pondrai d?s que possible.
