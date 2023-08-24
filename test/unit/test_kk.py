import pytest

from sentencesegmenter import segment

# ruff: noqa: E501
tests = [
    (
        "Мұхитқа тікелей шыға алмайтын мемлекеттердің ішінде Қазақстан - ең үлкені.",
        ["Мұхитқа тікелей шыға алмайтын мемлекеттердің ішінде Қазақстан - ең үлкені."],
    ),
    pytest.param(
        "Оқушылар үйі, Достық даңғылы, Абай даналығы, ауыл шаруашылығы – кім? не?",
        ["Оқушылар үйі, Достық даңғылы, Абай даналығы, ауыл шаруашылығы – кім?", "не?"],
        marks=pytest.mark.xfail,
    ),
    (
        "Әр түрлі өлшемнің атауы болып табылатын м (метр), см (сантиметр), кг (киллограмм), т (тонна), га (гектар), ц (центнер), т. б. (тағы басқа), тәрізді белгілер де қысқарған сөздер болып табылады.",
        [
            "Әр түрлі өлшемнің атауы болып табылатын м (метр), см (сантиметр), кг (киллограмм), т (тонна), га (гектар), ц (центнер), т. б. (тағы басқа), тәрізді белгілер де қысқарған сөздер болып табылады."
        ],
    ),
    (
        "Мысалы: обкомға (облыстық комитетке) барды, ауаткомда (аудандық атқару комитетінде) болды, педучилищеге (педагогтік училищеге) түсті, медпункттің (медициналық пункттің) алдында т. б.",
        [
            "Мысалы: обкомға (облыстық комитетке) барды, ауаткомда (аудандық атқару комитетінде) болды, педучилищеге (педагогтік училищеге) түсті, медпункттің (медициналық пункттің) алдында т. б."
        ],
    ),
    (
        "Елдің жалпы ішкі өнімі ЖІӨ (номинал) = $225.619 млрд (2014)",
        ["Елдің жалпы ішкі өнімі ЖІӨ (номинал) = $225.619 млрд (2014)"],
    ),
    (
        "Ресейдiң әлеуметтiк-экономикалық жағдайы.XVIII ғасырдың бiрiншi ширегiнде Ресейге тән нәрсе.",
        [
            "Ресейдiң әлеуметтiк-экономикалық жағдайы.",
            "XVIII ғасырдың бiрiншi ширегiнде Ресейге тән нәрсе.",
        ],
    ),
    (
        "(«Егемен Қазақстан», 7 қыркүйек 2012 жыл. №590-591); Бұл туралы кеше санпедқадағалау комитетінің облыыстық департаменті хабарлады. («Айқын», 23 сəуір 2010 жыл. № 70).",
        [
            "(«Егемен Қазақстан», 7 қыркүйек 2012 жыл. №590-591); Бұл туралы кеше санпедқадағалау комитетінің облыыстық департаменті хабарлады.",
            "(«Айқын», 23 сəуір 2010 жыл. № 70).",
        ],
    ),
    (
        "Иран революциясы (1905 — 11) және азаматтық қозғалыс (1918 — 21) кезінде А. Фарахани, М. Кермани, М. Т. Бехар, т.б. ақындар демократиялық идеяның жыршысы болды.",
        [
            "Иран революциясы (1905 — 11) және азаматтық қозғалыс (1918 — 21) кезінде А. Фарахани, М. Кермани, М. Т. Бехар, т.б. ақындар демократиялық идеяның жыршысы болды."
        ],
    ),
    (
        "Владимир Федосеев: Аттар магиясы енді жоқ http://www.vremya.ru/2003/179/10/80980.html",
        ["Владимир Федосеев: Аттар магиясы енді жоқ http://www.vremya.ru/2003/179/10/80980.html"],
    ),
    ("Бірақ оның енді не керегі бар? — деді.", ["Бірақ оның енді не керегі бар? — деді."]),
    (
        "Сондықтан шапаныма жегізіп отырғаным! - деп, жауап береді.",
        ["Сондықтан шапаныма жегізіп отырғаным! - деп, жауап береді."],
    ),
    (
        "Б.з.б. 6 – 3 ғасырларда конфуцийшілдік, моизм, легизм мектептерінің қалыптасуы нәтижесінде Қытай философиясы пайда болды.",
        [
            "Б.з.б. 6 – 3 ғасырларда конфуцийшілдік, моизм, легизм мектептерінің қалыптасуы нәтижесінде Қытай философиясы пайда болды."
        ],
    ),
    (
        "'Та марбута' тек сөз соңында екі түрде жазылады:",
        ["'Та марбута' тек сөз соңында екі түрде жазылады:"],
    ),
]


@pytest.mark.parametrize("text,expected_sents", tests)
def test_segment(text, expected_sents):
    assert list(segment("kk", text)) == expected_sents
