# phwcookiecutter 

Dyma dempled ystorfa ar gyfer prosiectau Python yn Iechyd Cyhoeddus Cymru (ICC).

- I greu ystorfa trwy ddefnyddio'r templed, gweler y [Canllaw cyflym](#Canllaw-cyflym---creu-ystorfa-trwy-ddefnyddio-r-templed-hwn).
- I weld beth mae'r templed yn ei gynnwys, gweler [Beth mae hyn yn ei wneud?](#Beth-mae-hyn-yn-ei-wneud)
- I ddatblygu'ch cookiecutter eich hun yn seiliedig ar yr un yma, [fforchiwch (fork) yr ystorfa hon](https://github.com/Public-Health-Wales/phwcookiecutter/fork).
- I awgrymu newidiadau neu atgyweiriadau i'r cookiecutter hwn, [ychwanegwch fater](https://github.com/Public-Health-Wales/phwcookiecutter/issues) neu [cysylltwch â'r cynhalwyr](mailto:phw.dkrdatascience@wales.nhs.uk). 

# Iaith

Mae testun iaith naturiol sy'n wynebu defnyddwyr yn yr ystorfa feddalwedd hon ar gael yn ddwyieithog Cymraeg-Saesneg. Os nad yw unrhyw destun sy'n wynebu defnyddwyr yn ddwyieithog, rhowch wybod i ni drwy gyflwyno mater neu gysylltu â ni trwy’r cyfeiriad e-bost cyswllt.
Fel ystorfa feddalwedd, gall yr ystorfa hon gynnwys cynnwys mewn ieithoedd rhaglennu neu fformatau eraill y gellir eu darllen gan gyfrifiadur. Bydd y cynnwys hwn bob amser yn aros yn ei ffurf wreiddiol. Bydd sylwadau sydd wedi'u hymgorffori yn y cod hefyd yn aros yn yr iaith a ddefnyddir gan y datblygwr. Mae'r ddogfen LICENSE yn ddogfen gyfreithiol safonol, nad yw wedi'i chynhyrchu o fewn GIG Cymru, ac mae ar gael yn Saesneg yn unig. Gall enwau ffeiliau a llwybrau ffeil sy'n defnyddio confensiynau o safon diwydiant (e.e. README.md) fod yn Saesneg yn unig. 

Y brif  gangen (main) yw'r fersiwn cyhoeddus o'r ystorfa. Wrth ddatblygu ystorfa ffynhonnell agored, gall y datblygwyr gwreiddiol neu gyfranwyr eraill greu canghennau eraill. Hyd nes y derbynnir newidiadau, trwy gyfuno â’r brif gangen (main), gall cynnwys iaith naturiol fod mewn unrhyw iaith a ddefnyddir gan y datblygwr.  

# Canllaw cyflym - creu ystorfa trwy ddefnyddio'r templed hwn

**Mae hwn yn dempled ystorfa y gellir ei ddefnyddio ar y cyd â'r pecyn cookiecutter i greu ystorfa sy'n edrych fel y templed.** Bydd rhedeg y gorchymyn cookiecutter yn defnyddio'r fersiwn o'r ystorfa hon o GitHub yn uniongyrchol, felly nid oes angen i chi glonio'r ystorfa hon oni bai eich bod am ychwanegu at y templed.

- Bydd llawer o'r camau hyn yn cynnwys gosod pecynnau Python. Mae'n arferol gweithio mewn amgylchedd rhithwir wrth osod pecynnau Python (e.e. conda/pip). Crëwch amgylchedd i weithio ynddo fel y byddech fel arfer.
- [Gosodwch y  pecyn cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html#installation): `python -m pip install --user cookiecutter`.
- Yn eich Anogwr Gorchymyn (Command Prompt)/Terfynell, llywiwch i'r ffolder lle rydych am greu eich prosiect a rhedeg  `python -m cookiecutter https://github.com/Public-Health-Wales/phwcookiecutter.git`. Os gofynnir i chi a yw'n iawn dileu ac ail-lawrlwytho'r cookiecutter, dywedwch ie.
- Rhowch y manylion y gofynnwyd amdanynt i greu’r ystorfa.
- Llywiwch i'r ystorfa sydd newydd ei chreu.
- Rhedwch `git init` i'w chychwyn fel ystorfa git.
- Gosodwch offer i gefnogi'r gosodiad:  `python -m pip install -U pip setuptools`. 
- Gosodwch fersiwn golygadwy o'r pecyn:  `python -m pip install -e .`. Mae golygadwy yn golygu y bydd yn newid wrth i chi wneud diweddariadau i'r cod. Unwaith eto, nodwch ei bod yn arferol gweithio mewn amgylchedd rhithwir wrth osod pecynnau Python.
- Gosodwch y pre-commit hooks:  `python -m pre_commit install`. Gall y cam hwn fod ychydig yn drafferthus o ran sut mae pethau'n cael eu gosod - rhowch wybod am unrhyw broblemau.
- Ychwanegwch unrhyw linynnau rydych chi am wirio'r cipluniau (commits) ar eu cyfer i  `.nocommitstrings` (un llinell i bob llinyn, dim dyfynodau). Byddwch yn ofalus i beidio â chyflwyno’r ffeil hon (mae hynny’n cael ei gwmpasu gan y `.gitignore`). Sylwch y gellir diffodd pre-commit hooks neu beidio â’u rhedeg , felly (fel gyda'r pre-commit hook datgeliad cudd), mae hon yn haen ychwanegol o ddiogelwch yn hytrach na rhywbeth y dylid dibynnu arno ynddo'i hun i atal cyfrinachau rhag cael eu cyflwyno.
- `git add` ("stage") i greu’r ystorfa. Rydyn ni'n hoffi gwneud hyn â llaw yn VS Code fel y gallwch chi weld y ffeiliau rydych chi'n eu hychwanegu a bod yn gwbl siŵr nad ydych chi'n cyflwyno unrhyw beth nad ydych chi am ei gyflwyno.
- `git commit` yr holl newidiadau rydych wedi'u hychwanegu. Rydym yn hoffi gwneud hyn o Anogwr Gorchymyn (Command Prompt)/Terfynell, fel y gallwch weld unrhyw negeseuon am y profion yn pasio neu'n methu. Sylwch, os yw'r pre-commit hooks wedi'u gosod, gall lintio (linting) ddatgelu rhai problemau y mae'r hooks  yn eu cywiro'n awtomatig. Os bydd unrhyw un o'r pre-commit hooks yn methu, nid ydych wedi cyflwyno, ac felly bydd angen i chi "stage" unrhyw newidiadau a wneir yn awtomatig a rhoi cynnig arall ar gyflwyno.
- Gwthiwch i GitHub (creu ystorfa newydd ar GitHub a dilynwch y cyfarwyddiadau i wthio ystorfa bresennol).
- Gosodwch amddiffyniad cangen fel na all cyfranwyr wthio'n uniongyrchol i'r brif gangen (`main`). Gallwch ddod o hyd i'r opsiwn hwn yn y gosodiadau ystorfa ar GitHub.
- Ychwanegwch eich cydweithwyr at yr ystorfa a rhowch lefel briodol o fynediad iddynt. Gallwch ddod o hyd i'r opsiwn hwn yn y gosodiadau ystorfa ar GitHub.
- Dilynwch y cyfarwyddiadau yn CONTRIBUTING_cy.md i barhau i ddatblygu.
  
# Beth mae hyn yn ei wneud? 

Yn sefydlu ystorfa gyda:
- README Safonol
- MIT License (hawlfraint Iechyd Cyhoeddus Cymru)
- Cyfarwyddiadau CYFRANNU Safonol
- Strwythur ffolder addas:
  - ffolder src sy'n cynnwys pecyn. Yn gyffredinol, dylid storio cod neu biblinellau prosiect terfynol yma.
  - ffolder tests ar gyfer profion
  - Mae ffolderi ar hyn o bryd yn cynnwys enghreifftiau (y dylid eu dileu).
- pyproject.toml yn ôl yr angen i'w wneud yn fersiwn y gellir ei gosod
- Ffeil .gitnore safonol
- Ffeil config.ini wag. Ni ddylid cyflwyno na gwthio hon ( ac mae yn y .gitignore). Defnyddiwch hwn ar gyfer agweddau ar ffurfweddu megis llwybrau ffeil. Dylai'r ffeil ffurfweddu fyw yn y cyfeiriadur gwraidd er mwyn osgoi dryswch gyda fersiynau lluosog.
- Gosod precommit hooks sy'n cwmpasu cynnal profion, lintio a gwiriadau diogelwch sylfaenol
- Templedi materion a PRs (pull requests) i'w defnyddio ar GitHub
- GitHub Action ar gyfer lintio a phrofi
- Rheoli fersiynau a rhyddhau gan ddefnyddio  `bump-my-version`
