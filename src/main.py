#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import Stage


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Story structure
#   4. Plot
#   5. Scenes
#   6. Conte
#   7. Layout
#   8. Draft
#
################################################################

# Constant
TITLE = "涙の意味は"
COPY = "その涙の意味を、考えたことはありますか？"
ONELINE = "約8000字のヒューマンドラマ。家族を捨てた父親似の自分の顔が嫌いな小学生の女子は、ある日、母の彼氏らしき男性を目撃する"
OUTLINE = "小学生の結美は幼い頃に出て行った父譲りの自分の太眉が大嫌いだった。ある日、母親と喫茶店で会っている知らない男性を目撃する。"
THEME = "テーマ"
GENRE = "ヒューマンドラマ"
TARGET = "ターゲット（年代）"
SIZE = "規定サイズ"
CONTEST_INFO = "妄想コンテスト「お父さん」応募作"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (11, 10, 2019)
MAJOR, MINOR, MICRO = 2, 1, 0


# Episodes
def ep1(w: World):
    return w.episode('1',
            Stage.sc_1(w),
            Stage.sc_2(w),
            )

def ep2(w: World):
    return w.episode("2",
            Stage.in_october(w),
            Stage.sc_3(w),
            )

def ep3(w: World):
    return w.episode("3",
            Stage.sc_4(w),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep1(w),
            ep2(w),
            ep3(w),
            w.symbol("（了）"),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

