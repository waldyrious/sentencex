import re

from sentencex.base import Language


class Danish(Language):
    language = "da"

    abbreviations = {
        "adm",
        "adr",
        "afd",
        "afs",
        "al",
        "alm",
        "ang",
        "ank",
        "anm",
        "ann",
        "ansvh",
        "apr",
        "årg",
        "årh",
        "årl",
        "arr",
        "ass",
        "att",
        "aud",
        "aug",
        "aut",
        "bd",
        "bdt",
        "bet",
        "bhk",
        "bio",
        "biol",
        "bk",
        "bl.a",
        "bot",
        "br",
        "bto",
        "ca",
        "cal",
        "cirk",
        "cit",
        "co",
        "cpr-nr",
        "cvr-nr",
        "d.å",
        "d.æ",
        "d.d",
        "d.e",
        "d.m",
        "d.s.s",
        "d.s",
        "d.y",
        "da",
        "dav",
        "dec",
        "def",
        "del",
        "dep",
        "diam",
        "din",
        "dir",
        "disp",
        "distr",
        "do",
        "dobb",
        "dr",
        "ds",
        "dvs",
        "e.b",
        "e.kr",
        "e.l",
        "e.o",
        "e.v.t",
        "eftf",
        "eftm",
        "egl",
        "eks",
        "eksam",
        "ekskl",
        "eksp",
        "ekspl",
        "el",
        "emer",
        "endv",
        "eng",
        "enk",
        "etc",
        "eur",
        "evt",
        "exam",
        "f.å",
        "f.eks",
        "f.kr",
        "f.m",
        "f.n",
        "f.o.m",
        "f.o",
        "f.s.v",
        "f.t",
        "f.v.t",
        "f",
        "fa",
        "fær",
        "fakt",
        "feb",
        "fec",
        "ff",
        "fg",
        "fhv",
        "fig",
        "fl",
        "flg",
        "fm",
        "fmd",
        "forb",
        "foreg",
        "foren",
        "forf",
        "forh",
        "fork",
        "form",
        "forr",
        "fors",
        "forsk",
        "forts",
        "fp",
        "fr",
        "frk",
        "fru",
        "fuldm",
        "fung",
        "fys",
        "g.d",
        "g.m",
        "g",
        "gd",
        "gdr",
        "gg",
        "gh",
        "gl",
        "gn",
        "gns",
        "gr",
        "grdl",
        "gross",
        "h.a",
        "h.c",
        "hdl",
        "henh",
        "henv",
        "hf",
        "hft",
        "hhv",
        "hort",
        "hosp",
        "hpl",
        "hr",
        "hrs",
        "hum",
        "i.e",
        "i",
        "ib",
        "ibid",
        "if",
        "ifm",
        "ill",
        "indb",
        "indreg",
        "ing",
        "inkl",
        "insp",
        "instr",
        "isl",
        "istf",
        "jan",
        "jf",
        "jfr",
        "jnr",
        "jr",
        "jul",
        "jun",
        "jur",
        "jvf",
        "kal",
        "kap",
        "kat",
        "kbh",
        "kem",
        "kgl",
        "kin",
        "kl",
        "kld",
        "km/t",
        "knsp",
        "komm",
        "kons",
        "korr",
        "kp",
        "kr",
        "kst",
        "kt",
        "ktr",
        "kv",
        "kvt",
        "l.c",
        "l",
        "lab",
        "lat",
        "lb.",
        "lb.nr",
        "lb",
        "lejl",
        "lgd",
        "lic",
        "lign",
        "lin",
        "ling.merc",
        "litt",
        "lø",
        "lok",
        "lrs",
        "ltr",
        "m.a.o",
        "m.fl.st",
        "m.m",
        "m",
        "m/",
        "ma",
        "mag",
        "maks",
        "mar",
        "mat",
        "matr.nr",
        "md",
        "mdl",
        "mdr",
        "mdtl",
        "med",
        "medd",
        "medflg",
        "medl",
        "merc",
        "mezz",
        "mf",
        "mfl",
        "mgl",
        "mhp",
        "mht",
        "mi",
        "mia",
        "mio",
        "ml",
        "mods",
        "modsv",
        "modt",
        "mr",
        "mrk",
        "mrs",
        "ms",
        "mul",
        "mv",
        "mvh",
        "n.br",
        "n.f",
        "n",
        "nat",
        "ned",
        "nedenn",
        "nedenst",
        "nederl",
        "nkr",
        "nl",
        "no",
        "nord",
        "nov",
        "nr",
        "nto",
        "nuv",
        "o.a",
        "ø.f",
        "o.fl.st",
        "o.g",
        "o.h",
        "o.m.a",
        "o",
        "obj",
        "obl",
        "obs",
        "odont",
        "oecon",
        "off",
        "ofl",
        "okt",
        "omg",
        "omr",
        "omtr",
        "on",
        "op.cit",
        "opg",
        "opl",
        "opr",
        "org",
        "orig",
        "osfr",
        "osv",
        "øv",
        "ovenn",
        "ovenst",
        "overs",
        "ovf",
        "øvr",
        "oz",
        "p.a",
        "p.b.v",
        "p.c",
        "p.m.v",
        "p.p",
        "p.s",
        "p.t",
        "p.v.a",
        "p.v.c",
        "p",
        "pæd",
        "par",
        "partc",
        "pass",
        "pct",
        "pd",
        "pens",
        "perf",
        "pers",
        "pg",
        "pga",
        "pgl",
        "ph.d",
        "ph",
        "pharm",
        "phil",
        "pinx",
        "pk",
        "pkt",
        "pl",
        "pluskv",
        "polit",
        "polyt",
        "port",
        "pos",
        "pp",
        "pr",
        "præd",
        "præf",
        "præp",
        "præs",
        "præt",
        "prc",
        "priv",
        "prod",
        "prof",
        "pron",
        "psych",
        "pt",
        "q.e.d",
        "rad",
        "red",
        "ref",
        "reg",
        "regn",
        "rel",
        "rep",
        "repr",
        "rest",
        "rk",
        "russ",
        "s.å",
        "s.br",
        "s.d",
        "s.e",
        "s.f",
        "s.m.b.a",
        "s.u",
        "s",
        "s/",
        "sa",
        "sædv",
        "såk",
        "sb",
        "sc",
        "scient",
        "sek",
        "sekr",
        "sem",
        "sen",
        "sep",
        "sept",
        "sg",
        "sign",
        "sj",
        "skr",
        "skt",
        "slutn",
        "sml",
        "smp",
        "sms",
        "smst",
        "sø",
        "soc",
        "sort",
        "sp",
        "spec",
        "spm",
        "spr",
        "spsk",
        "st",
        "stk",
        "str",
        "stud",
        "subj",
        "subst",
        "suff",
        "sup",
        "suppl",
        "sv",
        "t.h",
        "t.o.m",
        "t.v",
        "t",
        "tab",
        "td",
        "tdl",
        "tdr",
        "techn",
        "tekn",
        "temp",
        "th",
        "ti",
        "tidl",
        "tilf",
        "tilh",
        "till",
        "tilsv",
        "tjg",
        "tlf",
        "tlgr",
        "to",
        "tr",
        "trp",
        "tv",
        "ty",
        "u.å",
        "u.p",
        "u.st",
        "u",
        "uafh",
        "ubf",
        "ubøj",
        "udb",
        "udbet",
        "udd",
        "udg",
        "uds",
        "ugtl",
        "ulin",
        "ult",
        "undt",
        "univ",
        "v.f",
        "vær",
        "var",
        "vb",
        "vbsb",
        "vedk",
        "vedl",
        "vedr",
        "vejl",
        "vh",
        "vol",
        "vs",
        "vsa",
        "zool",
    }

    def continue_in_next_word(self, text_after_boundary) -> bool:
        if re.match(r"^\W*[0-9a-z]", text_after_boundary):
            return True