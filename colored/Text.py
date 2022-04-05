import math
import random
import sys
from time import sleep as wait

from colored import Text
from colored import fg, bg, attr, style, stylize


class Color():
    black = fg(0) + ""
    red = fg(1) + ""
    green = fg(2) + ""
    yellow = fg(3) + ""
    blue = fg(4) + ""
    magenta = fg(5) + ""
    cyan = fg(6) + ""
    light_gray = fg(7) + ""
    dark_gray = fg(8) + ""
    light_red = fg(9) + ""
    light_green = fg(10) + ""
    light_yellow = fg(11) + ""
    light_blue = fg(12) + ""
    light_magenta = fg(13) + ""
    light_cyan = fg(14) + ""
    white = fg(15) + ""
    grey_0 = fg(16) + ""
    navy_blue = fg(17) + ""
    dark_blue = fg(18) + ""
    blue_3a = fg(19) + ""
    blue_3b = fg(20) + ""
    blue_1 = fg(21) + ""
    dark_green = fg(22) + ""
    deep_sky_blue_4a = fg(23) + ""
    deep_sky_blue_4b = fg(24) + ""
    deep_sky_blue_4c = fg(25) + ""
    dodger_blue_3 = fg(26) + ""
    dodger_blue_2 = fg(27) + ""
    green_4 = fg(28) + ""
    spring_green_4 = fg(29) + ""
    turquoise_4 = fg(30) + ""
    deep_sky_blue_3a = fg(31) + ""
    deep_sky_blue_3b = fg(32) + ""
    dodger_blue_1 = fg(33) + ""
    green_3a = fg(34) + ""
    spring_green_3a = fg(35) + ""
    dark_cyan = fg(36) + ""
    light_sea_green = fg(37) + ""
    deep_sky_blue_2 = fg(38) + ""
    deep_sky_blue_1 = fg(39) + ""
    green_3b = fg(40) + ""
    spring_green_3b = fg(41) + ""
    spring_green_2a = fg(42) + ""
    cyan_3 = fg(43) + ""
    dark_turquoise = fg(44) + ""
    turquoise_2 = fg(45) + ""
    green_1 = fg(46) + ""
    spring_green_2b = fg(47) + ""
    spring_green_1 = fg(48) + ""
    medium_spring_green = fg(49) + ""
    cyan_2 = fg(50) + ""
    cyan_1 = fg(51) + ""
    dark_red_1 = fg(52) + ""
    deep_pink_4a = fg(53) + ""
    purple_4a = fg(54) + ""
    purple_4b = fg(55) + ""
    purple_3 = fg(56) + ""
    blue_violet = fg(57) + ""
    orange_4a = fg(58) + ""
    grey_37 = fg(59) + ""
    medium_purple_4 = fg(60) + ""
    slate_blue_3a = fg(61) + ""
    slate_blue_3b = fg(62) + ""
    royal_blue_1 = fg(63) + ""
    chartreuse_4 = fg(64) + ""
    dark_sea_green_4a = fg(65) + ""
    pale_turquoise_4 = fg(66) + ""
    steel_blue = fg(67) + ""
    steel_blue_3 = fg(68) + ""
    cornflower_blue = fg(69) + ""
    chartreuse_3a = fg(70) + ""
    dark_sea_green_4b = fg(71) + ""
    cadet_blue_2 = fg(72) + ""
    cadet_blue_1 = fg(73) + ""
    sky_blue_3 = fg(74) + ""
    steel_blue_1a = fg(75) + ""
    chartreuse_3b = fg(76) + ""
    pale_green_3a = fg(77) + ""
    sea_green_3 = fg(78) + ""
    aquamarine_3 = fg(79) + ""
    medium_turquoise = fg(80) + ""
    steel_blue_1b = fg(81) + ""
    chartreuse_2a = fg(82) + ""
    sea_green_2 = fg(83) + ""
    sea_green_1a = fg(84) + ""
    sea_green_1b = fg(85) + ""
    aquamarine_1a = fg(86) + ""
    dark_slate_gray_2 = fg(87) + ""
    dark_red_2 = fg(88) + ""
    deep_pink_4b = fg(89) + ""
    dark_magenta_1 = fg(90) + ""
    dark_magenta_2 = fg(91) + ""
    dark_violet_1a = fg(92) + ""
    purple_1a = fg(93) + ""
    orange_4b = fg(94) + ""
    light_pink_4 = fg(95) + ""
    plum_4 = fg(96) + ""
    medium_purple_3a = fg(97) + ""
    medium_purple_3b = fg(98) + ""
    slate_blue_1 = fg(99) + ""
    yellow_4a = fg(100) + ""
    wheat_4 = fg(101) + ""
    grey_53 = fg(102) + ""
    light_slate_grey = fg(103) + ""
    medium_purple = fg(104) + ""
    light_slate_blue = fg(105) + ""
    yellow_4b = fg(106) + ""
    dark_olive_green_3a = fg(107) + ""
    dark_green_sea = fg(108) + ""
    light_sky_blue_3a = fg(109) + ""
    light_sky_blue_3b = fg(110) + ""
    sky_blue_2 = fg(111) + ""
    chartreuse_2b = fg(112) + ""
    dark_olive_green_3b = fg(113) + ""
    pale_green_3b = fg(114) + ""
    dark_sea_green_3a = fg(115) + ""
    dark_slate_gray_3 = fg(116) + ""
    sky_blue_1 = fg(117) + ""
    chartreuse_1 = fg(118) + ""
    light_green_2 = fg(119) + ""
    light_green_3 = fg(120) + ""
    pale_green_1a = fg(121) + ""
    aquamarine_1b = fg(122) + ""
    dark_slate_gray_1 = fg(123) + ""
    red_3a = fg(124) + ""
    deep_pink_4c = fg(125) + ""
    medium_violet_red = fg(126) + ""
    magenta_3a = fg(127) + ""
    dark_violet_1b = fg(128) + ""
    purple_1b = fg(129) + ""
    dark_orange_3a = fg(130) + ""
    indian_red_1a = fg(131) + ""
    hot_pink_3a = fg(132) + ""
    medium_orchid_3 = fg(133) + ""
    medium_orchid = fg(134) + ""
    medium_purple_2a = fg(135) + ""
    dark_goldenrod = fg(136) + ""
    light_salmon_3a = fg(137) + ""
    rosy_brown = fg(138) + ""
    grey_63 = fg(139) + ""
    medium_purple_2b = fg(140) + ""
    medium_purple_1 = fg(141) + ""
    gold_3a = fg(142) + ""
    dark_khaki = fg(143) + ""
    navajo_white_3 = fg(144) + ""
    grey_69 = fg(145) + ""
    light_steel_blue_3 = fg(146) + ""
    light_steel_blue = fg(147) + ""
    yellow_3a = fg(148) + ""
    dark_olive_green_3 = fg(149) + ""
    dark_sea_green_3b = fg(150) + ""
    dark_sea_green_2 = fg(151) + ""
    light_cyan_3 = fg(152) + ""
    light_sky_blue_1 = fg(153) + ""
    green_yellow = fg(154) + ""
    dark_olive_green_2 = fg(155) + ""
    pale_green_1b = fg(156) + ""
    dark_sea_green_5b = fg(157) + ""
    dark_sea_green_5a = fg(158) + ""
    pale_turquoise_1 = fg(159) + ""
    red_3b = fg(160) + ""
    deep_pink_3a = fg(161) + ""
    deep_pink_3b = fg(162) + ""
    magenta_3b = fg(163) + ""
    magenta_3c = fg(164) + ""
    magenta_2a = fg(165) + ""
    dark_orange_3b = fg(166) + ""
    indian_red_1b = fg(167) + ""
    hot_pink_3b = fg(168) + ""
    hot_pink_2 = fg(169) + ""
    orchid = fg(170) + ""
    medium_orchid_1a = fg(171) + ""
    orange_3 = fg(172) + ""
    light_salmon_3b = fg(173) + ""
    light_pink_3 = fg(174) + ""
    pink_3 = fg(175) + ""
    plum_3 = fg(176) + ""
    violet = fg(177) + ""
    gold_3b = fg(178) + ""
    light_goldenrod_3 = fg(179) + ""
    tan = fg(180) + ""
    misty_rose_3 = fg(181) + ""
    thistle_3 = fg(182) + ""
    plum_2 = fg(183) + ""
    yellow_3b = fg(184) + ""
    khaki_3 = fg(185) + ""
    light_goldenrod_2a = fg(186) + ""
    light_yellow_3 = fg(187) + ""
    grey_84 = fg(188) + ""
    light_steel_blue_1 = fg(189) + ""
    yellow_2 = fg(190) + ""
    dark_olive_green_1a = fg(191) + ""
    dark_olive_green_1b = fg(192) + ""
    dark_sea_green_1 = fg(193) + ""
    honeydew_2 = fg(194) + ""
    light_cyan_1 = fg(195) + ""
    red_1 = fg(196) + ""
    deep_pink_2 = fg(197) + ""
    deep_pink_1a = fg(198) + ""
    deep_pink_1b = fg(199) + ""
    magenta_2b = fg(200) + ""
    magenta_1 = fg(201) + ""
    orange_red_1 = fg(202) + ""
    indian_red_1c = fg(203) + ""
    indian_red_1d = fg(204) + ""
    hot_pink_1a = fg(205) + ""
    hot_pink_1b = fg(206) + ""
    medium_orchid_1b = fg(207) + ""
    dark_orange = fg(208) + ""
    salmon_1 = fg(209) + ""
    light_coral = fg(210) + ""
    pale_violet_red_1 = fg(211) + ""
    orchid_2 = fg(212) + ""
    orchid_1 = fg(213) + ""
    orange_1 = fg(214) + ""
    sandy_brown = fg(215) + ""
    light_salmon_1 = fg(216) + ""
    light_pink_1 = fg(217) + ""
    pink_1 = fg(218) + ""
    plum_1 = fg(219) + ""
    gold_1 = fg(220) + ""
    light_goldenrod_2b = fg(221) + ""
    light_goldenrod_2c = fg(222) + ""
    navajo_white_1 = fg(223) + ""
    misty_rose1 = fg(224) + ""
    thistle_1 = fg(225) + ""
    yellow_1 = fg(226) + ""
    light_goldenrod_1 = fg(227) + ""
    khaki_1 = fg(228) + ""
    wheat_1 = fg(229) + ""
    cornsilk_1 = fg(230) + ""
    grey_100 = fg(231) + ""
    grey_3 = fg(232) + ""
    grey_7 = fg(233) + ""
    grey_11 = fg(234) + ""
    grey_15 = fg(235) + ""
    grey_19 = fg(236) + ""
    grey_23 = fg(237) + ""
    grey_27 = fg(238) + ""
    grey_30 = fg(239) + ""
    grey_35 = fg(240) + ""
    grey_39 = fg(241) + ""
    grey_42 = fg(242) + ""
    grey_46 = fg(243) + ""
    grey_50 = fg(244) + ""
    grey_54 = fg(245) + ""
    grey_58 = fg(246) + ""
    grey_62 = fg(247) + ""
    grey_66 = fg(248) + ""
    grey_70 = fg(249) + ""
    grey_74 = fg(250) + ""
    grey_78 = fg(251) + ""
    grey_82 = fg(252) + ""
    grey_85 = fg(253) + ""
    grey_89 = fg(254) + ""
    grey_93 = fg(255) + ""

    class number():
        n0 = fg(0)
        n1 = fg(1)
        n2 = fg(2)
        n3 = fg(3)
        n4 = fg(4)
        n5 = fg(5)
        n6 = fg(6)
        n7 = fg(7)
        n8 = fg(8)
        n9 = fg(9)
        n10 = fg(10)
        n11 = fg(11)
        n12 = fg(12)
        n13 = fg(13)
        n14 = fg(14)
        n15 = fg(15)
        n16 = fg(16)
        n17 = fg(17)
        n18 = fg(18)
        n19 = fg(19)
        n20 = fg(20)
        n21 = fg(21)
        n22 = fg(22)
        n23 = fg(23)
        n24 = fg(24)
        n25 = fg(25)
        n26 = fg(26)
        n27 = fg(27)
        n28 = fg(28)
        n29 = fg(29)
        n30 = fg(30)
        n31 = fg(31)
        n32 = fg(32)
        n33 = fg(33)
        n34 = fg(34)
        n35 = fg(35)
        n36 = fg(36)
        n37 = fg(37)
        n38 = fg(38)
        n39 = fg(39)
        n40 = fg(40)
        n41 = fg(41)
        n42 = fg(42)
        n43 = fg(43)
        n44 = fg(44)
        n45 = fg(45)
        n46 = fg(46)
        n47 = fg(47)
        n48 = fg(48)
        n49 = fg(49)
        n50 = fg(50)
        n51 = fg(51)
        n52 = fg(52)
        n53 = fg(53)
        n54 = fg(54)
        n55 = fg(55)
        n56 = fg(56)
        n57 = fg(57)
        n58 = fg(58)
        n59 = fg(59)
        n60 = fg(60)
        n61 = fg(61)
        n62 = fg(62)
        n63 = fg(63)
        n64 = fg(64)
        n65 = fg(65)
        n66 = fg(66)
        n67 = fg(67)
        n68 = fg(68)
        n69 = fg(69)
        n70 = fg(70)
        n71 = fg(71)
        n72 = fg(72)
        n73 = fg(73)
        n74 = fg(74)
        n75 = fg(75)
        n76 = fg(76)
        n77 = fg(77)
        n78 = fg(78)
        n79 = fg(79)
        n80 = fg(80)
        n81 = fg(81)
        n82 = fg(82)
        n83 = fg(83)
        n84 = fg(84)
        n85 = fg(85)
        n86 = fg(86)
        n87 = fg(87)
        n88 = fg(88)
        n89 = fg(89)
        n90 = fg(90)
        n91 = fg(91)
        n92 = fg(92)
        n93 = fg(93)
        n94 = fg(94)
        n95 = fg(95)
        n96 = fg(96)
        n97 = fg(97)
        n98 = fg(98)
        n99 = fg(99)
        n100 = fg(100)
        n101 = fg(101)
        n102 = fg(102)
        n103 = fg(103)
        n104 = fg(104)
        n105 = fg(105)
        n106 = fg(106)
        n107 = fg(107)
        n108 = fg(108)
        n109 = fg(109)
        n110 = fg(110)
        n111 = fg(111)
        n112 = fg(112)
        n113 = fg(113)
        n114 = fg(114)
        n115 = fg(115)
        n116 = fg(116)
        n117 = fg(117)
        n118 = fg(118)
        n119 = fg(119)
        n120 = fg(120)
        n121 = fg(121)
        n122 = fg(122)
        n123 = fg(123)
        n124 = fg(124)
        n125 = fg(125)
        n126 = fg(126)
        n127 = fg(127)
        n128 = fg(128)
        n129 = fg(129)
        n130 = fg(130)
        n131 = fg(131)
        n132 = fg(132)
        n133 = fg(133)
        n134 = fg(134)
        n135 = fg(135)
        n136 = fg(136)
        n137 = fg(137)
        n138 = fg(138)
        n139 = fg(139)
        n140 = fg(140)
        n141 = fg(141)
        n142 = fg(142)
        n143 = fg(143)
        n144 = fg(144)
        n145 = fg(145)
        n146 = fg(146)
        n147 = fg(147)
        n148 = fg(148)
        n149 = fg(149)
        n150 = fg(150)
        n151 = fg(151)
        n152 = fg(152)
        n153 = fg(153)
        n154 = fg(154)
        n155 = fg(155)
        n156 = fg(156)
        n157 = fg(157)
        n158 = fg(158)
        n159 = fg(159)
        n160 = fg(160)
        n161 = fg(161)
        n162 = fg(162)
        n163 = fg(163)
        n164 = fg(164)
        n165 = fg(165)
        n166 = fg(166)
        n167 = fg(167)
        n168 = fg(168)
        n169 = fg(169)
        n170 = fg(170)
        n171 = fg(171)
        n172 = fg(172)
        n173 = fg(173)
        n174 = fg(174)
        n175 = fg(175)
        n176 = fg(176)
        n177 = fg(177)
        n178 = fg(178)
        n179 = fg(179)
        n180 = fg(180)
        n181 = fg(181)
        n182 = fg(182)
        n183 = fg(183)
        n184 = fg(184)
        n185 = fg(185)
        n186 = fg(186)
        n187 = fg(187)
        n188 = fg(188)
        n189 = fg(189)
        n190 = fg(190)
        n191 = fg(191)
        n192 = fg(192)
        n193 = fg(193)
        n194 = fg(194)
        n195 = fg(195)
        n196 = fg(196)
        n197 = fg(197)
        n198 = fg(198)
        n199 = fg(199)
        n200 = fg(200)
        n201 = fg(201)
        n202 = fg(202)
        n203 = fg(203)
        n204 = fg(204)
        n205 = fg(205)
        n206 = fg(206)
        n207 = fg(207)
        n208 = fg(208)
        n209 = fg(209)
        n210 = fg(210)
        n211 = fg(211)
        n212 = fg(212)
        n213 = fg(213)
        n214 = fg(214)
        n215 = fg(215)
        n216 = fg(216)
        n217 = fg(217)
        n218 = fg(218)
        n219 = fg(219)
        n220 = fg(220)
        n221 = fg(221)
        n222 = fg(222)
        n223 = fg(223)
        n224 = fg(224)
        n225 = fg(225)
        n226 = fg(226)
        n227 = fg(227)
        n228 = fg(228)
        n229 = fg(229)
        n230 = fg(230)
        n231 = fg(231)
        n232 = fg(232)
        n233 = fg(233)
        n234 = fg(234)
        n235 = fg(235)
        n236 = fg(236)
        n237 = fg(237)
        n238 = fg(238)
        n239 = fg(239)
        n240 = fg(240)
        n241 = fg(241)
        n242 = fg(242)
        n243 = fg(243)
        n244 = fg(244)
        n245 = fg(245)
        n246 = fg(246)
        n247 = fg(247)
        n248 = fg(248)
        n249 = fg(249)
        n250 = fg(250)
        n251 = fg(251)
        n252 = fg(252)
        n253 = fg(253)
        n254 = fg(254)
        n255 = fg(255)

    def HEX(hex):
        str(hex)
        fg(hex)


class Style():
    Bold = style.BOLD + ""
    Dim = style.DIM + ""
    UnderLined = style.UNDERLINED + ""
    Blink = style.BLINK + ""
    Reverse = style.REVERSE + ""
    Hidden = style.HIDDEN + ""
    Reset = style.RESET + ""
    Res_Bold = style.RES_BOLD + ""
    Res_Dim = style.RES_DIM + ""
    Res_UnderLine = style.RES_UNDERLINED + ""
    Res_Blink = style.RES_BLINK + ""
    Res_Reverse = style.RES_REVERSE + ""
    Res_Hidden = style.RES_HIDDEN + ""


class Short():
    Error = style.RESET + style.BOLD + fg(9)
    Question = style.RESET + fg('#19c2b9')
    Message = style.RESET + fg(23)
    Options = style.RESET + fg('#27f29d')
    Success = style.RESET + fg(119)
    SuccessGold = style.RESET + style.BOLD + fg(220)
    Admin = style.RESET + fg('#ec71f5')
    AdminInput = style.RESET + fg('#d73ae8')
    Input = style.RESET + Style.UnderLined + Style.Bold + fg('#6e89f5')
    Error_rest = style.RESET + fg('#87b7ff')
    Command = style.RESET + Style.UnderLined + Style.Bold + fg('#b387ff')
    Message2 = style.RESET + fg(79)
    Lose = style.RESET + fg(9)
    Comment = style.RESET + fg('#BDBDBD') + "\t"
    End = style.RESET + fg(28)
    VarOrNum = style.RESET + fg('#008f5f')


class Animation():  # https://raw.githubusercontent.com/sindresorhus/cli-spinners/master/spinners.json

    def LoadAnimCricle(string="", wait_time=0.25, step=False, total_wait_time=5):
        if wait_time > total_wait_time:
            raise ValueError("wait_time has to be smaller (more than by 4) than total_wait_time")
        if step == False:
            for i in range(round(total_wait_time / (wait_time * 4))):
                sys.stdout.write('\r' + string + ' |')
                wait(wait_time)
                sys.stdout.write('\r' + string + ' /')
                wait(wait_time)
                sys.stdout.write('\r' + string + ' —')
                wait(wait_time)
                sys.stdout.write('\r' + string + ' \\')
                wait(wait_time)
                sys.stdout.write('\r' + string + ' |')
        else:
            sys.stdout.write('\r' + string + ' |')
            wait(wait_time)
            sys.stdout.write('\r' + string + ' /')
            wait(wait_time)
            sys.stdout.write('\r' + string + ' —')
            wait(wait_time)
            sys.stdout.write('\r' + string + ' \\')
            wait(wait_time)
            sys.stdout.write('\r' + string + ' |')

    def LoadAnimDots(string="", wait_time=0.5, step=False, total_wait_time=3):
        if wait_time > total_wait_time:
            raise ValueError("wait_time has to be smaller (more than by 4) than total_wait_time")

        if step == False:
            for i in range(round(total_wait_time / (wait_time * 4))):
                sys.stdout.write('\r' + string + '')
                wait(wait_time)
                sys.stdout.write('\r' + string + '.')
                wait(wait_time)
                sys.stdout.write('\r' + string + '..')
                wait(wait_time)
                sys.stdout.write('\r' + string + '...')
                wait(wait_time)
        else:

            sys.stdout.write('\r' + string + '.')
            wait(wait_time)
            sys.stdout.write('\r' + string + '..')
            wait(wait_time)
            sys.stdout.write('\r' + string + '...')
            wait(wait_time)

    def LoadAnimUpperAndLower(string, wait_time=0.5, selected_char_color=Text.Color.black,
                              unslected_chars_color=Text.Color.black):

        str_list = [char for char in string]
        str_list = [str_list.lower() for str_list in str_list]

        for i, char in enumerate(str_list):
            counter = 0

            if char.isalpha():

                # if i > 0:
                str_list = [unslected_chars_color + str_list.lower() for str_list in str_list]
                str_list[i] = str(selected_char_color + str(str_list[i]).upper() + Text.Style.Reset)
                str_comb = ""
                for value1 in str_list:
                    str_comb = str_comb + value1
                sys.stdout.write('\r' + str_comb)
                wait(wait_time)
                counter = counter + 1

    def UpperAndLowerbackAndForth(string, wait_time=0.5):
        str_list = [char for char in string]
        str_list = [str_list.lower() for str_list in str_list]
        for i, char in enumerate(str_list):
            counter = 0
            if char.isalpha():
                if i > 0:
                    str_list = [str_list.lower() for str_list in str_list]
                str_list[i] = str(str_list[i]).upper()
                str_comb = ""
                for value1 in str_list:
                    str_comb = str_comb + value1
                sys.stdout.write('\r' + str_comb)
                wait(wait_time)
        str_list = [str_list.lower() for str_list in str_list]
        for ii, char in enumerate(str_list):
            counter = 0
            if char.isalpha():
                if i > 0:
                    str_list = [str_list.lower() for str_list in str_list]
                str_list[i - ii] = str(str_list[i - ii]).upper()
                str_comb = ""
                for value1 in str_list:
                    str_comb = str_comb + value1
                sys.stdout.write('\r' + str_comb)
                wait(wait_time)

    def LoadAnimProgressbar1(string, wait_time=5):
        done = "█"
        appending = "▒"
        precent = 0

        status = [appending, appending, appending, appending, appending, appending, appending, appending, appending,
                  appending]
        print(string + "\n", end='')
        for i in range(10):

            status[i] = done
            precent = i * 10 + 10

            comb_str = ""
            for char in status:
                comb_str = comb_str + char
            sys.stdout.write("\r" + str(comb_str) + " " + str(precent) + "%")
            wait(wait_time / 10)
        print("\n")

    def LoadAnimProgressbar2(string, wait_time=5, appending_color=Text.Color.red, complete_color=Text.Color.green_4,
                             length=10):
        length = length + 1
        done = complete_color + Text.Style.Bold + "—"
        appending = appending_color + Text.Style.Bold + "—"
        current_proccesing = "╸"
        precent = 0

        status = []
        for i in range(length):
            status.append(appending)
        print(Text.Style.Reset + " " * (round((length) / 2) + 7 - len(string)) + string + "\n", end='')
        for i in range(length):

            status[i] = current_proccesing

            if i > 0 and precent < 100:
                precent = round(100 * i / length + 10, 1)
            if precent > 100:
                precent = 100.0

            comb_str = ""
            for char in status:
                comb_str = comb_str + char
            sys.stdout.write("\r" + str(comb_str) + " " + str(precent) + "%")
            wait(wait_time / length)
            if i > 0:
                status[i] = done
            if i == 1:
                status[i - 1] = done
                status[i] = done
        if precent < 100:
            precent = 100
            sys.stdout.write("\r" + str(comb_str) + " " + str(precent) + "%")
        print("\n")

    def LoadingAnim(string="", wait_time=0.21, colors=[Text.Color.green_4], random_colors=False, total_wait_time=3,
                    step=False):
        char_array = ["⠟", "⠯", "⠷", "⠾", "⠽", "⠻"]
        c = 0
        if wait_time > total_wait_time:
            raise ValueError("wait_time has to be smaller (more than by 4) than total_wait_time")
        if step == False:
            for i in range(round(total_wait_time / (wait_time * 4))):
                for i in range(len(char_array)):
                    wait(wait_time)
                    if random_colors == True:
                        sys.stdout.write("\r" + random.choice(colors) + char_array[i] + " " + Text.Style.Reset + string)
                    else:
                        sys.stdout.write("\r" + colors[c] + char_array[i] + " " + Text.Style.Reset + string)
                        if c == len(colors) - 1:
                            c = 0
                        else:
                            c = c + 1
        else:
            for i in range(len(char_array)):
                wait(wait_time)
                if random_colors == True:
                    sys.stdout.write(
                        "\r" + random.choice(colors) + char_array[i] + " " + Text.Style.Reset + string)
                else:
                    sys.stdout.write("\r" + colors[c] + char_array[i] + " " + Text.Style.Reset + string)
                    if c == len(colors) - 1:
                        c = 0
                    else:
                        c = c + 1

