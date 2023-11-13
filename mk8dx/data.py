from __future__ import annotations

from typing import Optional
from enum import Enum
import string
from jaconv.conv_table import H2HK_TABLE, Z2H_DK, Z2H_A

# make translate dict
_TRANSLATE_TABLE = \
    dict(zip(map(ord, string.ascii_uppercase), string.ascii_lowercase)) \
    | H2HK_TABLE \
    | Z2H_DK \
    | {k: v.lower() for k, v in Z2H_A.items()}

_ALL_TRACK_DICT = {}


def _translate(text: str):
    return text.translate(_TRANSLATE_TABLE)


class Console(Enum):

    __slots__ = (
        'name',
        'name_ja',
        'abbr',
        'abbr_ja'
    )

    def __new__(cls: type[Console], id: int, *_) -> Console:
        obj = object.__new__(cls)
        obj._value_ = id
        return obj

    def __init__(
        self,
        _: int,
        name: str,
        name_ja: Optional[str],
        abbr: str,
        abbr_ja: Optional[str],
    ):
        self.name: str = name
        self.name_ja: Optional[str] = name_ja
        self.abbr: str = abbr
        self.abbr_ja: Optional[str] = abbr_ja

    @property
    def id(self) -> int:
        return self._value_

    @property
    def cup(self) -> Cup:
        i = id // 4
        return Cup(i)

    SNES = (
        0,
        'Super Nintendo Entertainment System',
        'スーパーファミコン',
        'SNES',
        'SFC'
    )
    N64 = (
        1,
        'Nintendo 64',
        'NINTENDO64',
        'N64',
        None
    )
    GBA = (
        2,
        'Game Boy Advance',
        'ゲームボーイアドバンス',
        'GBA',
        None
    )
    GCN = (
        3,
        'Nintendo GameCube',
        'ニンテンドー ゲームキューブ',
        'GCN',
        'GC'
    )
    DS = (
        4,
        'Nintendo DS',
        'ニンテンドーDS',
        'DS',
        None
    )
    WII = (
        5,
        'Wii',
        None,
        'Wii',
        None
    )
    N3DS = (
        6,
        'Nintendo 3DS',
        'ニンテンドー3DS',
        '3DS',
        None
    )
    WU = (
        7,
        'Wii U',
        None,
        'WU',
        None
    )
    NS = (
        8,
        'Nintendo Switch',
        None,
        'NS',
        None
    )
    TOUR = (
        9,
        'Mario Kart Tour',
        'マリオカート ツアー',
        'Tour',
        None
    )


class Cup(Enum):

    __slots__ = (
        'name',
        'name_ja'
    )

    def __new__(cls: type[Cup], id: int, *_) -> Cup:
        obj = object.__new__(cls)
        obj._value_ = id
        return obj

    def __init__(
        self,
        _: int,
        name: str,
        name_ja: str
    ):
        self.name = name
        self.name_ja = name_ja

    @property
    def id(self) -> int:
        return self.value

    @property
    def full_name(self) -> str:
        return self.name + ' Cup'

    @property
    def full_name_ja(self) -> str:
        return self.name_ja + 'カップ'

    @property
    def tracks(self) -> list[Track]:
        if self.id == -1:
            return []
        # unreleased tracks
        if self.id >= 14:
            return []
        i = self.id * 4
        return [Track(i), Track(i+1), Track(i+2), Track(i+3)]

    @property
    def position(self) -> tuple[int]:
        x = self.id % 6
        y = self.id // 6
        return (x, y)

    @property
    def prefix(self) -> Optional[str]:
        x, y = self.position
        if y >= 2:
            return 'b'
        if x >= 4:
            return 'd'
        if y == 1:
            return 'r'

    MUSHROOM = (
        0,
        'Mushroom',
        'キノコ'
    )
    FLOWER = (
        1,
        'Flower',
        'フラワー'
    )
    STAR = (
        2,
        'Star',
        'スター'
    )
    SPECIAL = (
        3,
        'Special',
        'スペシャル'
    )
    EGG = (
        4,
        'Egg',
        'たまご'
    )
    CROSSING = (
        5,
        'Crossing',
        'どうぶつ'
    )
    SHELL = (
        6,
        'Shell',
        'こうら'
    )
    BANANA = (
        7,
        'Banana',
        'バナナ'
    )
    LEAF = (
        8,
        'Leaf',
        'このは'
    )
    LIGHTNING = (
        9,
        'Lightning',
        'サンダー'
    )
    TRIFORCE = (
        10,
        'Triforce',
        'ゼルダ'
    )
    BELL = (
        11,
        'Bell',
        'ベル'
    )
    GOLDEN_DASH = (
        12,
        'Golden Dash',
        'パワフル'
    )
    LUCKY_CAT = (
        13,
        'Lucky Cat',
        'まねきネコ'
    )
    TURNIP = (
        14,
        'Turnip',
        'カブ'
    )
    PROPELLER = (
        15,
        'Propeller',
        'プロペラ'
    )
    ROCK = (
        16,
        'Rock',
        'ゴロいわ'
    )
    MOON = (
        17,
        'Moon',
        'ムーン'
    )
    FRUIT = (
        18,
        'Fruit',
        'フルーツ'
    )
    BOOMERANG = (
        19,
        'Boomerang',
        'ブーメラン'
    )
    FEATHER = (
        20,
        'Feather',
        'ハネ'
    )
    CHERRY = (
        21,
        'Cherry',
        'チェリー'
    )
    ACORN = (
        22,
        'Acorn',
        'ドングリ'
    )
    SPINY = (
        23,
        'Spiny',
        'トゲゾー'
    )


class Track(Enum):

    __slots__ = (
        'name',
        'name_ja',
        'abbr',
        'abbr_ja',
        '_nicks',
        'console'
    )

    def __new__(cls: type[Track], id: int, *_) -> Track:
        obj = object.__new__(cls)
        obj._value_ = id
        return obj

    def __init__(
        self,
        _: int,
        name: str,
        name_ja: str,
        abbr: str,
        abbr_ja: str,
        nicks: set[str],
        console: Optional[Console] = None
    ):
        self.name: str = name
        self.name_ja: str = name_ja
        self.abbr: str = abbr
        self.abbr_ja: str = abbr_ja
        self.nicks: set[str] = nicks
        self.console: Optional[Console] = console

    @property
    def nicks(self) -> set[str]:
        return self._nicks

    @nicks.setter
    def nicks(self, nicks: set[str]) -> None:
        global _ALL_TRACK_DICT
        if hasattr(self, '_nicks'):
            for nick in self._nicks:
                _ALL_TRACK_DICT.pop(nick)
        for nick in nicks:
            _ALL_TRACK_DICT[nick] = self
        self._nicks = nicks

    @property
    def id(self) -> int:
        return self.value

    @property
    def cup(self) -> Cup:
        return Cup(self.id // 4)

    @property
    def full_name(self) -> str:
        if self.console is None:
            return self.name
        return f'{self.console.abbr} {self.name}'

    @property
    def full_name_ja(self) -> str:
        if self.console is None:
            return self.name_ja
        console = self.console.abbr_ja
        if console is None:
            console = self.console.abbr
        return f'{console} {self.name_ja}'

    @staticmethod
    def from_nick(nick: str) -> Optional[Track]:
        _nick = _translate(nick)
        return _ALL_TRACK_DICT.get(_nick)

    @staticmethod
    def from_initial(initial: str) -> list[Track]:
        _initial = _translate(initial)
        return [track for track in Track if sum(map(lambda n: n.startswith(_initial), track.nicks)) > 0]

    MKS = (
        0,
        'Mario Kart Stadium',
        'マリオカートスタジアム',
        'MKS',
        'マリカス',
        {'mks', 'ﾏﾘｵｶｰﾄｽﾀｼﾞｱﾑ', 'ﾏﾘｶｽ'}
    )
    WP = (
        1,
        'Water Park',
        'ウォーターパーク',
        'WP',
        'ウォタパ',
        {'wp', 'ｳｫｰﾀﾊﾟｰｸ', 'ｦｰﾀｰﾊﾟｰｸ', 'ｳｫﾀﾊﾟ', 'ｦﾀﾊﾟ', 'ｵﾀﾊﾟ'}
    )
    SSC = (
        2,
        'Sweet Sweet Canyon',
        'スイーツキャニオン',
        'SSC',
        'スイキャニ',
        {'ssc', 'ｽｲｰﾂｷｬﾆｵﾝ', 'ｽｲｷｬﾆ'}
    )
    TR = (
        3,
        'Thwomp Ruins',
        'ドッスンいせき',
        'TR',
        'ドッスン',
        {'tr', 'ﾄﾞｯｽﾝｲｾｷ', 'ﾄﾞｯｽﾝ', 'ｲｾｷ', 'ﾄﾞｯｽﾝ遺跡', '遺跡'}
    )
    MC = (
        4,
        'Mario Circuit',
        'マリオサーキット',
        'MC',
        '新マリサ',
        {'mc', 'ﾏﾘｵｻｰｷｯﾄ', 'ﾏﾘｻ', '新ﾏﾘｻ', 'ｼﾝﾏﾘｻ'}
    )
    TH = (
        5,
        'Toad Harbor',
        'キノピオハーバー',
        'TH',
        'ハーバー',
        {'th', 'ｷﾉﾋﾟｵﾊｰﾊﾞｰ', 'ﾊｰﾊﾞｰ'}
    )
    TM = (
        6,
        'Twisted Mansion',
        'ねじれマンション',
        'TM',
        'ねじマン',
        {'tm', 'ﾈｼﾞﾚﾏﾝｼｮﾝ', 'ﾈｼﾞﾏﾝ', 'ﾈｼﾞﾚ', 'ﾈｼﾞｼｮﾝ', 'ﾈｼﾞ', 'ﾈｼﾞﾈｼﾞ', 'ﾏﾝｼｮﾝ'}
    )
    SGF = (
        7,
        'Shy Guy Falls',
        'ヘイホーこうざん',
        'SGF',
        'ヘイこう',
        {'sgf', 'ﾍｲﾎｰｺｳｻﾞﾝ', 'ﾍｲﾎｰ鉱山', 'ﾍｲｺｰ', 'ﾍｲｺｳ', 'ﾍｲ鉱'}
    )
    SA = (
        8,
        'Sunshine Airport',
        'サンシャインくうこう',
        'SA',
        'くうこう',
        {'sa', 'ｻﾝｼｬｲﾝｸｳｺｳ', '空港', 'ｸｳｺｳ', 'ｻﾝｼｬｲﾝ'}
    )
    DS = (
        9,
        'Dolphin Shoals',
        'ドルフィンみさき',
        'DS',
        'ドルみ',
        {'ds', 'ﾄﾞﾙﾌｨﾝﾐｻｷ', 'ﾄﾞﾙﾐ', 'ﾐｻｷ', 'ﾄﾞﾙﾌｨﾝ岬', '岬'}
    )
    ED = (
        10,
        'Electrodrome',
        'エレクトロドリーム',
        'Ed',
        'エレド',
        {'ed', 'ｴﾚｸﾄﾛﾄﾞﾘｰﾑ', 'ｴﾚﾄﾞ', 'ｴﾚﾄﾞﾘ'}
    )
    MW = (
        11,
        'Mount Wario',
        'ワリオスノーマウンテン',
        'MW',
        'ワリスノ',
        {'mw', 'ﾜﾘｵｽﾉｰﾏｳﾝﾃﾝ', 'ﾜﾘｽﾉ', 'ﾕｷﾔﾏ', '雪山', 'ｽﾉ', 'ﾕｷﾔﾏｳﾝﾃﾝ'}
    )
    CC = (
        12,
        'Cloudtop Cruise',
        'スカイガーデン',
        'CC',
        'スカガ',
        {'cc', 'ｽｶｲｶﾞｰﾃﾞﾝ', 'ｽｶｶﾞ'}
    )
    BDD = (
        13,
        'Bone-Dry Dunes',
        'ホネホネさばく',
        'BDD',
        'ホネさば',
        {'bdd', 'ﾎﾈﾎﾈｻﾊﾞｸ', 'ﾎﾈｻﾊﾞ', 'ﾎﾈﾎﾈ'}
    )
    BC = (
        14,
        "Bowser's Castle",
        'クッパキャッスル',
        'BC',
        'クパキャ',
        {'bc', 'ｸｯﾊﾟｷｬｯｽﾙ', 'ｸﾊﾟｷｬ', 'ｸｷｬﾊﾟ', 'ｸｯｷｬﾊﾟｯｽﾙ'}
    )
    RR = (
        15,
        'Rainbow Road',
        'レインボーロード',
        'RR',
        '新虹',
        {'rr', 'ﾚｲﾝﾎﾞｰﾛｰﾄﾞ', '新虹', 'ｼﾝﾆｼﾞ'}
    )
    DYC = (
        16,
        'Yoshi Circuit',
        'ヨッシーサーキット',
        'dYC',
        'ヨシサ',
        {'dyc', 'yc', 'ﾖｯｼｰｻｰｷｯﾄ', 'ﾖｼｻ'},
        Console.GCN
    )
    DEA = (
        17,
        'Excitebike Arena',
        'エキサイトバイク',
        'dEA',
        'エキバ',
        {'dea', 'ea', 'ｴｷｻｲﾄﾊﾞｲｸ', 'ｴｷﾊﾞ'}
    )
    DDD = (
        18,
        'Dragon Driftway',
        'ドラゴンロード',
        'dDD',
        'ドラロ',
        {'ddd', 'dd', 'ﾄﾞﾗｺﾞﾝﾛｰﾄﾞ', 'ﾄﾞﾗﾛ'}
    )
    DMC = (
        19,
        'Mute City',
        'ミュートシティ',
        'dMC',
        'ミュート',
        {'dmc', 'ﾐｭｰﾄｼﾃｨ', 'ﾐｭｰﾄ'}
    )
    DBP = (
        20,
        'Baby Park',
        'ベビィパーク',
        'dBP',
        'ベビパ',
        {'dbp', 'bp', 'ﾍﾞﾋﾞｨﾊﾟｰｸ', 'ﾍﾞﾋﾞｰﾊﾟｰｸ', 'ﾍﾞﾋﾞﾊﾟ'},
        Console.GCN
    )
    DCL = (
        21,
        'Cheese Land',
        'チーズランド',
        'dCL',
        'チーズ',
        {'dcl', 'cl', 'ﾁｰｽﾞﾗﾝﾄﾞ', 'ﾁｰｽﾞ'},
        Console.GBA
    )
    DWW = (
        22,
        'Wild Woods',
        'ネイチャーロード',
        'dWW',
        'ネイチャー',
        {'dww', 'ww', 'ﾈｲﾁｬｰﾗﾝﾄﾞ', 'ﾈｲﾁｬｰ', 'ﾅﾁｭﾚ'}
    )
    DAC = (
        23,
        'Animal Crossing',
        'どうぶつの森',
        'dAC',
        'どう森',
        {'dac', 'ac', 'ﾄﾞｳﾌﾞﾂﾉﾓﾘ', 'ﾄﾞｳﾓﾘ', 'ﾌﾞﾂﾓﾘ', 'ﾄﾞｳ森', 'ﾌﾞﾂ森', 'ﾄﾞｳﾌﾞﾂﾉ森'}
    )
    RMMM = (
        24,
        'Moo Moo Meadows',
        'モーモーカントリー',
        'rMMM',
        'モモカン',
        {'rmmm', 'mmm', 'ﾓｰﾓｰｶﾝﾄﾘｰ', 'ﾓﾓｶﾝ', 'ﾓｰﾓｰ'},
        Console.WII
    )
    RMC = (
        25,
        'Mario Circuit',
        'マリオサーキット',
        'rMC',
        'GBAマリサ',
        {'rmc', 'gba', 'ｸﾞﾊﾞ', 'gbaﾏﾘｵｻｰｷｯﾄ', 'gbaﾏﾘｻ'},
        Console.GBA
    )
    RCCB = (
        26,
        'Cheep Cheep Beach',
        'プクプクビーチ',
        'rCCB',
        'プクビ',
        {'rccb', 'ccb', 'ﾌﾟｸﾌﾟｸﾋﾞｰﾁ', 'ﾌﾟｸﾌﾟｸ', 'ﾌﾟｸﾋﾞ'},
        Console.DS
    )
    RTT = (
        27,
        "Toad's Turnpike",
        'キノピオハイウェイ',
        'rTT',
        'ハイウェイ',
        {'rtt', 'tt', 'ｷﾉﾋﾟｵﾊｲｳｪｲ', 'ﾊｲｳｪｲ'},
        Console.N64
    )
    RDDD = (
        28,
        'Dry Dry Desert',
        'カラカラさばく',
        'rDDD',
        'GCカラさば',
        {'rddd', 'ｶﾗｶﾗｻﾊﾞｸ', 'ｶﾗｻﾊﾞ', 'ｻﾊﾞｸ', 'gcｶﾗ', 'gcｶﾗｻﾊﾞ', 'gcｻﾊﾞ'},
        Console.GCN
    )
    RDP3 = (
        29,
        'Donut Plains 3',
        'ドーナツへいや3',
        'rDP3',
        'へいや',
        {'rdp3', 'rdp', 'dp3', 'ﾄﾞｰﾅﾂﾍｲﾔ', 'ﾍｲﾔ', 'ﾄﾞｰﾅﾂ平野', '平野'},
        Console.SNES
    )
    RRRY = (
        30,
        'Royal Raceway',
        'ピーチサーキット',
        'rRRy',
        'ピチサ',
        {'rrry', 'rry', 'ﾋﾟｰﾁｻｰｷｯﾄ', 'ﾋﾟﾁｻ'},
        Console.N64
    )
    RDKJ = (
        31,
        'DK Jungle',
        'DKジャングル',
        'rDKJ',
        'ジャングル',
        {'rdkj', 'dk', 'dkj', 'dkｼﾞｬﾝｸﾞﾙ', 'ｼﾞｬﾝｸﾞﾙ'},
        Console.N3DS
    )
    RWS = (
        32,
        'Wario Stadium',
        'ワリオスタジアム',
        'rWS',
        'ワリスタ',
        {'rws', 'ws', 'ﾜﾘｵｽﾀｼﾞｱﾑ', 'ﾜﾘｽﾀ'},
        Console.DS
    )
    RSL = (
        33,
        'Sherbet Land',
        'シャーベットランド',
        'rSL',
        'シャベラン',
        {'rsl', 'sl', 'ｼｬｰﾍﾞｯﾄﾗﾝﾄﾞ', 'ｼｬｰﾍﾞｯﾄ', 'ｼｬﾍﾞﾗﾝ', 'ｼｬﾍﾞ'},
        Console.GCN
    )
    RMP = (
        34,
        'Music Park',
        'ミュージックパーク',
        'rMP',
        'ミューパ',
        {'rmp', 'mp', 'ﾐｭｰｼﾞｯｸﾊﾟｰｸ', 'ﾐｭｰﾊﾟ'},
        Console.N3DS
    )
    RYV = (
        35,
        'Yoshi Valley',
        'ヨッシーバレー',
        'rYV',
        'ヨシバ',
        {'ryv', 'yv', 'ﾖｯｼｰﾊﾞﾚｰ', 'ﾖｼﾊﾞ'},
        Console.N64
    )
    RTTC = (
        36,
        'Tick-Tock Clock',
        'チクタクロック',
        'rTTC',
        'チクタク',
        {'rttc', 'ttc', 'ﾁｸﾀｸﾛｯｸ', 'ﾁｸﾀｸ'},
        Console.DS
    )
    RPPS = (
        37,
        'Piranha Planet Slide',
        'パックンスライダー',
        'rPPS',
        'パクスラ',
        {'rpps', 'pps', 'ﾊﾟｯｸﾝｽﾗｲﾀﾞｰ', 'ﾊﾟｸｽﾗ', 'ﾊﾟｯｸﾝ'},
        Console.N3DS
    )
    RGV = (
        38,
        'Grumble Volcano',
        'グラグラかざん',
        'rGV',
        'かざん',
        {'rgv', 'gv', 'ｸﾞﾗｸﾞﾗｶｻﾞﾝ', 'ｸﾞﾗｸﾞﾗ', 'ｶｻﾞﾝ'},
        Console.WII
    )
    RRRD = (
        39,
        'Rainbow Road',
        'レインボーロード',
        'rRRd',
        '64虹',
        {'rrrd', 'rrd', '64ﾚｲﾝﾎﾞｰﾛｰﾄﾞ', '64ﾆｼﾞ', '64虹', 'ﾛｸﾖﾝ'},
        Console.N64
    )
    DWGM = (
        40,
        "Wario's Gold Mine",
        'ワリオこうざん',
        'dWGM',
        'ワリこう',
        {'dwgm', 'wgm', 'ﾜﾘｵｺｳｻﾞﾝ', 'ﾜﾘｺｳ', 'ﾜﾘｵ鉱山', 'ﾜﾘ鉱'},
        Console.WII
    )
    DRR = (
        41,
        'Rainbow Road',
        'レインボーロード',
        'dRR',
        'SFC虹',
        {'drr', 'sfcﾆｼﾞ', 'sfcﾚｲﾝﾎﾞｰﾛｰﾄﾞ', 'sfc虹', 'sfc'},
        Console.SNES
    )
    DIIO = (
        42,
        'Ice Ice Outpost',
        'ツルツルツイスター',
        'dIIO',
        'ツルツル',
        {'diio', 'iio', 'ﾂﾙﾂﾙﾂｲｽﾀｰ', 'ﾂﾂﾂ', 'ﾂﾙﾂﾙ'}
    )
    DHC = (
        43,
        'Hyrule Circuit',
        'ハイラルサーキット',
        'dHC',
        'ハイラル',
        {'dhc', 'hc', 'ﾊｲﾗﾙｻｰｷｯﾄ', 'ﾊｲﾗﾙ'}
    )
    DNBC = (
        44,
        'Neo Bowser City',
        'ネオクッパシティ',
        'dNBC',
        'ネオパ',
        {'dnbc', 'nbc', 'ﾈｵｸｯﾊﾟｼﾃｨ', 'ﾈｵﾊﾟ', 'ﾈｵｸｯﾊﾟ'},
        Console.N3DS
    )
    DRIR = (
        45,
        'Ribbon Road',
        'リボンロード',
        'dRiR',
        'リボン',
        {'drir', 'rir', 'ﾘﾎﾞﾝﾛｰﾄﾞ', 'ﾘﾎﾞﾝ'},
        Console.GBA
    )
    DSBS = (
        46,
        'Super Bell Subway',
        'リンリンメトロ',
        'dSBS',
        'リンメト',
        {'dsbs', 'sbs', 'ﾘﾝﾘﾝﾒﾄﾛ', 'ﾘﾝﾒﾄ'}
    )
    DBB = (
        47,
        'Big Blue',
        'ビッグブルー',
        'dBB',
        'ビッグブルー',
        {'dbb', 'bb', 'ﾋﾞｯｸﾞﾌﾞﾙｰ'}
    )
    BPP = (
        48,
        'Paris Promenade',
        'パリプロムナード',
        'bPP',
        'パリ',
        {'bpp', 'pp', 'paris', 'ﾊﾟﾘﾌﾟﾛﾑﾅｰﾄﾞ', 'ﾊﾟﾘ'},
        Console.TOUR
    )
    BTC = (
        49,
        'Toad Circuit',
        'キノピオサーキット',
        'bTC',
        'キノサ',
        {'btc', 'tc', 'ｷﾉﾋﾟｵｻｰｷｯﾄ', 'ｷﾉｻ'},
        Console.N3DS
    )
    BCMO = (
        50,
        'Choco Mountain',
        'チョコマウンテン',
        'bCMo',
        'チョコ',
        {'bcmo', 'bcm64', 'bchm', 'cmo', 'chm', 'cm64', 'ﾁｮｺﾏｳﾝﾃﾝ', 'ﾁｮｺ', 'ﾁｮｺﾏ'},
        Console.N64
    )
    BCMA = (
        51,
        'Coconut Mall',
        'ココナッツモール',
        'bCMa',
        'ココモ',
        {'bcma', 'bcom', 'bcmw', 'cma', 'com', 'cmw', 'ｺｺﾅｯﾂﾓｰﾙ', 'ｺｺﾓ', 'ｺｺﾅｯﾂ', 'ﾅｯﾂ'},
        Console.WII
    )
    BTB = (
        52,
        'Tokyo Blur',
        'トーキョースクランブル',
        'bTB',
        'トーキョー',
        {'btb', 'tb', 'tokyo', 'ﾄｰｷｮｰｽｸﾗﾝﾌﾞﾙ', 'ｽｸﾗﾝﾌﾞﾙ', 'ﾄｰｷｮｰ', 'ﾄｳｷｮｳ', 'ﾄｰｷｮｳ', 'ﾄｳｷｮｰ', '東京'},
        Console.TOUR
    )
    BSR = (
        53,
        'Shroom Ridge',
        'キノコリッジウェイ',
        'bSR',
        'リッジ',
        {'bsr', 'sr', 'ｷﾉｺﾘｯｼﾞｳｪｲ', 'ｷﾉｺﾘｯｼﾞ', 'ﾘｯｼﾞｳｪｲ', 'ｷﾉｺﾘ', 'ｷｺﾘ', 'ﾘｯｼﾞ'},
        Console.DS
    )
    BSG = (
        54,
        'Sky Garden',
        'スカイガーデン',
        'bSG',
        'GBAスカガ',
        {'bsg', 'sg', 'gbaｽｶｲｶﾞｰﾃﾞﾝ', 'gbaｽｶ', 'ｸﾞﾊﾞｽｶ', 'ｸﾞﾊﾞｽｶｶﾞ', 'gbaｽｶｶﾞ'},
        Console.GBA
    )
    BNH = (
        55,
        'Ninja Hideaway',
        'ニンニンドージョー',
        'bNH',
        'ニンニン',
        {'bnh', 'nh', 'ﾆﾝﾆﾝﾄﾞｰｼﾞｮｰ', 'ﾆﾝｼﾞｮｰ', 'ﾆﾝﾆﾝ'}
    )
    BNYM = (
        56,
        'New York Minute',
        'ニューヨークドリーム',
        'bNYM',
        'ニューヨーク',
        {'bnym', 'nym', 'ﾆｭｰﾖｰｸﾄﾞﾘｰﾑ', 'ﾆｭｰﾖｰｸ', 'ﾆｭｰﾄﾞﾘ', 'ny'},
        Console.TOUR
    )
    BMC3 = (
        57,
        'Mario Circuit 3',
        'マリオサーキット3',
        'bMC3',
        'SFCマリサ',
        {'bmc3', 'mc3', 'ﾏﾘｵｻｰｷｯﾄ3', 'ﾏﾘｻ3', 'sfcﾏﾘｻ', 'sfcﾏﾘｵｻｰｷｯﾄ', 'sfcﾏﾘｻ3', 'sfcﾏﾘｵｻｰｷｯﾄ3'},
        Console.SNES
    )
    BKD = (
        58,
        'Kalimari Desert',
        'カラカラさばく',
        'bKD',
        '64カラさば',
        {'bkd', 'kd', '64ｶﾗｻﾊﾞ', '64ｶﾗ', '64ｻﾊﾞ'},
        Console.N64
    )
    BWP = (
        59,
        'Waluigi Pinball',
        'ワルイージピンボール',
        'bWP',
        'ワルピン',
        {'bwp', 'ﾜﾙｲｰｼﾞﾋﾟﾝﾎﾞｰﾙ', 'ﾜﾙﾋﾟﾝ', 'ﾋﾟﾝﾎﾞｰﾙ'},
        Console.DS
    )
    BSS = (
        60,
        'Sydney Sprint',
        'シドニーサンシャイン',
        'bSS',
        'シドニー',
        {'bss', 'ss', 'bsys', 'sys', 'ｼﾄﾞﾆｰｻﾝｼｬｲﾝ', 'ｼﾄﾞﾆｰ'},
        Console.TOUR
    )
    BSL = (
        61,
        'Snow Land',
        'スノーランド',
        'bSL',
        'スノラン',
        {'bsl', 'ｽﾉｰﾗﾝﾄﾞ', 'ｽﾉﾗﾝ'},
        Console.GBA
    )
    BMG = (
        62,
        'Mushroom Gorge',
        'キノコキャニオン',
        'bMG',
        'キノキャニ',
        {'bmg', 'mg', 'ｷﾉｺｷｬﾆｵﾝ', 'ｷﾉｷｬﾆ', 'ｷｬﾆｵﾝ'},
        Console.WII
    )
    BSHS = (
        63,
        'Sky-High Sundae',
        'アイスビルディング',
        'bSHS',
        'アイス',
        {'bshs', 'shs', 'ｱｲｽﾋﾞﾙﾃﾞｨﾝｸﾞ', 'ｱｲｽ'}
    )
    BLL = (
        64,
        'London Loop',
        'ロンドンアベニュー',
        'bLL',
        'ロンドン',
        {'bll', 'll', 'ﾛﾝﾄﾞﾝｱﾍﾞﾆｭｰ', 'ﾛﾝﾄﾞﾝ'},
        Console.TOUR
    )
    BBL = (
        65,
        'Boo Lake',
        'テレサレイク',
        'bBL',
        'レイク',
        {'bbl', 'bl', 'ﾃﾚｻﾚｲｸ', 'ﾚｲｸ', 'ﾃﾚｲｸ'},
        Console.GBA
    )
    BRRM = (
        66,
        'Rock Rock Mountain',
        'ロックロックマウンテン',
        'bRRM',
        'ロック',
        {'brrm', 'rrm', 'ﾛｯｸﾛｯｸﾏｳﾝﾃﾝ', 'ﾛｸﾏ', 'ﾛｯｸ', '岩山', 'ﾛｯｸﾛｯｸ'},
        Console.N3DS
    )
    BMT = (
        67,
        'Maple Treeway',
        'メイプルツリーハウス',
        'bMT',
        'メイプル',
        {'bmt', 'mt', 'ﾒｲﾌﾟﾙﾂﾘｰﾊｳｽ', 'ﾒｲﾌﾟﾙ'},
        Console.WII
    )
    BBB = (
        68,
        'Berlin Byways',
        'ベルリンシュトラーセ',
        'bBB',
        'ベルリン',
        {'bbb', 'ﾍﾞﾙﾘﾝｼｭﾄﾗｰｾ', 'ﾍﾞﾙﾘﾝ'},
        Console.TOUR
    )
    BPG = (
        69,
        'Peach Gardens',
        'ピーチガーデン',
        'bPG',
        'ピチガ',
        {'bpg', 'pg', 'ﾋﾟｰﾁｶﾞｰﾃﾞﾝ', 'ﾋﾟﾁｶﾞ', 'ｶﾞｰﾃﾞﾝ'},
        Console.DS
    )
    BMM = (
        70,
        'Merry Mountain',
        'メリーメリーマウンテン',
        'bMM',
        'メリー',
        {'bmm', 'mm', 'ﾒﾘｰﾒﾘｰﾏｳﾝﾃﾝ', 'ﾒﾘﾏ', 'ﾒﾘｰﾒﾘｰ', 'ﾒﾘｰ', 'ﾒﾘﾔﾏ', 'ﾒﾘ山'}
    )
    BRR7 = (
        71,
        'Rainbow Road',
        'レインボーロード',
        'bRR7',
        '7虹',
        {'brr7', 'rr7', '3dsﾆｼﾞ', '3ds虹', '7ﾆｼﾞ', '7虹'},
        Console.N3DS
    )
    BAD = (
        72,
        'Amsterdam Drift',
        'アムステルダムブルーム',
        'bAD',
        'アムステルダム',
        {'bad', 'ad', 'amsterdam', 'ｱﾑｽﾃﾙﾀﾞﾑﾌﾞﾙｰﾑ', 'ｱﾑｽﾃﾙﾀﾞﾑ', 'ｱﾑｽ', 'ﾌﾞﾙｰﾑ'},
        Console.TOUR
    )
    BRP = (
        73,
        'Riverside Park',
        'リバーサイドパーク',
        'bRP',
        'リバパ',
        {'brp', 'rp', 'ﾘﾊﾞｰｻｲﾄﾞﾊﾟｰｸ', 'ﾘﾊﾞｰｻｲﾄﾞ', 'ﾘﾊﾞﾊﾟ'},
        Console.GBA
    )
    BDKS = (
        74,
        'DK Summit',
        'DKスノーボードクロス',
        'bDKS',
        'スノボ',
        {'bdks', 'dks', 'summit', 'dkｽﾉｰﾎﾞｰﾄﾞｸﾛｽ', 'ｽﾉｰﾎﾞｰﾄﾞｸﾛｽ', 'ｽﾉﾎﾞｸﾛｽ', 'ｽﾉﾎﾞ'},
        Console.WII
    )
    BYI = (
        75,
        'Yoshi\'s Island',
        'ヨッシーアイランド',
        'bYI',
        'ヨシアイ',
        {'byi', 'yi', 'ﾖｯｼｰｱｲﾗﾝﾄﾞ', 'ﾖｼｱｲ'}
    )
    BBR = (
        76,
        'Bangkok Rush',
        'バンコクラッシュ',
        'bBR',
        'バンコク',
        {'bbr', 'br', 'bangkok', 'ﾊﾞﾝｺｸﾗｯｼｭ', 'ﾊﾞﾝｺｸ'},
        Console.TOUR
    )
    BMC = (
        77,
        'Mario Circuit',
        'マリオサーキット',
        'bMC',
        'DSマリサ',
        {'bmc', 'dsﾏﾘｵｻｰｷｯﾄ', 'dsﾏﾘｻ'},
        Console.DS
    )
    BWS = (
        78,
        'Waluigi Stadium',
        'ワルイージスタジアム',
        'bWS',
        'ワルスタ',
        {'bws', 'ﾜﾙｲｰｼﾞｽﾀｼﾞｱﾑ', 'ﾜﾙｽﾀ'},
        Console.GCN
    )
    BSSY = (
        79,
        'Singapore Speedway',
        'シンガポールスプラッシュ',
        'bSSy',
        'シンガポール',
        {'bssy', 'ssy', 'bsis', 'sis', 'singapore', 'ｼﾝｶﾞﾎﾟｰﾙｽﾌﾟﾗｯｼｭ', 'ｼﾝｶﾞﾎﾟｰﾙ'},
        Console.TOUR
    )
    BATD = (
        80,
        'Athens Dash',
        'アテネポリス',
        'bAtD',
        'アテネ',
        {'batd', 'atd', 'bada', 'ada', 'athens', 'ｱﾃﾈﾎﾟﾘｽ', 'ｱﾃﾈ'},
        Console.TOUR
    )
    BDC = (
        81,
        'Daisy Cruiser',
        'デイジークルーザー',
        'bDC',
        'デイクル',
        {'bdc', 'dc', 'ﾃﾞｲｼﾞｰｸﾙｰｻﾞｰ', 'ﾃﾞｲｸﾙ'},
        Console.GCN
    )
    BMH = (
        82,
        'Moonview Highway',
        'ムーンリッジ&ハイウェイ',
        'bMH',
        'ムーンリッジ',
        {'bmh', 'mh', 'ﾑｰﾝﾘｯｼﾞ', 'ﾑﾝﾊｲ', 'ﾑｰﾝﾊｲ'},
        Console.WII
    )
    BSPS = (
        83,
        'Squeaky Clean Sprint',
        'シャボンロード',
        'bSCS',
        'シャボン',
        {'bscs', 'scs', 'ｼｬﾎﾞﾝﾛｰﾄﾞ', 'ｼｬﾎﾞﾝ', 'ｼｬﾎﾞﾛ'}
    )
    BLAL = (
        84,
        'Los Angeles Laps',
        'ロサンゼルスコースト',
        'bLAL',
        'ロサンゼルス',
        {'blal', 'lal', 'losangeles', 'los', 'ﾛｻﾝｾﾞﾙｽｺｰｽﾄ', 'ﾛｻﾝｾﾞﾙｽ', 'ﾛｽ'},
        Console.TOUR
    )
    BSW = (
        85,
        'Sunset Wilds',
        'サンセットこうや',
        'bSW',
        'サンセット',
        {'bsw', 'sw', 'ｻﾝｾｯﾄｺｳﾔ', 'ｻﾝｾｯﾄ', 'ｺｳﾔ', 'ｻﾝｾ'},
        Console.GBA
    )
    BKC = (
        86,
        'Koopa Cape',
        'ノコノコみさき',
        'bKC',
        'ノコみ',
        {'bkc', 'kc', 'ﾉｺﾉｺﾐｻｷ', 'ﾉｺﾉｺ', 'ﾉｺﾐｻ', 'ﾉｺﾐ'},
        Console.WII
    )
    BVV = (
        87,
        'Vancouver Velocity',
        'バンクーバーバレー',
        'bVV',
        'バンクーバー',
        {'bvv', 'vv', 'vancouver', 'ﾊﾞﾝｸｰﾊﾞｰﾊﾞﾚｰ', 'ﾊﾞﾝｸｰﾊﾞｰ'},
        Console.TOUR
    )
    BRA = (
        88,
        'Rome Avanti',
        'ローマアバンティ',
        'bRA',
        'ローマ',
        {'bra', 'ra', 'rome', 'ﾛｰﾏｱﾊﾞﾝﾃｨ', 'ﾛｰﾏ'},
        Console.TOUR
    )
    BDKM = (
        89,
        'DK Mountain',
        'DKマウンテン',
        'bDKM',
        'DKマウンテン',
        {'bdkm', 'dkm', 'dkﾏｳﾝﾃﾝ', 'dkﾔﾏ', 'dk山'},
        Console.GCN
    )
    BDCI = (
        90,
        'Daisy Circuit',
        'デイジーサーキット',
        'bDCi',
        'デイサ',
        {'bdci', 'dci', 'ﾃﾞｲｼﾞｰｻｰｷｯﾄ', 'ﾃﾞｲｻ'},
        Console.WII
    )
    BPPC = (
        91,
        'Piranha Plant Cove',
        'パックンしんでん',
        'bPPC',
        'しんでん',
        {'bppc', 'ppc', 'ﾊﾟｯｸﾝｼﾝﾃﾞﾝ', 'ﾊﾟｸｼﾝ', 'ｼﾝﾃﾞﾝ'}
    )
    BMD = (
        92,
        'Madrid Drive',
        'マドリードグランデ',
        'bMD',
        'マドリード',
        {'bmd', 'md', 'madrid', 'ﾏﾄﾞﾘｰﾄﾞｸﾞﾗﾝﾃﾞ', 'ﾏﾄﾞﾘｰﾄﾞ'},
        Console.TOUR
    )
    BRIW = (
        93,
        'Rosalina\'s Ice World',
        'ロゼッタプラネット',
        'bRIW',
        'ロゼプラ',
        {'briw', 'riw', 'ﾛｾﾞｯﾀﾌﾟﾗﾈｯﾄ', 'ﾛｾﾞﾌﾟﾗ'},
        Console.N3DS
    )
    BBC3 = (
        94,
        'Bowser\'s Castle 3',
        'クッパじょう3',
        'bBC3',
        'クッパじょう',
        {'bbc3', 'bbc', 'bc3', 'ｸｯﾊﾟｼﾞｮｳ3', 'ｸｯﾊﾟｼﾞｮｳ', 'ｸｯﾊﾟ城'},
        Console.SNES
    )
    BRR = (
        95,
        'Rainbow Road',
        'レインボーロード',
        'bRR',
        'Wii虹',
        {'brr', 'brrw', 'rrw', 'wiiﾆｼﾞ', 'wiiﾚｲﾝﾎﾞｰﾛｰﾄﾞ', 'wii虹', 'wiiﾆｼﾞ', 'ｳｨｰﾆｼﾞ'},
        Console.WII
    )
