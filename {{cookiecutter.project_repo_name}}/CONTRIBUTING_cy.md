# Canllawiau Cyfrannu

Rydym wrth ein bodd â chyfraniadau! Rydym wedi llunio'r ddogfennaeth hon i'ch helpu i ddeall ein canllawiau cyfrannu. [Os oes gennych gwestiynau o hyd, cysylltwch â ni](mailto:{{cookiecutter.contact_email}}) a byddwn yn hapus i helpu.

## Dechrau arni

Os ydych yn anghyfarwydd â git a GitHub, edrychwch ar adnoddau ar ddechrau arni fel [y canllaw hwn gan GitHub](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account) neu'r [cyflwyniad hwn i git yn VSCode](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git).

Os ydych yn gweithio yn Iechyd Cyhoeddus Cymru, gallwch hepgor cam 1 a chlonio’r ystorfa ei hun. Dylid dilyn y camau eraill yn yr un modd.

1.	**Fforchiwch yr ystorfa:**
Dechreuwch trwy fforchio'r ystorfa hon i'ch cyfrif GitHub eich hun.

1.	**Cloniwch eich fforc:**
Cloniwch yr ystorfa wedi’i fforchio i'ch peiriant lleol.

1.	**Gosodwch eich copi lleol o'r pecyn a'r ystorfa:**
I weithio gyda'r pecyn yn lleol, gallwch osod fersiwn y gellir ei golygu ohono (a ddylai hefyd osod ei ddibyniaethau). Yn ogystal â gosod y pecyn fel pecyn y gellir ei olygu, dylai cyfranwyr hefyd osod y pre-commit hooks. I ddechrau cyfrannu, agorwch eich terfynell a gosodwch y pecyn a'r pre-commit hooks gan ddefnyddio:
    ```{shell}
    pip install -e .
    python -m pre_commit install
    ```
Gallwch ddarllen mwy am pre-commit hooks [isod](#pre-commit-hooks).

1.	**Defnyddiwch gangen newydd ar gyfer eich newidiadau:**
Defnyddiwch gangen newydd ar gyfer eich newidiadau bob amser. Bydd hyn yn cadw pethau'n daclus ac yn drefnus.
    ```{shell}
	git checkout -b [branch-name] main
    ```

1.	**Gwnewch eich newidiadau i'r cod:**
Gwnewch eich newidiadau i'r cod fel y byddech yn ei wneud fel arfer. Rhedwch y cod yn lleol i wirio ei fod yn gweithio.

1.	**Cyflwynwch eich newidiadau:**
Unwaith y byddwch wedi gwneud eich newidiadau, cyflwynwch nhw:
    ```{shell}
    git add name_of_changed_file
    # Ailadroddwch git add os ydych chi wedi ychwanegu sawl ffeil:**
    git commit -m "Describe your changes"
    # Arfer dda ar gyfer negeseuon cyflwyno yw
	# gorffen y frawddeg gyda "This change will [commit message]"
	# Er enghraifft: "Fix bug in error calculation"
    ```

1.	**Cyflwyno eich newidiadau i'ch fforc:**
Unwaith y byddwch wedi gwneud eich newidiadau, cyflwynwch nhw i'ch fforc ar GitHub.
    ```{shell}
    git push origin [branch-name]
    ```

1. **Agor cais cyfuno (pull request):**
Ewch i'r brif ystorfa ar GitHub, a byddwch yn gweld botwm i greu cais cyfuno newydd o'ch fforc (neu o'ch cangen os na wnaethoch chi fforchio'r ystorfa). Rhowch ddisgrifiad o'ch newidiadau. Cysylltwch â materion GitHub perthnasol o'r ôl-groniad (backlog). Cyflwyno'ch cais cyfuno a gofyn am adolygiad gan y cynhalwyr. Gwnewch yn siŵr eich bod yn profi eich newidiadau yn drylwyr cyn cyflwyno cais cyfuno. Bydd hyn yn sicrhau cywirdeb ac ansawdd y prosiect.

1.	**Ymateb i newidiadau:**
Mynd i'r afael ag unrhyw newidiadau gofynnol ar eich cangen, a chael cymeradwyaeth yr adolygwyr i gyfuno.

1.	**Cyfuno’r brif gangen (main) a’ch cangen chi:**
Cyfunwch unrhyw newidiadau ar y brif gangen â'ch cangen chi. Gallwch wneud hyn trwy lywio i'ch cangen yn yr Anogwr Gorchymyn (Command Prompt) a rhedeg:
    ```{shell}
    git fetch origin main
    git merge origin/main
    ```

1. **Diweddaru'r LOG NEWIDIADAU:**
Diweddarwch y [log newidiadau](CHANGELOG_cy.md) trwy nodi’r newidiadau rydych chi wedi'u gwneud. Dilynwch y fformat templed, sy'n seiliedig ar y [prosiect cadw log newidiadau].(https://keepachangelog.com/en/1.1.0/). Defnyddiwch y rhif fersiwn nesaf a gynhyrchir (gweler y pwynt nesaf).

1. **Cynyddu rhif y fersiwn:**
Mae'r ystorfa hon yn defnyddio `bump-my-version` i reoli fersiynau. Dylai'r ciplun (git commit) olaf cyn cyfuno PR (Cais Cyfuno - Pull Request) fod yn giplun wedi'i gynhyrchu'n awtomatig gan `bump-my-version`. Rhedwch `bump-my-version bump patch` (ar gyfer atgyweiriadau byg sy'n gydnaws tuag at yn ôl), `bump-my-version bump minor` (ar gyfer nodweddion newydd sy'n gydnaws tuag at yn ôl) neu `bump-my-version bump major` (ar gyfer newidiadau sy'n torri/ newidiadau API ac ati) yn yr Anogwr Gorchymyn/Terfynell (gellir `bump-my-version` hefyd gael ei ddisodli yn yr uchod gan `python -m bumpversion`, ond sicrhewch nad yw ei ragflaenwyr `bump2version` neu `bumpversion` yn cael eu gosod). Dylai hwn gael ei redeg a'i gyflwyno ar ôl i'r newidiadau eraill ar y gangen gael eu cymeradwyo ond cyn y cyfuno, fel bod y ciplun wedi'i dagio a'i fersiwn yn cynrychioli maint terfynol y newidiadau o'r gangen (gan gynnwys unrhyw ddiwygiadau a awgrymir gan adolygiad). Yn ogystal â gwthio'r ciplun olaf hwn, gwiriwch enw'r tag (e.e. v0.0.5; gallwch ddod o hyd iddo trwy redeg `git describe --tags --abbrev=0` yn yr Anogwr Gorchymyn) a gwthiwch y tag `git push origin {TAG NAME}`. I gael rhagor o wybodaeth am fersiynau, gweler ein nodiadau.

1.	**Cyfuno eich PR:**
Cyfuno'r PR gan ddefnyddio'r botwm ar GitHub.

## Profi

### Ysgrifennu pytests

Ceisiwch ychwanegu profion wrth ychwanegu swyddogaeth newydd.

[Mae profion yn defnyddio'r fframwaith pytest](https://pypi.org/project/pytest/). Mae profion yn cael eu storio yn y ffolder `tests`. Er mwyn i pytest ddod o hyd i brawf, rhaid i bob ffeil i’w phrofi a phrawf ddechrau gyda `test_` neu orffen gyda `_test.py`.

### Rhedeg pytests

I redeg pytests yn eich terfynell, rhedwch:
    ```{shell}
    pytest
    ```
yn eich cyfeiriadur gwraidd.

## Pre-commit hooks
M
ae pre-commit hooks yn gamau gweithredu sy'n cael eu rhedeg yn awtomatig, fel arfer ar bob ciplun, i gyflawni set gyffredin o dasgau. Mae pre-commit hooks yn nodwedd diogelwch i leihau (ond nid dileu) y risg bod rhai cyfrinachau, ffeiliau data mawr, ac allbynnau llyfr nodiadau Jupyter yn cael eu hychwanegu at yr ystorfa’n ddamweiniol. Mae'r pre-commit hooks ar yr ystorfa hon hefyd yn helpu i sicrhau ansawdd cod trwy redeg amrywiol wiriadau lintio (linting) a rhedeg pecyn brofi awtomataidd y pecyn.

Weithiau efallai y byddwch am ddiffodd pre-commit hook dros dro (er enghraifft, os yw'n cymryd amser hir). Gallwch wneud hyn [trwy osod y newidyn amgylchedd SKIP](https://pre-commit.com/#temporarily-disabling-hooks) e.e. . set SKIP=the_hook_i_want_to_skip.

